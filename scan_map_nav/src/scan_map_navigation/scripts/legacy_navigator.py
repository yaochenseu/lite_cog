#!/usr/bin/python3
"""Historical reference only. Not launched by rolling navigation."""
import copy
import math
import os
import sys
import threading
import time
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import actionlib
import rospy
import tf
from geometry_msgs.msg import Pose, PoseArray, PoseStamped, Twist, TwistStamped
from nav_msgs.msg import Odometry, Path
from nav_msgs.srv import GetPlan
from std_msgs.msg import Bool, String, UInt32
from std_srvs.srv import Trigger
from scan_planner.msg import Bspline
from scan_map_navigation.msg import NavigateAction, NavigateFeedback, NavigateGoal, NavigateResult, VelocityCommand
from scan_map_navigation.srv import CheckPoses
from nav_math import angle, integrate, thin_points
from route_recovery import nearby_probes, transform_shift, StableTransformWindow, RefreshBudget


class TaskCancelled(Exception):
    pass


def quat_yaw(q):
    return tf.transformations.euler_from_quaternion([q.x,q.y,q.z,q.w])[2]


def pose_at(x, y, z, yaw):
    p = Pose()
    p.position.x, p.position.y, p.position.z = x, y, z
    p.orientation.z, p.orientation.w = math.sin(yaw/2), math.cos(yaw/2)
    return p


