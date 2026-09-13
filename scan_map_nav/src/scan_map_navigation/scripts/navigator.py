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
from nav_msgs.msg import OccupancyGrid, Path
from nav_msgs.srv import GetPlan
from std_msgs.msg import Bool, String, UInt32
from std_srvs.srv import Trigger
from visualization_msgs.msg import Marker
from scan_map_navigation.msg import (NavigateAction, NavigateFeedback, NavigateGoal,
                                     NavigateResult, NavigationControl, LocalTarget)
from nav_math import angle
from rolling_route import OrderedRoute, distance, planar_transform, transform_point, correction_size


class TaskCancelled(Exception):
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
        self.control_lock = threading.RLock()
        for name,default in dict(xy_tolerance=0.15,yaw_tolerance=0.12,task_timeout=300.0,
                                 stall_timeout=15.0,service_timeout=2.0,lookahead=0.9,
                                 corner_cut=0.12,target_step=0.18,correction_step=0.08,
                                 target_period=0.3,jump_distance=0.8,jump_yaw=0.5).items():
            value = rospy.get_param('~'+name,default)
            if not math.isfinite(value) or value <= 0:
                raise ValueError('Invalid parameter: '+name)
            setattr(self,name,value)
        self.max_replans = rospy.get_param('~max_replans',2)
        self.control = rospy.Publisher('/scan_map_nav/control',NavigationControl,queue_size=1,latch=True)
        self.target = rospy.Publisher('/scan_map_nav/local_target',LocalTarget,queue_size=1)
        self.target_marker = rospy.Publisher('/scan_map_nav/target_marker',Marker,queue_size=1)
        self.path = rospy.Publisher('/scan_map_nav/reference_path',Path,queue_size=1,latch=True)
        self.state = rospy.Publisher('/scan_map_nav/task_state',String,queue_size=1,latch=True)
        self.plan = rospy.ServiceProxy('/scan_global/make_plan',GetPlan)
        self.reset_local = rospy.ServiceProxy('/scan_local/reset',Trigger)
        self.reset_controller = rospy.ServiceProxy('/scan_controller/reset',Trigger)
        rospy.Subscriber('/map',OccupancyGrid,lambda m: setattr(self,'grid',m),queue_size=1)
        rospy.Subscriber('/scan_map_nav/ready',Bool,self.on_ready,queue_size=1)
        rospy.Subscriber('/scan_map_nav/command_epoch',UInt32,
                         lambda m: setattr(self,'command_epoch',m.data),queue_size=1)
        self.server = actionlib.SimpleActionServer('/scan_map_nav/navigate',NavigateAction,
                                                  execute_cb=self.execute,auto_start=False)
        self.server.register_preempt_callback(self.stop)
        self.server.start()
        self.client = actionlib.SimpleActionClient('/scan_map_nav/navigate',NavigateAction)
        rospy.Subscriber('/move_base_simple/goal',PoseStamped,
                         lambda m: self.client.send_goal(NavigateGoal(m,True)),queue_size=1)
        rospy.on_shutdown(self.stop)
        self.state.publish(String('IDLE: confirm localization, then send a goal'))

    def on_ready(self,msg):
        self.ready,self.ready_time = msg.data,time.monotonic()

    def lease(self,mode,yaw=0):
        with self.control_lock:
            if mode != NavigationControl.STOP and self.server.is_preempt_requested():
                raise TaskCancelled()
            msg = NavigationControl()
            msg.header.stamp,msg.header.frame_id = rospy.Time.now(),'odom'
            msg.task_id,msg.epoch,msg.mode,msg.yaw = self.task_id,self.task_epoch,mode,yaw
            self.control.publish(msg)

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
        for service in (self.reset_local,self.reset_controller):
            if not self.call(service).success:
                raise RuntimeError('SCAN reset failed')

    def snapshot(self):
        # Both poses use ONE common time. Upstream NDT's timestamp skew remains
        # an upstream limitation; do not introduce more skew here.
        stamp = self.tf.getLatestCommonTime('map','base_link')
        if stamp.to_sec() <= 0 or not -0.2 <= (rospy.Time.now()-stamp).to_sec() <= 0.7:
            raise RuntimeError('Stale map/body TF')
        mp,mq = self.tf.lookupTransform('map','base_link',stamp)
        op,oq = self.tf.lookupTransform('odom','base_link',stamp)
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
        if self.server.is_preempt_requested() or rospy.is_shutdown():
            raise TaskCancelled()
        if not self.ready or time.monotonic()-self.ready_time > 0.3:
            raise RuntimeError('Navigation inputs unhealthy or stale')
        if self.task_epoch != self.command_epoch:
            raise RuntimeError('Input fault interrupted task; resend after recovery')
        if time.monotonic() >= deadline:
            raise RuntimeError('Task deadline exceeded')

    def visible(self,a,b):
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
            if v < 0 or v >= 65:
                return False
        return True

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
        marker.lifetime = rospy.Duration(2.0)
        self.target_marker.publish(marker)

    def execute(self,request):
        self.stop()
        try:
            if self.poisoned:
                raise RuntimeError('Previous service timed out; restart navigation')
            self.task_id = time.time_ns()
            self.task_epoch = self.command_epoch if self.command_epoch is not None else 0
            deadline = time.monotonic()+self.task_timeout
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
            robot,transform,height = self.snapshot()
            last_transform = transform
            route = None
            sent_point,sent_transform,sent_final = None,None,None
            sent_at = 0
            last_progress = time.monotonic()
            anchor = (robot.pose.position.x,robot.pose.position.y,quat_yaw(robot.pose.orientation))
            replans,settled = 0,0
            while not rospy.is_shutdown():
                self.check_task(deadline)
                now = time.monotonic()
                robot,transform,height = self.snapshot()
                xy = robot.pose.position.x,robot.pose.position.y
                yaw = quat_yaw(robot.pose.orientation)
                remaining = distance(xy,(p.x,p.y))
                shift,turn = correction_size(last_transform,transform,[xy,sent_point or xy])
                if shift > self.jump_distance or turn > self.jump_yaw:
                    raise RuntimeError('Large localization jump; check RViz and resend goal')
                last_transform = transform
                if distance(xy,anchor) > 0.08 or abs(angle(yaw-anchor[2])) > 0.12:
                    last_progress,anchor = now,(xy[0],xy[1],yaw)
                if remaining <= self.xy_tolerance:
                    # If localization later moves us outside the arrival band,
                    # force a target refresh instead of reusing an old spline.
                    sent_point = None
                    if not request.require_yaw or abs(angle(yaw_goal-yaw)) <= self.yaw_tolerance:
                        self.stop()
                        settled += 1
                        if settled >= 4:
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
                        self.state.publish(String('PLANNING'))
                        route = self.make_route(robot,goal,deadline)
                        last_progress = time.monotonic()
                    choice,deviation = route.select(xy,self.visible)
                    if choice is None or deviation > 0.8 or now-last_progress > self.stall_timeout:
                        self.stop()
                        if replans >= self.max_replans:
                            raise RuntimeError('Route blocked/deviated or no progress after replanning')
                        replans += 1
                        self.clear_scan()
                        route,sent_point = None,None
                        self.state.publish(String('REPLANNING'))
                        continue
                    point,final = choice
                    changed = (sent_point is None or now-sent_at >= 1.0 or distance(point,sent_point) >= self.target_step or
                               final != sent_final or correction_size(sent_transform,transform,[point])[0] >= self.correction_step)
                    if changed and (sent_point is None or now-sent_at >= self.target_period):
                        self.check_task(deadline)
                        self.publish_target(point,final,transform,height)
                        sent_point,sent_transform,sent_final,sent_at = point,transform,final,now
                    self.lease(NavigationControl.TRACK)
                    state = 'TRACKING'
                self.state.publish(String(state))
                self.server.publish_feedback(NavigateFeedback(state,remaining))
                if now-last_progress > self.stall_timeout:
                    raise RuntimeError('No motion progress')
                time.sleep(0.1)
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


if __name__ == '__main__':
    rospy.init_node('scan_navigator')
    Navigator()
    rospy.spin()
