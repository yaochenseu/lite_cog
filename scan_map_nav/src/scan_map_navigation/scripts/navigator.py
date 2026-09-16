#!/usr/bin/python3
"""Map-frame route/task manager. Never receives or publishes robot velocities."""
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
from geometry_msgs.msg import PoseStamped
from hdl_localization.msg import ScanMatchingStatus
from nav_msgs.msg import OccupancyGrid, Path
from nav_msgs.srv import GetPlan
from std_msgs.msg import Bool, String, UInt32
from std_srvs.srv import Trigger, SetBool, SetBoolResponse
from visualization_msgs.msg import Marker
from scan_map_navigation.msg import (NavigateAction, NavigateFeedback, NavigateGoal,
                                     NavigateResult, NavigationControl, LocalTarget, PlannerState, LeaseRecovery)
from nav_math import angle
from rolling_route import OrderedRoute, GuideRecovery, distance, planar_transform, transform_point, correction_size
from localization_guard import LocalizationJumpGuard


class TaskCancelled(Exception):
    pass


class LocalizationTimeout(RuntimeError):
    """Only freshness/unavailability, never bad quality or a pose jump."""
    pass


def quat_yaw(q):
    return tf.transformations.euler_from_quaternion([q.x,q.y,q.z,q.w])[2]