class Navigator:
    def __init__(self):
        self.tf = tf.TransformListener()
        self.odom = None
        self.ready = False
        self.ready_time = 0
        self.command_epoch = None
        self.raw = Twist()
        self.raw_time = 0
        self.spline_stamp = 0
        self.poisoned = False
        self.xy_tolerance = rospy.get_param('~xy_tolerance', 0.15)
        self.yaw_tolerance = rospy.get_param('~yaw_tolerance', 0.12)
        self.task_timeout = rospy.get_param('~task_timeout', 300.0)
        self.stall_timeout = rospy.get_param('~stall_timeout', 15.0)
        self.srv_timeout = rospy.get_param('~service_timeout', 2.0)
        self.static_check = rospy.get_param('~static_check', False)
        self.recovery = dict(shift_distance=0.35, shift_yaw=0.25, probe_horizon=1.5,
                             stable_duration=1.0, stable_distance=0.05, stable_yaw=0.04,
                             wait_timeout=8.0, cooldown=2.0, max_refreshes=3,
                             stopped_speed=0.05, stopped_yaw_speed=0.10)
        self.recovery.update(rospy.get_param('~route_recovery', {}))
        if (any(not math.isfinite(float(v)) or float(v) <= 0 for v in self.recovery.values()) or
                self.recovery['wait_timeout'] <= max(self.recovery['stable_duration'], self.recovery['cooldown']) or
                int(self.recovery['max_refreshes']) != self.recovery['max_refreshes']):
            raise ValueError('Invalid route_recovery parameters')
        self.cmd = rospy.Publisher('/scan_map_nav/desired_cmd', VelocityCommand, queue_size=1)
        self.path = rospy.Publisher('/scan_map_nav/reference_path', Path, queue_size=1)
        self.state = rospy.Publisher('/scan_map_nav/task_state', String, queue_size=1, latch=True)
        self.plan = rospy.ServiceProxy('/scan_global/make_plan', GetPlan)
        self.global_check = (rospy.ServiceProxy('/scan_global/check_poses', CheckPoses)
                             if self.static_check else None)
        self.local_check = rospy.ServiceProxy('/scan_local/check_poses', CheckPoses)
        self.reset_local = rospy.ServiceProxy('/scan_local/reset', Trigger)
        self.reset_controller = rospy.ServiceProxy('/scan_controller/reset', Trigger)
        rospy.Subscriber('/leg_odom2', Odometry, lambda m: setattr(self, 'odom', m), queue_size=1)
        rospy.Subscriber('/scan_map_nav/ready', Bool, self.on_ready, queue_size=1)
        rospy.Subscriber('/scan_map_nav/command_epoch', UInt32,
                         lambda m: setattr(self, 'command_epoch', m.data), queue_size=1)
        rospy.Subscriber('/scan_map_nav/raw_cmd', Twist, self.on_raw, queue_size=1)
        rospy.Subscriber('/scan_map_nav/bspline', Bspline,
                         lambda m: setattr(self, 'spline_stamp', m.start_time.to_sec()), queue_size=1)
        self.server = actionlib.SimpleActionServer('/scan_map_nav/navigate', NavigateAction,
                                                   execute_cb=self.execute, auto_start=False)
        self.server.register_preempt_callback(self.stop)
        self.server.start()
        self.client = actionlib.SimpleActionClient('/scan_map_nav/navigate', NavigateAction)
        rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.rviz_goal, queue_size=1)
        rospy.on_shutdown(self.stop)
        self.state.publish(String('IDLE: confirm localization, then send a goal'))

    def on_ready(self, msg):
        self.ready, self.ready_time = msg.data, time.monotonic()

    def on_raw(self, msg):
        self.raw, self.raw_time = msg, time.monotonic()

    def rviz_goal(self, msg):
        self.client.send_goal(NavigateGoal(target_pose=msg, require_yaw=True))

    def send_cmd(self, cmd, epoch=None):
        stamped = TwistStamped()
        stamped.header.frame_id = 'base_link'
        stamped.header.stamp = rospy.Time.now()
        stamped.twist = cmd
        generation = (self.command_epoch or 0) if epoch is None else epoch
        self.cmd.publish(VelocityCommand(epoch=generation, command=stamped))

    def stop(self):
        self.send_cmd(Twist())

    def call(self, service, *args):
        # A stuck ROS service must not keep the previous command alive.
        result, done = [], threading.Event()
        def worker():
            try:
                result.append(service(*args))
            except Exception as exc:
                result.append(exc)
            finally:
                done.set()
        threading.Thread(target=worker, daemon=True).start()
        if not done.wait(self.srv_timeout):
            self.poisoned = True
            raise RuntimeError('Service timeout: '+service.resolved_name)
        if isinstance(result[0], Exception):
            raise RuntimeError(str(result[0]))
        return result[0]

    def map_pose(self):
        stamp = self.tf.getLatestCommonTime('map', 'base_link')
        if not -0.2 <= (rospy.Time.now()-stamp).to_sec() <= 0.7:
            raise RuntimeError('Stale map -> base_link TF')
        xyz, quat = self.tf.lookupTransform('map', 'base_link', rospy.Time(0))
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = xyz
        (pose.pose.orientation.x, pose.pose.orientation.y,
         pose.pose.orientation.z, pose.pose.orientation.w) = quat
        return pose

    def map_to_odom(self):
        trans, quat = self.tf.lookupTransform('odom', 'map', rospy.Time(0))
        mat = tf.transformations.quaternion_matrix(quat)
        mat[:3, 3] = trans
        return mat, math.atan2(mat[1,0], mat[0,0])

    def check_task(self, task_epoch, deadline):
        if self.server.is_preempt_requested() or rospy.is_shutdown():
            raise TaskCancelled()
        if not self.ready or time.monotonic()-self.ready_time > 0.3:
            raise RuntimeError('Navigation inputs unhealthy or stale')
        if task_epoch != self.command_epoch:
            raise RuntimeError('Input fault interrupted this task; resend goal after recovery')
        if time.monotonic() >= deadline:
            raise RuntimeError('Task deadline exceeded')

    def clear_scan(self):
        self.stop()
        for service in (self.reset_local, self.reset_controller):
            if not self.call(service).success:
                raise RuntimeError('SCAN reset failed')
        self.raw_time = self.spline_stamp = 0

    def report(self, state, distance):
        self.state.publish(String(state))
        self.server.publish_feedback(NavigateFeedback(state, distance))

    def route_error(self, reference, current, points):
        p = self.odom.pose.pose.position
        probes = nearby_probes(reference, (p.x,p.y,p.z), points, self.recovery['probe_horizon'])
        distance, yaw = transform_shift(reference, current, probes)
        changed = distance > self.recovery['shift_distance'] or yaw > self.recovery['shift_yaw']
        return changed, distance, yaw, probes

    def wait_for_localization(self, probes, budget, task_epoch, deadline, distance):
        self.stop()
        budget.begin()
        timeout = time.monotonic()+self.recovery['wait_timeout']
        self.report('WAITING_FOR_LOCALIZATION', distance)
        self.clear_scan()
        stable = StableTransformWindow(self.recovery['stable_duration'],
                                       self.recovery['stable_distance'], self.recovery['stable_yaw'])
        while True:
            self.stop()
            self.check_task(task_epoch, deadline)
            now = time.monotonic()
            if now >= timeout:
                raise RuntimeError('Localization did not stabilize before route refresh timeout')
            try:
                self.map_pose()  # ensure the live map/base TF is still fresh
                current, _ = self.map_to_odom()
            except (tf.Exception, RuntimeError):
                current = None
            velocity = self.odom.twist.twist
            stopped = (math.hypot(velocity.linear.x,velocity.linear.y) <= self.recovery['stopped_speed'] and
                       abs(velocity.angular.z) <= self.recovery['stopped_yaw_speed'])
            if stable.update(now, current, probes, stopped) and budget.cooled_down(now):
                self.report('REPLANNING_AFTER_LOCALIZATION', distance)
                budget.last_plan = now
                return current
            time.sleep(0.05)

    def make_route(self, start, goal, task_epoch, deadline):
        self.stop()
        self.check_task(task_epoch, deadline)
        response = self.call(self.plan, start, goal, 0.0)
        if len(response.plan.poses) < 2:
            raise RuntimeError('Dijkstra returned no usable route')
        self.clear_scan()
        self.check_task(task_epoch, deadline)
        transform, _ = self.map_to_odom()
        route = Path()
        route.header.frame_id = 'odom'
        route.header.stamp = rospy.Time.now()
        pts = thin_points([(p.pose.position.x, p.pose.position.y) for p in response.plan.poses])
        for x,y in pts:
            xyz = transform.dot([x,y,0,1])
            p = PoseStamped()
            p.header = route.header
            p.pose = pose_at(xyz[0], xyz[1], self.odom.pose.pose.position.z, 0)
            route.poses.append(p)
        self.raw_time = 0
        self.spline_stamp = 0
        self.check_task(task_epoch, deadline)
        self.path.publish(route)
        return transform, route.header.stamp.to_sec(), pts

    def safe_command(self, cmd, robot_map):
        local = PoseArray()
        local.header.frame_id = 'odom'
        checks = [(self.local_check, self.odom.pose.pose, local)]
        if self.static_check:
            global_samples = PoseArray()
            global_samples.header.frame_id = 'map'
            checks.append((self.global_check, robot_map.pose, global_samples))
        # Check swept footprint over a 0.8s braking/lookahead envelope, including
        # in-place final yaw. The independent gate expires commands in 0.25s.
        for i in range(9):
            t = i*0.1
            for _, source, dest in checks:
                x,y,yaw = integrate(source.position.x, source.position.y, quat_yaw(source.orientation),
                                    cmd.linear.x, cmd.linear.y, cmd.angular.z, t)
                dest.poses.append(pose_at(x,y,source.position.z,yaw))
        for service, _, samples in checks:
            result = self.call(service, samples)
            if not result.safe:
                return result.message
        return ''

    def execute(self, request):
        result = NavigateResult(success=False)
        self.stop()
        try:
            if self.poisoned:
                raise RuntimeError('Previous service timed out; restart this navigation stack before retrying')
            if (not self.ready or time.monotonic()-self.ready_time > 0.3 or
                    self.odom is None or self.command_epoch is None):
                raise RuntimeError('Inputs not ready/healthy. Check /scan_map_nav/gate_state')
            task_epoch = self.command_epoch
            goal = copy.deepcopy(request.target_pose)
            if goal.header.frame_id != 'map':
                raise RuntimeError('Target frame must be map')
            p,q = goal.pose.position,goal.pose.orientation
            if not all(math.isfinite(v) for v in (p.x,p.y,p.z,q.x,q.y,q.z,q.w)):
                raise RuntimeError('Non-finite goal')
            norm = math.sqrt(q.x*q.x+q.y*q.y+q.z*q.z+q.w*q.w)
            if norm < 1e-6:
                if request.require_yaw:
                    raise RuntimeError('Fixed-yaw goal needs a valid quaternion')
                goal.pose.orientation.w = 1
            else:
                q.x,q.y,q.z,q.w = q.x/norm,q.y/norm,q.z/norm,q.w/norm
            goal.pose.position.z = 0
            robot = self.map_pose()
            yaw_goal = quat_yaw(goal.pose.orientation)
            started = moved = time.monotonic()
            deadline = started+self.task_timeout
            budget = RefreshBudget(self.recovery['max_refreshes'], self.recovery['cooldown'])
            budget.last_plan = started
            reference_tf, _ = self.map_to_odom()
            reference_points = [(robot.pose.position.x,robot.pose.position.y),(p.x,p.y)]
            last_pos = (robot.pose.position.x,robot.pose.position.y,quat_yaw(robot.pose.orientation))
            route_data = None
            blocked_since = None
            settled = 0
            while not rospy.is_shutdown():
                self.check_task(task_epoch, deadline)
                now = time.monotonic()
                robot = self.map_pose()
                x,y = robot.pose.position.x,robot.pose.position.y
                yaw = quat_yaw(robot.pose.orientation)
                distance = math.hypot(p.x-x,p.y-y)
                yaw_error = angle(yaw_goal-yaw)
                current_tf, _ = self.map_to_odom()
                changed, shift, yaw_shift, probes = self.route_error(reference_tf, current_tf, reference_points)
                if changed:
                    self.stop()
                    rospy.logwarn('Route correction: nearby shift %.3f m, yaw %.1f deg; refreshing goal (%d/%d)',
                                  shift, math.degrees(yaw_shift), budget.count+1, budget.maximum)
                    reference_tf = self.wait_for_localization(probes, budget, task_epoch, deadline, distance)
                    route_data = None
                    robot = self.map_pose()
                    reference_points = [(robot.pose.position.x,robot.pose.position.y),(p.x,p.y)]
                    moved = time.monotonic()  # deliberate stabilization pauses are not a navigation stall
                    last_pos = (robot.pose.position.x,robot.pose.position.y,quat_yaw(robot.pose.orientation))
                    blocked_since = None
                    settled = 0
                    continue
                if math.hypot(x-last_pos[0],y-last_pos[1]) > 0.08 or abs(angle(yaw-last_pos[2])) > 0.12:
                    moved, last_pos = now,(x,y,yaw)
                if now-moved > self.stall_timeout:
                    raise RuntimeError('No motion progress; inspect obstacles/route before retry')
                cmd = Twist()
                state = 'TRACKING'
                if distance <= self.xy_tolerance:
                    state = 'ALIGNING' if request.require_yaw else 'ARRIVED'
                    if not request.require_yaw or abs(yaw_error) <= self.yaw_tolerance:
                        self.stop()
                        settled += 1
                        if settled >= 4:
                            self.server.set_succeeded(NavigateResult(True, 'Reached target'))
                            self.state.publish(String('SUCCEEDED'))
                            return
                        time.sleep(0.05)
                        continue
                    cmd.angular.z = max(-0.4,min(0.4,1.2*yaw_error))
                else:
                    settled = 0
                    if route_data is None:
                        route_data = self.make_route(robot,goal,task_epoch,deadline)
                        reference_tf, _, reference_points = route_data
                        budget.last_plan = time.monotonic()
                        time.sleep(0.05)
                        continue
                    _, issue_stamp, _ = route_data
                    if self.spline_stamp >= issue_stamp and now-self.raw_time <= 0.25:
                        cmd = copy.deepcopy(self.raw)
                    else:
                        state = 'WAITING_FOR_SCAN'
                # Check capped command; the gate independently enforces the same limits.
                if not all(math.isfinite(v) for v in (cmd.linear.x,cmd.linear.y,cmd.angular.z)):
                    raise RuntimeError('Non-finite SCAN controller command')
                cmd.linear.x = max(-0.18,min(0.35,cmd.linear.x))
                cmd.linear.y = max(-0.25,min(0.25,cmd.linear.y))
                cmd.angular.z = max(-0.8,min(0.8,cmd.angular.z))
                if any(abs(v)>1e-5 for v in (cmd.linear.x,cmd.linear.y,cmd.angular.z)):
                    reason = self.safe_command(cmd,robot)
                    if reason:
                        cmd = Twist()
                        state = 'BLOCKED: '+reason
                        blocked_since = now if blocked_since is None else blocked_since
                        if now-blocked_since > 3.0:
                            raise RuntimeError(state)
                    else:
                        blocked_since = None
                # A cancellation may arrive while a service call is in flight.
                self.check_task(task_epoch, deadline)
                latest_tf, _ = self.map_to_odom()
                if self.route_error(reference_tf, latest_tf, reference_points)[0]:
                    self.stop()
                    continue
                self.send_cmd(cmd, epoch=task_epoch)
                self.state.publish(String(state))
                self.server.publish_feedback(NavigateFeedback(state,distance))
                time.sleep(0.05)
        except TaskCancelled:
            self.stop()
            if self.server.is_active():
                self.server.set_preempted(NavigateResult(False, 'Cancelled; velocity cleared'))
            self.state.publish(String('CANCELLED'))
        except Exception as exc:
            result.message = str(exc)
            rospy.logerr('Navigation aborted: %s', exc)
            self.state.publish(String('ABORTED: '+str(exc)))
            if self.server.is_active():
                self.server.set_aborted(result)
        finally:
            self.stop()
            for service in (self.reset_local,self.reset_controller):
                try:
                    self.call(service)
                except Exception as exc:
                    rospy.logwarn('Stop/reset service: %s',exc)


if __name__ == '__main__':
    rospy.init_node('scan_navigator')
    Navigator()
    rospy.spin()