class Navigator:
    def __init__(self):
        self.tf = tf.TransformListener()
        self.ready, self.ready_time, self.command_epoch = False, 0, None
        self.grid = None
        self.poisoned = False
        self.task_id, self.task_epoch = 0, 0
        self.planner_status = None
        self.minimum_generation = 0
        self.control_lock = threading.RLock()
        self.control_intent = None
        self.control_progress = 0.0
        self.lease_request = None
        self.lease_recovery_done = 0
        self.last_fault = ''
        self.hard_fault_serial = 0
        self.hard_fault_reason = ''
        self.hard_fault_baseline = 0
        self.jump_resume_pending = False
        self.latest_ndt = None
        self.ndt_min_inliers = rospy.get_param('/scan_velocity_gate/min_inlier_fraction',0.5)
        self.ndt_max_error = rospy.get_param('/scan_velocity_gate/max_matching_error',0.3)
        self.last_remaining = float('nan')
        self.test_stalled = False
        self.task_lease_watchdog = rospy.get_param('~task_lease_watchdog',False)
        if type(self.task_lease_watchdog) is not bool:
            raise ValueError('task_lease_watchdog must be a boolean')
        for name,default in dict(xy_tolerance=0.15,yaw_tolerance=0.12,task_timeout=300.0,
                                 stall_timeout=15.0,service_timeout=2.0,lookahead=2.0,
                                 corner_cut=0.12,target_step=0.08,correction_step=0.08,
                                 target_period=0.05,
                                 loop_period=0.05,jump_distance=0.8,jump_yaw=0.5,
                                 local_recovery_limit=4.0,lease_progress_timeout=0.3,
                                 local_retry_wait=0.2,
                                 localization_timeout=1.2,localization_retry_wait=3.0).items():
            value = rospy.get_param('~'+name,default)
            if not math.isfinite(value) or value <= 0:
                raise ValueError('Invalid parameter: '+name)
            setattr(self,name,value)
        self.localization_retries = rospy.get_param('~localization_retries',3)
        if type(self.localization_retries) is not int or not 0 <= self.localization_retries <= 10:
            raise ValueError('Invalid localization_retries (expected 0..10)')
        self.max_replans = rospy.get_param('~max_replans',2)
        self.jump_guard = LocalizationJumpGuard(
            self.jump_distance,self.jump_yaw,
            rospy.get_param('~jump_confirm_frames',5),rospy.get_param('~jump_confirm_time',.3),
            rospy.get_param('~jump_recover_frames',3),rospy.get_param('~jump_recover_time',.15),
            rospy.get_param('~jump_hold_timeout',2.))
        self.guide_extension_failures = rospy.get_param('~guide_extension_failures',3)
        self.guide_extension_step = rospy.get_param('~guide_extension_step',.5)
        self.guide_extension_max_ahead = rospy.get_param('~guide_extension_max_ahead',5.)
        self.guide_extension_motion = rospy.get_param('~guide_extension_motion',.2)
        GuideRecovery(self.guide_extension_failures,self.guide_extension_step,
                      self.guide_extension_max_ahead,self.guide_extension_motion)  # validate
        self.control = rospy.Publisher('/scan_map_nav/control',NavigationControl,queue_size=1,latch=True)
        self.lease_ack = rospy.Publisher('/scan_map_nav/lease_recovery_ack',LeaseRecovery,queue_size=1)
        self.target = rospy.Publisher('/scan_map_nav/local_target',LocalTarget,queue_size=1)
        self.target_marker = rospy.Publisher('/scan_map_nav/target_marker',Marker,queue_size=1)
        self.path = rospy.Publisher('/scan_map_nav/reference_path',Path,queue_size=1,latch=True)
        # Keep short-lived PLANNING/REPLANNING transitions when a service
        # returns within the same cycle; queue_size=1 can silently discard them.
        self.state = rospy.Publisher('/scan_map_nav/task_state',String,queue_size=10,latch=True)
        self.plan = rospy.ServiceProxy('/scan_global/make_plan',GetPlan)
        self.reset_local = rospy.ServiceProxy('/scan_local/reset',Trigger)
        self.reset_controller = rospy.ServiceProxy('/scan_controller/reset',Trigger)
        rospy.Subscriber('/map',OccupancyGrid,lambda m: setattr(self,'grid',m),queue_size=1)
        rospy.Subscriber('/scan_map_nav/ready',Bool,self.on_ready,queue_size=1)
        rospy.Subscriber('/scan_map_nav/command_epoch',UInt32,
                         lambda m: setattr(self,'command_epoch',m.data),queue_size=1)
        rospy.Subscriber('/scan_map_nav/planner_state',PlannerState,self.on_planner_state,queue_size=1)
        rospy.Subscriber('/scan_map_nav/lease_recovery',LeaseRecovery,self.on_lease_recovery,queue_size=1)
        rospy.Subscriber('/scan_map_nav/last_fault',String,self.on_fault,queue_size=10)
        rospy.Subscriber('/status',ScanMatchingStatus,self.on_ndt,queue_size=1)
        self.server = actionlib.SimpleActionServer('/scan_map_nav/navigate',NavigateAction,
                                                  execute_cb=self.execute,auto_start=False)
        self.server.register_preempt_callback(self.stop)
        self.server.start()
        self.client = actionlib.SimpleActionClient('/scan_map_nav/navigate',NavigateAction)
        rospy.Subscriber('/move_base_simple/goal',PoseStamped,
                         lambda m: self.client.send_goal(NavigateGoal(m,True)),queue_size=1)
        rospy.on_shutdown(self.stop)
        if (rospy.get_param('~test_hooks',False) and
                rospy.get_param('/scan_velocity_gate/output_topic','') == '/test/cmd_vel'):
            def test_stall(req):
                self.test_stalled = req.data
                return SetBoolResponse(success=True)
            self.test_service = rospy.Service('~test_stall',SetBool,test_stall)
        threading.Thread(target=self.lease_loop,daemon=True).start()
        self.state.publish(String('IDLE: confirm localization, then send a goal'))

    def on_fault(self,msg):
        self.last_fault = msg.data
        if msg.data and msg.data != 'Stale ndt':
            self.hard_fault_reason = msg.data
            self.hard_fault_serial += 1

    def retry_guard(self,deadline):
        if self.server.is_preempt_requested() or rospy.is_shutdown():
            raise TaskCancelled()
        if self.hard_fault_serial != self.hard_fault_baseline:
            raise RuntimeError('Non-retryable input fault during task: '+self.hard_fault_reason)
        if time.monotonic() >= deadline:
            raise RuntimeError('Task deadline exceeded')

    def on_ndt(self,msg):
        self.latest_ndt = (msg,time.monotonic())

    def recovered_ndt(self,after_stamp):
        # TF and status are different ROS connections: a new TF cannot prove
        # that the corresponding new matching result has arrived and is valid.
        sample = self.latest_ndt
        if sample is None:
            return False
        status,received = sample
        age = (rospy.Time.now()-status.header.stamp).to_sec()
        return (status.header.stamp > after_stamp and
                -0.2 <= age <= self.localization_timeout and
                time.monotonic()-received <= self.localization_timeout and
                status.has_converged and math.isfinite(status.matching_error) and
                status.matching_error <= self.ndt_max_error and
                math.isfinite(status.inlier_fraction) and status.inlier_fraction >= self.ndt_min_inliers)

    def validate_localization_change(self,robot,transform,target=None):
        was_pending = self.jump_guard.pending
        xy = (robot.pose.position.x,robot.pose.position.y)
        result = self.jump_guard.observe(robot.header.stamp.to_nsec(),transform,xy,target,time.monotonic())
        if result == 'HOLD':
            self.stop()
            if not was_pending:
                rospy.logwarn('Suspected localization jump: %.3f m / %.1f deg at TF %.6f; holding STOP for multi-frame confirmation',
                              self.jump_guard.shift,math.degrees(self.jump_guard.turn),robot.header.stamp.to_sec())
                self.clear_scan()  # Discard the old spline once, never execute through uncertain TF.
                self.jump_resume_pending = True
            self.state.publish(String('LOCALIZATION_JUMP_HOLD'))
            self.server.publish_feedback(NavigateFeedback('LOCALIZATION_JUMP_HOLD',self.last_remaining))
            return False
        if result == 'RECOVERED':
            rospy.logwarn('Localization jump recovered on fresh frames; generating a new local trajectory for the same task')
        return True

    def checked_snapshot(self,deadline,target=None):
        while True:
            self.check_task(deadline)
            robot,transform,height = self.snapshot()
            if self.validate_localization_change(robot,transform,target):
                self.check_task(deadline)
                return robot,transform,height
            time.sleep(0.05)

    def wait_localization(self,deadline,after_stamp,label):
        # STOP is held throughout. Readiness alone is insufficient: require a
        # new valid NDT status AND localization TF from AFTER the failure.
        end = min(deadline,time.monotonic()+self.localization_retry_wait)
        while time.monotonic() < end:
            self.retry_guard(deadline)
            self.stop()
            self.state.publish(String(label))
            self.server.publish_feedback(NavigateFeedback(label,self.last_remaining))
            if self.ready and time.monotonic()-self.ready_time <= 0.3:
                try:
                    robot,transform,_ = self.snapshot()
                except LocalizationTimeout:
                    pass
                else:
                    valid = self.validate_localization_change(robot,transform)
                    if valid and robot.header.stamp > after_stamp and self.recovered_ndt(after_stamp):
                        self.retry_guard(deadline)
                        return True
            time.sleep(0.05)
        self.retry_guard(deadline)
        return False

    def on_lease_recovery(self,msg):
        # Empty notifications clear the gate latch, not an in-flight request.
        # Requests are matched to task + epoch before use; old tasks cannot reset
        # a replacement task. A completed id cannot be executed twice.
        if msg.recovery_id and (self.lease_request is None or msg.recovery_id > self.lease_request.recovery_id):
            self.lease_request = msg

    def recover_lease(self,deadline):
        if not self.task_lease_watchdog:
            return False
        request = self.lease_request
        if (request is None or request.recovery_id <= self.lease_recovery_done or
                (request.task_id,request.epoch) != (self.task_id,self.task_epoch)):
            return False
        self.check_task(deadline)
        self.state.publish(String('LEASE_RECOVERY'))
        self.clear_scan()
        self.check_task(deadline)
        # ACK after BOTH resets, never just because the renewal worker is alive.
        ack = copy.deepcopy(request)
        ack.header.stamp = rospy.Time.now()
        self.lease_ack.publish(ack)
        self.lease_recovery_done = request.recovery_id
        return True

    def on_ready(self,msg):
        self.ready,self.ready_time = msg.data,time.monotonic()

    def on_planner_state(self,msg):
        if self.planner_status is None or msg.header.stamp >= self.planner_status.header.stamp:
            self.planner_status = msg

    def local_state(self):
        state = self.planner_status
        if (state is not None and state.task_id == self.task_id and state.epoch == self.task_epoch and
                state.generation >= self.minimum_generation):
            return state
        return None

    def lease(self,mode,yaw=0):
        with self.control_lock:
            if mode != NavigationControl.STOP and self.server.is_preempt_requested():
                raise TaskCancelled()
            msg = NavigationControl()
            msg.header.stamp,msg.header.frame_id = rospy.Time.now(),'odom'
            msg.task_id,msg.epoch,msg.mode,msg.yaw = self.task_id,self.task_epoch,mode,yaw
            # Only the navigation loop (or an explicit STOP) advances progress.
            self.control_intent,self.control_progress = msg,time.monotonic()
            self.control.publish(msg)

    def renew_lease(self):
        with self.control_lock:
            msg = self.control_intent
            if msg is None:
                return
            if msg.mode != NavigationControl.STOP:
                if (self.server.is_preempt_requested() or
                        (self.task_lease_watchdog and
                         time.monotonic()-self.control_progress > self.lease_progress_timeout)):
                    return
                # Retain the last computation's stamp, so a live worker cannot
                # mask a stalled computation when the watchdog is enabled.
                # Disabled mode keeps announcing intent, not fake fresh work;
                # gate/controller skip only the lease age checks in that mode.
                self.control.publish(msg)
            else:
                stopped = copy.deepcopy(msg)
                stopped.header.stamp = rospy.Time.now()
                self.control.publish(stopped)

    def lease_loop(self):
        while not rospy.is_shutdown():
            self.renew_lease()
            time.sleep(0.05)

    def stop(self):
        self.lease(NavigationControl.STOP)

    def call(self,service,*args):
        result,done = [],threading.Event()
        def worker():
            try:
                result.append(service(*args))
            except Exception as exc:
                result.append(exc)
            finally:
                done.set()
        threading.Thread(target=worker,daemon=True).start()
        if not done.wait(self.service_timeout):
            self.poisoned = True
            raise RuntimeError('Service timeout: '+service.resolved_name)
        if isinstance(result[0],Exception):
            raise result[0]
        return result[0]

    def clear_scan(self):
        self.stop()
        old = self.local_state()
        if old is not None:
            self.minimum_generation = max(self.minimum_generation,old.generation+1)
        for service in (self.reset_local,self.reset_controller):
            if not self.call(service).success:
                raise RuntimeError('SCAN reset failed')

    def retry_local_target(self,point,final,deadline,reason,label='LOCAL_RETRY'):
        # A local failure is NOT evidence that the static global route changed.
        # Hold STOP between bounded SCAN attempts, then reset only local state.
        # The caller retains its OrderedRoute, task identity and map-frame goal.
        self.stop()
        rospy.logwarn('Local planning blocked: %s; keeping route, retrying after %.1fs',
                      reason,self.local_retry_wait)
        end = time.monotonic()+self.local_retry_wait
        while True:
            self.stop()
            self.check_task(deadline)
            robot,transform,_ = self.checked_snapshot(deadline,point)
            self.state.publish(String('BLOCKED_WAIT'))
            self.server.publish_feedback(NavigateFeedback('BLOCKED_WAIT',self.last_remaining))
            if time.monotonic() >= end:
                break
            time.sleep(0.05)
        self.clear_scan()
        self.check_task(deadline)
        robot,transform,height = self.checked_snapshot(deadline,point)
        self.check_task(deadline)
        # Same map point, but current localization correction and a new local
        # generation. TRACK cannot release motion until SCAN checks a new spline.
        self.publish_target(point,final,transform,height)
        self.lease(NavigationControl.TRACK)
        self.state.publish(String(label))
        self.server.publish_feedback(NavigateFeedback(label,self.last_remaining))
        return transform,time.monotonic()

    def target_update_due(self,point,final,sent_point,sent_final,transform,sent_transform,elapsed):
        # Elapsed time only limits rate; it must never force a refresh of a
        # stationary target. Compare with the last SENT values so small real
        # changes accumulate, while sub-threshold jitter does not reset SCAN.
        if sent_point is None:
            return True
        if elapsed < self.target_period:
            return False
        shift = distance(point,sent_point)
        return (shift >= self.target_step or final != sent_final or
                correction_size(sent_transform,transform,[point])[0] >= self.correction_step)

    def snapshot(self):
        # Both poses use ONE common time. Upstream NDT's timestamp skew remains
        # an upstream limitation; do not introduce more skew here.
        try:
            stamp = self.tf.getLatestCommonTime('map','base_link')
            age = (rospy.Time.now()-stamp).to_sec()
            if stamp.to_sec() <= 0 or age < -0.2:
                raise RuntimeError('Invalid localization TF timestamp')
            if age > self.localization_timeout:
                raise LocalizationTimeout('Stale map/body TF')
            mp,mq = self.tf.lookupTransform('map','base_link',stamp)
            op,oq = self.tf.lookupTransform('odom','base_link',stamp)
        except (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException) as exc:
            raise LocalizationTimeout('Localization TF unavailable: '+str(exc))
        if not all(math.isfinite(v) for v in tuple(mp)+tuple(mq)+tuple(op)+tuple(oq)):
            raise RuntimeError('Non-finite localization/body TF')
        myaw = tf.transformations.euler_from_quaternion(mq)[2]
        oyaw = tf.transformations.euler_from_quaternion(oq)[2]
        pose = PoseStamped()
        pose.header.frame_id,pose.header.stamp = 'map',stamp
        pose.pose.position.x,pose.pose.position.y,pose.pose.position.z = mp
        q = pose.pose.orientation
        q.x,q.y,q.z,q.w = mq
        transform = planar_transform((mp[0],mp[1],myaw),(op[0],op[1],oyaw))
        return pose,transform,op[2]

    def check_task(self,deadline):
        self.retry_guard(deadline)
        if self.task_epoch != self.command_epoch:
            if self.last_fault == 'Stale ndt':
                raise LocalizationTimeout('Stale ndt')
            raise RuntimeError('Input fault interrupted task; last gate fault: '+(self.last_fault or 'command epoch revoked'))
        if not self.ready:
            if self.last_fault == 'Stale ndt':
                raise LocalizationTimeout('Stale ndt')
            raise RuntimeError('Navigation inputs unhealthy; last gate fault: '+(self.last_fault or 'not yet received'))
        if time.monotonic()-self.ready_time > 0.3:
            raise RuntimeError('Velocity gate readiness feedback stale')
        if time.monotonic() >= deadline:
            raise RuntimeError('Task deadline exceeded')

    def visible(self,a,b,allow_occupied=False):
        # Goal-selection line-of-sight only, NOT a velocity/footprint check.
        grid = self.grid
        if (grid is None or grid.header.frame_id != 'map' or grid.info.resolution <= 0 or
                len(grid.data) != grid.info.width*grid.info.height):
            return False
        info = grid.info
        yaw = quat_yaw(info.origin.orientation)
        c,s = math.cos(yaw),math.sin(yaw)
        count = max(1,int(math.ceil(distance(a,b)/(info.resolution*0.5))))
        for i in range(count+1):
            u = i/count
            dx = a[0]+u*(b[0]-a[0])-info.origin.position.x
            dy = a[1]+u*(b[1]-a[1])-info.origin.position.y
            x,y = math.floor((c*dx+s*dy)/info.resolution),math.floor((-s*dx+c*dy)/info.resolution)
            if not 0 <= x < info.width or not 0 <= y < info.height:
                return False
            v = grid.data[y*info.width+x]
            if v < 0 or (v >= 65 and not allow_occupied):
                return False
        return True

    def recovery_visible(self,a,b):
        # Only for guides after three local failures: tolerate stale static
        # occupancy, not unknown/map bounds. SCAN's live collision checks remain.
        return self.visible(a,b,allow_occupied=True)

    def make_route(self,start,goal,deadline):
        self.check_task(deadline)
        response = self.call(self.plan,start,goal,0.0)
        self.check_task(deadline)
        if response.plan.header.frame_id != 'map':
            raise RuntimeError('Global path is not in map frame')
        pts = [(p.pose.position.x,p.pose.position.y) for p in response.plan.poses]
        if not pts or not all(math.isfinite(x) and math.isfinite(y) for x,y in pts):
            raise RuntimeError('Invalid/empty global route')
        pts.append((goal.pose.position.x,goal.pose.position.y))
        route = OrderedRoute(pts,self.lookahead,self.corner_cut)
        self.path.publish(response.plan)  # stays in map, never odom
        return route

    def publish_target(self,point,final,transform,height):
        msg = LocalTarget()
        msg.header.frame_id,msg.header.stamp = 'odom',rospy.Time.now()
        msg.epoch,msg.task_id,msg.final_goal = self.task_epoch,self.task_id,final
        msg.position.x,msg.position.y = transform_point(transform,point)
        msg.position.z = height
        self.target.publish(msg)
        marker = Marker()
        marker.header = msg.header
        marker.ns,marker.id,marker.type,marker.action = 'rolling_target',0,Marker.SPHERE,Marker.ADD
        marker.pose.position = msg.position
        marker.pose.orientation.w = 1
        marker.scale.x = marker.scale.y = marker.scale.z = 0.16
        marker.color.r,marker.color.g,marker.color.b,marker.color.a = 1,0.5,0,1
        # Event-driven targets may stay unchanged for longer than two seconds.
        # Keep their visualization without republishing a planning command.
        marker.lifetime = rospy.Duration(0)
        self.target_marker.publish(marker)

    def clear_target_marker(self):
        marker = Marker()
        marker.header.frame_id = 'odom'
        marker.ns,marker.id,marker.action = 'rolling_target',0,Marker.DELETE
        self.target_marker.publish(marker)

    def execute_attempt(self,request,deadline):
        if self.poisoned:
            raise RuntimeError('Previous service timed out; restart navigation')
        self.task_id = time.time_ns()
        self.minimum_generation = 0
        self.task_epoch = self.command_epoch if self.command_epoch is not None else 0
        self.check_task(deadline)
        goal = copy.deepcopy(request.target_pose)
        p,q = goal.pose.position,goal.pose.orientation
        if goal.header.frame_id != 'map' or not all(math.isfinite(v) for v in (p.x,p.y,p.z,q.x,q.y,q.z,q.w)):
            raise RuntimeError('Goal must be finite and in map frame')
        norm = math.sqrt(q.x*q.x+q.y*q.y+q.z*q.z+q.w*q.w)
        if norm < 1e-6:
            if request.require_yaw:
                raise RuntimeError('Fixed-yaw goal needs a valid quaternion')
            q.w = 1
        else:
            q.x,q.y,q.z,q.w = q.x/norm,q.y/norm,q.z/norm,q.w/norm
        p.z = 0
        yaw_goal = quat_yaw(q)
        self.clear_scan()  # task boundary only, not normal target updates
        robot,transform,height = self.checked_snapshot(deadline)
        route = None
        guides = GuideRecovery(self.guide_extension_failures,self.guide_extension_step,
                               self.guide_extension_max_ahead,self.guide_extension_motion)
        sent_point,sent_transform,sent_final = None,None,None
        sent_arc = None
        sent_at = 0
        last_progress = time.monotonic()
        anchor = (robot.pose.position.x,robot.pose.position.y,quat_yaw(robot.pose.orientation))
        replans,settled = 0,0
        recovery_generation,recovery_started = None,0
        while not rospy.is_shutdown():
            # Test hook stalls computation, not callbacks or lease renewal.
            while self.test_stalled and not self.server.is_preempt_requested() and not rospy.is_shutdown():
                time.sleep(0.02)
            robot,transform,height = self.checked_snapshot(deadline,sent_point)
            now = time.monotonic()
            xy = robot.pose.position.x,robot.pose.position.y
            yaw = quat_yaw(robot.pose.orientation)
            remaining = distance(xy,(p.x,p.y))
            self.last_remaining = remaining
            if self.jump_resume_pending:
                # Preserve route/goal/guide policy; a new checked spline is mandatory.
                sent_point = sent_arc = None
                recovery_generation = None
                last_progress = now
                self.jump_resume_pending = False
            if self.recover_lease(deadline):
                # Preserve the static route, but require a newly generated local trajectory.
                sent_point = None
                sent_arc = None
                recovery_generation = None
                last_progress = now
            if distance(xy,anchor) > 0.08 or abs(angle(yaw-anchor[2])) > 0.12:
                last_progress,anchor = now,(xy[0],xy[1],yaw)
            local = self.local_state()
            if guides.observe_motion(transform_point(transform,xy),
                                     local is not None and local.state == PlannerState.TRACKING):
                rospy.loginfo('Guide failure count reset: TRACKING odom displacement reached %.2f m',self.guide_extension_motion)
            recovering = local is not None and local.state in (PlannerState.RECOVERING,PlannerState.BLOCKED)
            if recovering and recovery_generation != local.generation:
                recovery_generation,recovery_started = local.generation,now
            if local is not None and local.state == PlannerState.BLOCKED and remaining <= self.xy_tolerance:
                if request.require_yaw and abs(angle(yaw_goal-yaw)) > self.yaw_tolerance:
                    raise RuntimeError('Final orientation blocked: '+local.reason)
            if remaining <= self.xy_tolerance:
                # If localization later moves us outside the arrival band,
                # force a target refresh instead of reusing an old spline.
                sent_point = None
                sent_arc = None
                if not request.require_yaw or abs(angle(yaw_goal-yaw)) <= self.yaw_tolerance:
                    self.stop()
                    settled += 1
                    if settled*self.loop_period >= 0.4:
                        self.server.set_succeeded(NavigateResult(True,'Reached target'))
                        self.state.publish(String('SUCCEEDED'))
                        return
                    state = 'ARRIVED'
                else:
                    settled = 0
                    self.lease(NavigationControl.ALIGN,angle(yaw_goal+transform[2]))
                    state = 'ALIGNING'
            else:
                settled = 0
                if route is None:
                    self.stop()
                    planning_state = 'PLANNING' if replans == 0 else 'REPLANNING_GLOBAL'
                    self.state.publish(String(planning_state))
                    self.server.publish_feedback(NavigateFeedback(planning_state,remaining))
                    route = self.make_route(robot,goal,deadline)
                    last_progress = time.monotonic()
                # Only route invalidity/deviation requests another global path.
                # Local blockage/no progress alone keeps the existing route.
                choice,deviation = route.select(xy,self.visible)
                choice,choice_arc = guides.choose(route,xy,choice,self.recovery_visible)
                # A relaxed guide must not be replaced by normal static/corner
                # checks on the next tick. During recovery keep an already sent
                # guide through the first two retries, so counting can reach three.
                if (choice is None and recovering and sent_point is not None and sent_arc is not None and
                        sent_arc >= route.progress-1e-6 and self.recovery_visible(xy,sent_point)):
                    choice,choice_arc = (sent_point,sent_final),sent_arc
                if choice is None or deviation > 0.8:
                    self.stop()
                    if replans >= self.max_replans:
                        raise RuntimeError('Global route invalid/deviated after replanning')
                    replans += 1
                    self.clear_scan()
                    route,sent_point = None,None
                    sent_arc = None
                    guides.reset()
                    recovery_generation = None
                    self.state.publish(String('REPLANNING_GLOBAL'))
                    continue
                failed_local = recovering and (local.state == PlannerState.BLOCKED or
                                                 now-recovery_started >= self.local_recovery_limit)
                if failed_local or (not recovering and now-last_progress > self.stall_timeout):
                    point,final = (sent_point,sent_final) if sent_point is not None else choice
                    arc = sent_arc if sent_arc is not None else choice_arc
                    active_recovery = guides.active_arc is not None and abs(arc-guides.active_arc) < 1e-6
                    if not active_recovery and route.checked_target(xy,arc,self.visible) is None:
                        (point,final),arc = choice,choice_arc
                    label = 'LOCAL_RETRY'
                    extended = guides.failed(route,xy,arc,self.recovery_visible)
                    if extended is not None:
                        (point,final),arc,extra = extended
                        label = 'TRY_ENDPOINT' if final else 'EXTENDING_TARGET +%.1fm' % extra
                    rospy.logwarn('Guide recovery: failures=%d, guide_arc=%.2f, endpoint_arc=%.2f; %s',
                                  guides.failures,arc,route.lengths[-1],guides.reason)
                    reason = local.reason if failed_local else 'No local motion progress'
                    sent_transform,sent_at = self.retry_local_target(point,final,deadline,reason,label)
                    if extended is not None:
                        guides.commit(arc)
                    sent_point,sent_final = point,final
                    sent_arc = arc
                    # retry_local_target already published a freshly checked target.
                    self.jump_resume_pending = False
                    last_progress = sent_at
                    recovery_generation = None
                    continue
                if recovering and not failed_local:
                    self.lease(NavigationControl.TRACK)
                    self.state.publish(String('LOCAL_RECOVERY'))
                    self.server.publish_feedback(NavigateFeedback('LOCAL_RECOVERY',remaining))
                    time.sleep(self.loop_period)
                    continue
                point,final = choice
                if self.target_update_due(point,final,sent_point,sent_final,transform,sent_transform,now-sent_at):
                    self.check_task(deadline)
                    self.publish_target(point,final,transform,height)
                    sent_point,sent_transform,sent_final,sent_at = point,transform,final,now
                    sent_arc = choice_arc
                self.lease(NavigationControl.TRACK)
                state = 'TRACKING'
            self.state.publish(String(state))
            self.server.publish_feedback(NavigateFeedback(state,remaining))
            if now-last_progress > self.stall_timeout:
                raise RuntimeError('No motion progress')
            time.sleep(self.loop_period)

    def execute(self,request):
        self.stop()
        self.hard_fault_baseline = self.hard_fault_serial
        self.jump_guard.reset()
        self.jump_resume_pending = False
        self.last_remaining = float('nan')
        deadline = time.monotonic()+self.task_timeout
        retries = 0
        try:
            while not rospy.is_shutdown():
                try:
                    self.execute_attempt(request,deadline)
                    return
                except LocalizationTimeout as exc:
                    # A gate-revoked epoch is never revived by a retry:
                    # reset, wait, then build a NEW internal task and
                    # a new global/local route for the SAME user action goal.
                    self.stop()
                    after_stamp = rospy.Time.now()
                    self.retry_guard(deadline)
                    self.clear_scan()
                    restored = False
                    while retries < self.localization_retries:
                        retries += 1
                        label = 'LOCALIZATION_RECOVERY %d/%d' % (retries,self.localization_retries)
                        rospy.logwarn('%s: %s; stopped, waiting for fresh localization',label,exc)
                        if self.wait_localization(deadline,after_stamp,label):
                            restored = True
                            break
                    if not restored:
                        raise RuntimeError('Localization recovery exhausted (%d retries): %s' %
                                           (self.localization_retries,exc))
        except TaskCancelled:
            self.stop()
            if self.server.is_active():
                self.server.set_preempted(NavigateResult(False,'Cancelled'))
            self.state.publish(String('CANCELLED'))
        except Exception as exc:
            self.stop()
            rospy.logerr('Navigation aborted: %s',exc)
            if self.server.is_active():
                self.server.set_aborted(NavigateResult(False,str(exc)))
            self.state.publish(String('ABORTED: '+str(exc)))
        finally:
            self.stop()
            try:
                self.clear_scan()
            except Exception as exc:
                rospy.logwarn('Stop/reset service: %s',exc)
            self.clear_target_marker()


if __name__ == '__main__':
    rospy.init_node('scan_navigator')
    Navigator()
    rospy.spin()
