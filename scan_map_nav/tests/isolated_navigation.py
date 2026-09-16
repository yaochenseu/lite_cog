#!/usr/bin/python3
"""Run real global+SCAN+controller+gate against a synthetic robot on a PRIVATE master.

Never connects to the robot master, never starts transfer/ros2qnx, and all final
velocity output is /test/cmd_vel. Temporary files contain test logs only.
"""
import math
import os
import pathlib
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
import xmlrpc.client

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src/scan_map_navigation/scripts'))
from nav_math import integrate
from synthetic_lidar import scan as lidar_scan


def wait_until(fn, timeout=30):
    end = time.monotonic()+timeout
    while time.monotonic()<end:
        try:
            if fn():
                return
        except Exception:
            pass
        time.sleep(0.05)
    raise AssertionError('Timed out: '+str(fn))


def main():
    logs = tempfile.mkdtemp(prefix='scan_map_nav_test_')
    print('Isolated test logs: '+logs,flush=True)
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0))
        port = sock.getsockname()[1]
    assert port != 11311
    os.environ.update(ROS_MASTER_URI='http://127.0.0.1:'+str(port),ROS_IP='127.0.0.1',
                      ROS_HOSTNAME='localhost',ROS_HOME=logs,ROS_LOG_DIR=logs)
    processes,streams = [],[]
    def start(cmd,name):
        stream = open(os.path.join(logs,name+'.log'),'w')
        streams.append(stream)
        proc = subprocess.Popen(cmd,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        processes.append(proc)
        return proc
    done = threading.Event()
    try:
        start(['roscore','-p',str(port)],'master')
        master = xmlrpc.client.ServerProxy(os.environ['ROS_MASTER_URI'])
        wait_until(lambda: master.getPid('/test')[0]==1)
        import rospy
        import tf
        import actionlib
        from actionlib_msgs.msg import GoalStatus
        from geometry_msgs.msg import PoseStamped, PoseArray, Twist
        from nav_msgs.msg import Odometry, OccupancyGrid, Path
        from nav_msgs.srv import GetPlan
        from sensor_msgs.msg import Imu,PointCloud2
        from sensor_msgs import point_cloud2
        from std_msgs.msg import Header,String
        from hdl_localization.msg import ScanMatchingStatus
        from scan_map_navigation.msg import (NavigateAction,NavigateGoal,LocalTarget,PlannerState,
                                            LocalTrajectory,NavigationControl,LeaseRecovery)
        from std_msgs.msg import UInt32
        from std_srvs.srv import SetBool
        from scan_map_navigation.srv import CheckPoses
        rospy.init_node('isolated_robot_test',anonymous=True,disable_signals=True)
        broadcaster = tf.TransformBroadcaster()
        odom_pub = rospy.Publisher('/leg_odom2',Odometry,queue_size=1)
        imu_pub = rospy.Publisher('/imu/data',Imu,queue_size=1)
        ndt_pub = rospy.Publisher('/status',ScanMatchingStatus,queue_size=1)
        cloud_pub = rospy.Publisher('/rslidar_points',PointCloud2,queue_size=1)
        map_pub = rospy.Publisher('/map',OccupancyGrid,queue_size=1,latch=True)
        state = {'x':0.0,'y':0.0,'yaw':0.0,'cmd':Twist(),'cmd_time':0,
                 'cloud':True,'ndt':True,'gate':'','motion':False,
                 'tf_offset':0.0,'wobble':False,'task':'','history':[],'routes':[],'targets':[],
                 'planner':None,'epoch':0,'reported_speed':None,'trajectories':[],
                 'extra_boxes':[],'samples':[],'target_observations':[],
                 'ndt_publish':True,'ndt_age':0.0,'localization_tf':True,
                 'control':None,'lease_requests':[]}
        def velocity(m):
            state['cmd'],state['cmd_time'] = m,time.monotonic()
            if abs(m.linear.x)+abs(m.linear.y)+abs(m.angular.z)>1e-4:
                state['motion'] = True
        rospy.Subscriber('/test/cmd_vel',Twist,velocity,queue_size=1)
        rospy.Subscriber('/scan_map_nav/gate_state',String,
                         lambda m: state.update(gate=m.data),queue_size=1)
        def task_state(m):
            state['task'] = m.data
            state['history'].append(m.data)
        rospy.Subscriber('/scan_map_nav/task_state',String,task_state,queue_size=10)
        rospy.Subscriber('/scan_map_nav/reference_path',Path,
                         lambda m: state['routes'].append(m),queue_size=10)
        def target_received(m):
            state['targets'].append(m)
            state['target_observations'].append((m,state['x'],state['y']))
        rospy.Subscriber('/scan_map_nav/local_target',LocalTarget,target_received,queue_size=10)
        rospy.Subscriber('/scan_map_nav/planner_state',PlannerState,
                         lambda m: state.update(planner=m),queue_size=10)
        rospy.Subscriber('/scan_map_nav/command_epoch',UInt32,
                         lambda m: state.update(epoch=m.data),queue_size=10)
        rospy.Subscriber('/scan_map_nav/local_trajectory',LocalTrajectory,
                         lambda m: state['trajectories'].append(m),queue_size=10)
        rospy.Subscriber('/scan_map_nav/control',NavigationControl,
                         lambda m: state.update(control=m),queue_size=1)
        rospy.Subscriber('/scan_map_nav/lease_recovery',LeaseRecovery,
                         lambda m: state['lease_requests'].append(m) if m.recovery_id else None,queue_size=10)
        grid = OccupancyGrid()
        grid.header.frame_id='map'
        grid.info.resolution=0.1
        grid.info.width=grid.info.height=100
        grid.info.origin.position.x=grid.info.origin.position.y=-5
        grid.info.origin.orientation.w=1
        grid.data=[0]*10000
        for i in range(100):
            for j in range(100):
                if i in (0,99) or j in (0,99) or (i==65 and 42<=j<=58):
                    grid.data[j*100+i]=100
        # Static map is latched ONCE with an intentionally old stamp.
        # Sensor/TF freshness remains live and independently enforced.
        grid.header.stamp=rospy.Time.from_sec(1)
        map_pub.publish(grid)
        def sensors():
            last = time.monotonic()
            tick=0
            while not done.is_set() and not rospy.is_shutdown():
                now=time.monotonic()
                dt=min(now-last,0.05)
                last=now
                cmd = state['cmd'] if now-state['cmd_time']<0.25 else Twist()
                state['x'],state['y'],state['yaw']=integrate(state['x'],state['y'],state['yaw'],
                                                          cmd.linear.x,cmd.linear.y,cmd.angular.z,dt)
                if state['extra_boxes']:
                    state['samples'].append((state['x'],state['y'],state['yaw']))
                stamp=rospy.Time.now()
                # Leg odometry is continuous and independent of NDT correction.
                # state x/y are physical position in the ORIGINAL map. Changing
                # tf_offset changes only localization, never this odometry.
                ca,sa=math.cos(0.3),math.sin(0.3)
                offset = state['tf_offset']
                if state['wobble']:
                    offset += 0.45 if int(now/0.15)%2 else -0.45
                tx = 1.0+offset
                ox=ca*(state['x']-1.0)+sa*(state['y']+0.5)
                oy=-sa*(state['x']-1.0)+ca*(state['y']+0.5)
                quat=tf.transformations.quaternion_from_euler(0,0,state['yaw']-0.3)
                if state['localization_tf']:
                    broadcaster.sendTransform((tx,-0.5,0),tf.transformations.quaternion_from_euler(0,0,0.3),stamp,'odom','map')
                broadcaster.sendTransform((ox,oy,0.327),quat,stamp,'base_link','odom')
                broadcaster.sendTransform((0.187,0,0.073),tf.transformations.quaternion_from_euler(0,math.pi/10,0),
                                          stamp,'rslidar','base_link')
                odom=Odometry()
                odom.header.stamp=stamp
                odom.header.frame_id='odom'
                odom.child_frame_id='base_link'
                odom.pose.pose.position.x=ox
                odom.pose.pose.position.y=oy
                odom.pose.pose.position.z=0.327
                q=odom.pose.pose.orientation
                q.x,q.y,q.z,q.w=quat
                odom.twist.twist=Twist()
                odom.twist.twist.linear.x=cmd.linear.x if state['reported_speed'] is None else state['reported_speed']
                odom.twist.twist.linear.y=cmd.linear.y
                odom.twist.twist.angular.z=cmd.angular.z
                odom_pub.publish(odom)
                imu=Imu()
                imu.header=odom.header
                imu.header.frame_id='base_link'
                imu.orientation.w=1
                imu.linear_acceleration.z=9.81
                imu_pub.publish(imu)
                if tick%5==0:
                    ndt=ScanMatchingStatus()
                    ndt.header=Header(stamp=stamp-rospy.Duration(state['ndt_age']),frame_id='rslidar')
                    ndt.has_converged=state['ndt']
                    ndt.matching_error=0.01
                    ndt.inlier_fraction=0.9
                    if state['ndt_publish']:
                        ndt_pub.publish(ndt)
                    if state['cloud']:
                        points=lidar_scan(state['x'],state['y'],state['yaw'],
                                         [((1.5,-.8,0),(1.6,.8,1.2))]+state['extra_boxes'])
                        cloud_pub.publish(point_cloud2.create_cloud_xyz32(Header(stamp=stamp,frame_id='rslidar'),points))
                tick+=1
                time.sleep(0.02)
        threading.Thread(target=sensors,daemon=True).start()
        scenario=os.environ.get('SCAN_NAV_SCENARIO','')
        launch_args=['roslaunch','scan_map_navigation','navigation.launch','localization:=false',
                     'rviz:=false','output_topic:=/test/cmd_vel','test_hooks:=true']
        # Existing recovery scenarios deliberately retain their opt-in watchdog.
        # lease_disabled omits the argument to test the production DEFAULT.
        if scenario not in ('lease_disabled','guide_extension','jump_confirmation','static_recovery'):
            launch_args.append('task_lease_watchdog:=true')
        launch=start(launch_args,'navigation')
        rospy.wait_for_service('/scan_global/make_plan',timeout=60)
        rospy.wait_for_service('/scan_local/check_poses',timeout=60)
        rospy.wait_for_service('/scan_local/test_obstacle',timeout=60)
        obstacle=rospy.ServiceProxy('/scan_local/test_obstacle',SetBool)
        rospy.wait_for_service('/scan_navigator/test_stall',timeout=60)
        stall=rospy.ServiceProxy('/scan_navigator/test_stall',SetBool)
        wait_until(lambda: state['gate'] in ('READY','IDLE'),60)
        assert rospy.get_param('/scan_local/fsm/navi_mode') == 4
        assert not state['motion'], 'Movement without a goal'
        print('PASS: automatically READY without an unlock call; idle stays stopped',flush=True)
        def pose(x,y,yaw=0):
            p=PoseStamped()
            p.header=Header(frame_id='map',stamp=rospy.Time.now())
            p.pose.position.x=x
            p.pose.position.y=y
            p.pose.orientation.z=math.sin(yaw/2)
            p.pose.orientation.w=math.cos(yaw/2)
            return p
        planner=rospy.ServiceProxy('/scan_global/make_plan',GetPlan)
        route=planner(pose(0,0),pose(3,0),0).plan
        assert len(route.poses)>10 and max(abs(p.pose.position.y) for p in route.poses)>0.8
        print('PASS: Dijkstra detours around static wall',flush=True)
        samples=PoseArray(header=Header(frame_id='map'),poses=[pose(1.5,0).pose])
        assert not rospy.ServiceProxy('/scan_global/check_poses',CheckPoses)(samples).safe
        print('PASS: static swept-footprint rejection',flush=True)
        client=actionlib.SimpleActionClient('/scan_map_nav/navigate',NavigateAction)
        assert client.wait_for_server(rospy.Duration(10))
        def send(x,y,yaw=0,require=False):
            state['history'].clear()
            client.send_goal(NavigateGoal(target_pose=pose(x,y,yaw),require_yaw=require))
        published={name for name,_ in rospy.get_published_topics()}
        assert '/scan_map_nav/planning_grid' not in published
        assert '/scan_map_nav/runtime_grid' not in published
        print('PASS: static latched map works without runtime-grid publishers or age refresh',flush=True)

        if scenario in ('lease_disabled','lease_enabled'):
            enabled=scenario=='lease_enabled'
            for node in ('scan_navigator','scan_velocity_gate','scan_controller'):
                assert rospy.get_param('/'+node+'/task_lease_watchdog') is enabled
            def moving():
                return math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>.04
            def stopped():
                return abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            send(-1.2,0)
            wait_until(moving,20)
            task_before=state['targets'][-1].task_id
            epoch_before=state['epoch']
            generation_before=state['planner'].generation
            routes_before=len(state['routes'])
            xy_before=(state['x'],state['y'])
            assert stall(True).success
            if enabled:
                wait_until(lambda: state['gate'].startswith('LEASE_RECOVERY'),2)
                wait_until(stopped,1)
                time.sleep(.2)
                assert stopped() and state['epoch']==epoch_before
                assert stall(False).success
                assert client.wait_for_result(rospy.Duration(35))
                assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
                assert state['targets'][-1].task_id==task_before
                assert len(state['routes'])==routes_before
                assert 'LEASE_RECOVERY' in state['history']
                assert any(m.task_id==task_before and m.generation>generation_before for m in state['trajectories'])
                print('PASS: opt-in watchdog stops stalled task, then requires reset/new trajectory to resume',flush=True)
            else:
                time.sleep(1.2)  # Exceeds BOTH the former 0.3 and 0.5 s limits.
                assert not state['lease_requests'],state['lease_requests']
                assert 'LEASE_RECOVERY' not in state['history']
                assert state['epoch']==epoch_before
                assert state['planner'].generation==generation_before
                assert (rospy.Time.now()-state['control'].header.stamp).to_sec()>.5
                assert moving(),state['gate']
                assert math.hypot(state['x']-xy_before[0],state['y']-xy_before[1])>.08
                print('PASS: default-off watchdog permits checked trajectory with old lease stamp; no reset/epoch change',flush=True)
                client.cancel_goal()  # Cancellation callbacks work despite the stalled loop.
                assert client.wait_for_result(rospy.Duration(5))
                assert client.get_state()==GoalStatus.PREEMPTED
                wait_until(stopped,1)
                assert stall(False).success
                time.sleep(.3); assert stopped()
                print('PASS: default-off mode still cancels and stops a stalled task',flush=True)

                wait_until(lambda: state['gate']=='IDLE',3)
                send(state['x']-.8,state['y'])
                wait_until(moving,20)
                epoch_before=state['epoch']
                assert stall(True).success
                state['cloud']=False
                wait_until(lambda: state['epoch']>epoch_before,3)
                wait_until(stopped,1)
                assert stall(False).success
                assert client.wait_for_result(rospy.Duration(5))
                assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
                assert 'Stale cloud' in client.get_result().message,str(client.get_result())
                state['cloud']=True
                wait_until(lambda: state['gate']=='IDLE',3)
                time.sleep(.3); assert stopped()
                print('PASS: cloud loss still stops/revokes a stalled task; recovery does not resume it',flush=True)

                send(state['x']+.6,state['y'])
                wait_until(moving,20)
                assert obstacle(True).success
                wait_until(lambda: state['planner'].state in (PlannerState.RECOVERING,PlannerState.BLOCKED),2)
                wait_until(stopped,1)
                time.sleep(.2); assert stopped()
                client.cancel_goal()
                assert client.wait_for_result(rospy.Duration(5))
                assert client.get_state()==GoalStatus.PREEMPTED
                assert obstacle(False).success
                wait_until(lambda: state['gate']=='IDLE',3)
                print('PASS: SCAN candidate rejection still stops motion with watchdog disabled',flush=True)

                send(state['x']+.6,state['y'])
                wait_until(moving,20)
                state['ndt']=False
                assert client.wait_for_result(rospy.Duration(5))
                assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
                assert 'NDT quality' in client.get_result().message,str(client.get_result())
                wait_until(stopped,1)
                state['ndt']=True
                wait_until(lambda: state['gate']=='IDLE',3)
                time.sleep(.3); assert stopped()
                print('PASS: poor NDT quality remains a hard stop with watchdog disabled',flush=True)
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('ALL %s TESTS PASSED (private master; no physical robot commands)'%scenario.upper(),flush=True)
            return

        if scenario=='static_recovery':
            def map_point(msg):
                c,s=math.cos(.3),math.sin(.3)
                return (1+c*msg.position.x-s*msg.position.y,-.5+s*msg.position.x+c*msg.position.y)
            assert rospy.get_param('/scan_navigator/guide_extension_failures')==3
            assert rospy.get_param('/scan_navigator/task_lease_watchdog') is False
            assert obstacle(True).success
            send(-3.2,0)
            wait_until(lambda: bool(state['targets']),15)
            wait_until(lambda: bool(state['routes']),5)
            task=state['targets'][-1].task_id;epoch=state['epoch']
            route_count=len(state['routes'])
            # The global route already exists. Mark future guide cells and its
            # endpoint occupied in the static prior; real lidar still sees free space.
            data=list(grid.data)
            for j in range(47,54):
                for i in range(15,28): data[j*100+i]=100
            grid.data=data
            map_pub.publish(grid)
            wait_until(lambda: 'TRY_ENDPOINT' in state['history'],45)
            wait_until(lambda: state['history'].count('LOCAL_RETRY')>=4,15)
            assert not state['motion'],'SCAN-rejected candidates must never move'
            assert state['epoch']==epoch
            assert len(state['routes'])==route_count
            targets=list(state['targets'])
            points=[map_point(m) for m in targets]
            advances=[]
            for p in points:
                if p[0]<-2.2 and (not advances or abs(p[0]-advances[-1])>.04):advances.append(p[0])
            assert len(advances)==3,advances
            assert all(abs(a-b)<.04 for a,b in zip(advances,(-2.5,-3.,-3.2))),advances
            assert all(p[0]>=-3.21 for p in points),points
            assert targets[-1].final_goal and all(m.task_id==task for m in targets)
            assert grid.data[50*100+18]==100
            assert state['history'].count('TRY_ENDPOINT')==1
            assert 'REPLANNING_GLOBAL' not in state['history']
            print('PASS: three failures permit static-occupied guides in 0.5m steps; endpoint wins before 5m, real SCAN rejection still stops motion',flush=True)
            assert obstacle(False).success
            assert client.wait_for_result(rospy.Duration(50))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['targets'][-1].task_id==task and state['epoch']==epoch
            assert len(state['routes'])==route_count
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('ALL STATIC RECOVERY TESTS PASSED: occupied prior endpoint reached only after checked SCAN trajectory (private master)',flush=True)
            return

        if scenario=='jump_confirmation':
            assert rospy.get_param('/scan_global/global_costmap/inflation_layer/inflation_radius')==.30
            assert rospy.get_param('/scan_navigator/jump_confirm_frames')==5
            assert rospy.get_param('/scan_navigator/jump_recover_frames')==3
            def moving():
                return math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>.03
            def stopped():
                return abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            def holding():
                return state['task']=='LOCALIZATION_JUMP_HOLD'
            send(-1.2,0)
            wait_until(moving,20)
            task_before=state['targets'][-1].task_id;routes_before=len(state['routes'])
            generation_before=state['planner'].generation;epoch_before=state['epoch']
            state['tf_offset']=1.
            wait_until(holding,2);wait_until(stopped,1)
            targets_before=len(state['targets'])
            assert client.get_state()==GoalStatus.ACTIVE
            state['tf_offset']=0.
            time.sleep(.05)
            assert stopped() and len(state['targets'])==targets_before
            assert client.wait_for_result(rospy.Duration(35))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['targets'][-1].task_id==task_before and state['epoch']==epoch_before
            assert len(state['routes'])==routes_before
            assert any(t.task_id==task_before and t.generation>generation_before for t in state['trajectories'])
            print('PASS: transient jump holds STOP; fresh normal frames resume SAME task/route on a new trajectory',flush=True)

            send(state['x']+.7,state['y']);wait_until(moving,20)
            state['tf_offset']=1.
            wait_until(holding,2);wait_until(stopped,1)
            targets_before=len(state['targets'])
            assert client.wait_for_result(rospy.Duration(4))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'Persistent localization jump' in client.get_result().message,str(client.get_result())
            assert len(state['targets'])==targets_before
            state['tf_offset']=0.;time.sleep(.4);assert stopped()
            print('PASS: permanent step cannot become a new baseline; multi-frame confirmation aborts without new target',flush=True)

            send(state['x']+.7,state['y']);wait_until(moving,20)
            state['tf_offset']=1.
            wait_until(holding,2)
            client.cancel_goal()
            assert client.wait_for_result(rospy.Duration(4))
            assert client.get_state()==GoalStatus.PREEMPTED
            state['tf_offset']=0.;time.sleep(.4);assert stopped()
            print('PASS: cancelling during jump confirmation prevents automatic resume',flush=True)

            send(state['x']+.7,state['y']);wait_until(moving,20)
            state['tf_offset']=1.
            wait_until(holding,2)
            state['ndt']=False
            assert client.wait_for_result(rospy.Duration(4))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'NDT quality' in client.get_result().message,str(client.get_result())
            state['tf_offset']=0.;state['ndt']=True;time.sleep(.4);assert stopped()
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('ALL JUMP CONFIRMATION TESTS PASSED (private master; no physical robot commands)',flush=True)
            return

        if os.environ.get('SCAN_NAV_SCENARIO')=='guide_extension':
            assert rospy.get_param('/scan_global/global_costmap/inflation_layer/inflation_radius')==.30
            assert rospy.get_param('/scan_navigator/lookahead')==2.
            assert rospy.get_param('/scan_navigator/target_period')==.05
            assert not rospy.has_param('/scan_navigator/target_resend')
            assert not rospy.has_param('/scan_navigator/target_near_distance')
            assert rospy.get_param('/scan_navigator/target_step')==.08
            assert rospy.get_param('/scan_navigator/local_retry_wait')==.2
            assert rospy.get_param('/scan_navigator/guide_extension_step')==.5
            assert rospy.get_param('/scan_navigator/guide_extension_max_ahead')==5.
            assert rospy.get_param('/scan_navigator/guide_extension_motion')==.2
            assert rospy.get_param('/scan_navigator/task_lease_watchdog') is False
            def map_point(msg):
                c,s=math.cos(.3),math.sin(.3)
                return (1+c*msg.position.x-s*msg.position.y,-.5+s*msg.position.x+c*msg.position.y)

            # Observe updates with a real running controller, before reaching
            # the previous guide (not just parameter assertions).
            start=len(state['target_observations'])
            send(-2.,-3.)
            assert client.wait_for_result(rospy.Duration(45))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            observations=state['target_observations'][start:]
            previous=observations[0][0]
            early=[]; intervals=[]
            for msg,x,y in observations[1:]:
                old,new=map_point(previous),map_point(msg)
                if math.hypot(new[0]-old[0],new[1]-old[1])>=.03:
                    early.append(math.hypot(x-old[0],y-old[1]))
                    intervals.append((msg.header.stamp-previous.header.stamp).to_sec())
                    previous=msg
            assert len(early)>=5,(len(early),early)
            assert early[0]>.35,early
            print('PASS: rolling targets update before reaching old guide; %d advances, first %.2fm early' %
                  (len(early),early[0]),flush=True)

            # Reject all candidates while trying the six half-metre extensions. This
            # verifies the protocol, not an assertion of real obstacle clearance.
            assert obstacle(True).success
            routes_before=len(state['routes']); targets_before=len(state['targets'])
            epoch_before=state['epoch']; state['motion']=False
            # Six-metre free corridor, left of the wall, entirely inside the room.
            recovery_origin=(state['x'],state['y'])
            send(state['x'],state['y']+6.)
            expected=['EXTENDING_TARGET +%.1fm'%v for v in (.5,1.,1.5,2.,2.5,3.)]
            limit=time.monotonic()+60
            while not all(label in state['history'] for label in expected):
                assert time.monotonic()<limit,'Half-metre extension stages not observed'
                assert not state['motion'],'Rejected trajectory produced movement'
                assert state['epoch']==epoch_before
                assert 'REPLANNING_GLOBAL' not in state['history']
                time.sleep(.05)
            assert client.get_state()==GoalStatus.ACTIVE,str(client.get_result())
            assert len(state['routes'])==routes_before+1
            first_extension=state['history'].index(expected[0])
            assert state['history'][:first_extension].count('LOCAL_RETRY')==2
            indices=[state['history'].index(label) for label in expected]
            assert indices==sorted(indices)
            # At 5 m, further failures must retry that point, not keep extending.
            wait_until(lambda: state['history'].count('LOCAL_RETRY')>=4,15)
            assert not state['motion']
            targets=state['targets'][targets_before:]
            task=targets[0].task_id
            base=map_point(targets[0]); distinct=[]
            for msg in targets:
                p=map_point(msg)
                offset=math.hypot(p[0]-base[0],p[1]-base[1])
                if offset>.04 and (not distinct or abs(offset-distinct[-1])>.04):
                    distinct.append(offset)
                assert msg.task_id==task
            assert len(distinct)==6,distinct
            assert all(abs(actual-want)<.04 for actual,want in zip(distinct,(.5,1.,1.5,2.,2.5,3.))),distinct
            last=map_point(targets[-1])
            assert 4.9<math.hypot(last[0]-recovery_origin[0],last[1]-recovery_origin[1])<=5.02
            assert not targets[-1].final_goal
            assert obstacle(False).success
            assert client.wait_for_result(rospy.Duration(65))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert len(state['routes'])==routes_before+1
            assert state['targets'][-1].task_id==task
            assert state['epoch']==epoch_before
            print('PASS: third failure starts 0.5m steps through 5m; capped retries keep SAME route/task, then reach goal',flush=True)

            # Endpoint wins when it is nearer than the five-metre ceiling.
            assert obstacle(True).success
            targets_before=len(state['targets']); state['motion']=False
            endpoint=(state['x'],state['y']-3.2)
            send(*endpoint)
            wait_until(lambda: len(state['targets'])>targets_before and state['targets'][-1].final_goal,35)
            final_index=len(state['targets'])-1
            wait_until(lambda: len(state['targets'])>final_index+1,10)
            assert not state['motion']
            final_targets=state['targets'][final_index:]
            assert all(m.final_goal and math.hypot(map_point(m)[0]-endpoint[0],map_point(m)[1]-endpoint[1])<.01
                       for m in final_targets)
            assert len([s for s in state['history'] if s.startswith('EXTENDING_TARGET')])==2
            assert 'TRY_ENDPOINT' in state['history']
            assert obstacle(False).success
            assert client.wait_for_result(rospy.Duration(45))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            print('PASS: last half-metre step clamps to endpoint; subsequent failures do not extend beyond it',flush=True)

            # Release rejection immediately after the first extension. Actual
            # motion must stop the ladder, without snapping the useful guide back.
            assert obstacle(True).success
            send(state['x'],state['y']-3.)
            wait_until(lambda: 'EXTENDING_TARGET +0.5m' in state['history'],25)
            extended=state['targets'][-1]
            extended_point=map_point(extended)
            release_xy=(state['x'],state['y']); observations_start=len(state['target_observations'])
            assert obstacle(False).success
            wait_until(lambda: math.hypot(state['x']-release_xy[0],state['y']-release_xy[1])>.25,20)
            for msg,x,y in state['target_observations'][observations_start:]:
                if math.hypot(x-release_xy[0],y-release_xy[1])<.3:
                    assert math.hypot(map_point(msg)[0]-extended_point[0],map_point(msg)[1]-extended_point[1])<.04
            assert client.wait_for_result(rospy.Duration(45))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert [s for s in state['history'] if s.startswith('EXTENDING_TARGET')]==['EXTENDING_TARGET +0.5m']
            print('PASS: physical motion after first extension stops the ladder and retains the working guide',flush=True)
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('ALL GUIDE EXTENSION TESTS PASSED (private master; no physical robot commands)',flush=True)
            return

        def persistent_local_retry(dx):
            # A blocked candidate must NOT cause Dijkstra to repeat the same
            # static route. Stay active/stopped across multiple local budgets,
            # including beyond the old 15-second no-progress trigger.
            assert obstacle(True).success
            routes_before=len(state['routes'])
            targets_before=len(state['targets'])
            epoch_before=state['epoch']
            state['motion']=False
            send(state['x']+dx,state['y'])
            wait_until(lambda: state['task']=='BLOCKED_WAIT',12)
            first_task=state['targets'][-1].task_id
            first_generation=state['planner'].generation
            until=time.monotonic()+16
            limit=time.monotonic()+40
            while time.monotonic()<until or state['history'].count('LOCAL_RETRY')<3:
                assert time.monotonic()<limit,'Local retries did not progress'
                assert client.get_state()==GoalStatus.ACTIVE,str(client.get_result())
                assert not state['motion'],'Motion with every candidate rejected'
                assert state['epoch']==epoch_before
                assert len(state['routes'])==routes_before+1
                assert 'REPLANNING_GLOBAL' not in state['history']
                time.sleep(.05)
            assert all(t.task_id==first_task for t in state['targets'][targets_before:])
            assert obstacle(False).success
            assert client.wait_for_result(rospy.Duration(35))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert len(state['routes'])==routes_before+1
            assert state['targets'][-1].task_id==first_task
            assert state['epoch']==epoch_before
            assert any(t.task_id==first_task and t.generation>first_generation for t in state['trajectories'])
            print('PASS: repeated local budgets keep SAME route/task, remain stopped, then resume on checked new trajectory',flush=True)

        if os.environ.get('SCAN_NAV_SCENARIO')=='local_recovery':
            assert rospy.get_param('/scan_navigator/local_retry_wait')==.2
            assert rospy.get_param('/scan_global/global_costmap/inflation_layer/inflation_radius')==.30
            persistent_local_retry(-.65)

            assert obstacle(True).success
            send(state['x']-.6,state['y'])
            wait_until(lambda: state['task']=='BLOCKED_WAIT',12)
            targets_before=len(state['targets'])
            client.cancel_goal()
            assert client.wait_for_result(rospy.Duration(5))
            assert client.get_state()==GoalStatus.PREEMPTED,str(client.get_result())
            assert obstacle(False).success
            time.sleep(1.3)
            assert len(state['targets'])==targets_before
            assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            print('PASS: cancel in BLOCKED_WAIT prevents any later local retry',flush=True)

            assert obstacle(True).success
            send(state['x']-.6,state['y'])
            wait_until(lambda: state['task']=='BLOCKED_WAIT',12)
            state['cloud']=False
            assert client.wait_for_result(rospy.Duration(5))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'Stale cloud' in client.get_result().message,str(client.get_result())
            assert obstacle(False).success
            state['cloud']=True
            wait_until(lambda: state['gate']=='IDLE',3)
            time.sleep(1.3)
            assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            print('PASS: input fault during blocked wait aborts and cannot auto-resume',flush=True)

            assert obstacle(True).success
            send(state['x']-.6,state['y'])
            wait_until(lambda: state['task']=='BLOCKED_WAIT',12)
            old_task=state['targets'][-1].task_id
            assert obstacle(False).success
            send(state['x']+.4,state['y'])
            assert client.wait_for_result(rospy.Duration(30))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['targets'][-1].task_id!=old_task
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('PASS: new goal during blocked wait replaces old goal; old retries cannot return',flush=True)
            print('ALL LOCAL-ONLY RETRY TESTS PASSED (private master; no physical robot commands)',flush=True)
            return

        if os.environ.get('SCAN_NAV_SCENARIO')=='localization':
            assert rospy.get_param('/scan_velocity_gate/localization_timeout')==1.2
            assert rospy.get_param('/scan_navigator/localization_timeout')==1.2
            assert rospy.get_param('/scan_global/global_costmap/inflation_layer/inflation_radius')==.30
            def stopped():
                return abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            def moving():
                return math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>.02
            def recovering():
                return state['task'].startswith('LOCALIZATION_RECOVERY')
            # Between the old and new thresholds: still valid at 0.9 s old.
            state['ndt_age']=.9
            epoch_before=state['epoch']
            send(-.6,0)
            assert client.wait_for_result(rospy.Duration(30))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['epoch']==epoch_before
            state['ndt_age']=0
            print('PASS: 0.9-second-old NDT accepted by 1.2-second limit; other inputs stay fresh',flush=True)

            # Drop NDT + map TF, NOT odometry or point clouds. Keep the user
            # action active, but old task/epoch/trajectories must never resume.
            send(state['x']-.8,state['y'])
            wait_until(moving,15)
            old_task=state['targets'][-1].task_id
            state['ndt_publish']=state['localization_tf']=False
            wait_until(recovering,4)
            wait_until(stopped,1)
            until=time.monotonic()+.25
            while time.monotonic()<until:
                assert stopped()
                assert client.get_state()==GoalStatus.ACTIVE
                time.sleep(.02)
            state['ndt_publish']=state['localization_tf']=True
            assert client.wait_for_result(rospy.Duration(35))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['targets'][-1].task_id!=old_task
            assert any(s.startswith('LOCALIZATION_RECOVERY 1/3') for s in state['history'])
            print('PASS: localization timeout stops; fresh NDT/TF replans SAME action goal with NEW internal task',flush=True)

            # TF-only staleness must also pause safely, not bypass the timeout.
            send(state['x']+.6,state['y'])
            wait_until(moving,15)
            old_task=state['targets'][-1].task_id
            state['localization_tf']=False
            wait_until(recovering,4); wait_until(stopped,1)
            state['localization_tf']=True
            assert client.wait_for_result(rospy.Duration(30))
            assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
            assert state['targets'][-1].task_id!=old_task
            print('PASS: TF-only localization delay also stops and generates a fresh retry task',flush=True)

            send(state['x']+.6,state['y'])
            wait_until(moving,15)
            state['ndt_publish']=False
            wait_until(recovering,4); wait_until(stopped,1)
            client.cancel_goal()
            assert client.wait_for_result(rospy.Duration(5))
            assert client.get_state()==GoalStatus.PREEMPTED
            state['ndt_publish']=True
            wait_until(lambda: state['gate']=='IDLE',3)
            time.sleep(.3); assert stopped()
            print('PASS: cancel during NDT recovery prevents all later retries',flush=True)

            send(state['x']+.6,state['y'])
            wait_until(moving,15)
            state['ndt_publish']=False
            wait_until(recovering,4)
            state['ndt']=False; state['ndt_publish']=True
            assert client.wait_for_result(rospy.Duration(5))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'NDT quality' in client.get_result().message,str(client.get_result())
            state['ndt']=True
            wait_until(lambda: state['gate']=='IDLE',3)
            time.sleep(.2); assert stopped()
            print('PASS: poor localization quality during retry immediately aborts, never auto-resumes',flush=True)

            send(state['x']+.6,state['y'])
            wait_until(moving,15)
            state['ndt_publish']=state['localization_tf']=False
            wait_until(recovering,4)
            state['tf_offset']+=1.0
            state['ndt_publish']=state['localization_tf']=True
            assert client.wait_for_result(rospy.Duration(5))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'localization jump' in client.get_result().message,str(client.get_result())
            state['tf_offset']=0
            time.sleep(.3); assert stopped()
            print('PASS: localization jump after dropout cannot be hidden by reinitializing a retry',flush=True)

            wait_until(lambda: state['gate']=='IDLE',3)
            send(state['x']+.6,state['y'])
            wait_until(moving,15)
            state['ndt_publish']=False
            wait_until(recovering,4)
            assert client.wait_for_result(rospy.Duration(13))
            assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
            assert 'exhausted (3 retries)' in client.get_result().message,str(client.get_result())
            for i in (1,2,3):
                assert any(s.startswith('LOCALIZATION_RECOVERY %d/3'%i) for s in state['history'])
            state['ndt_publish']=True
            wait_until(lambda: state['gate']=='IDLE',3)
            time.sleep(.3); assert stopped()
            assert '/ros2qnx' not in str(master.getSystemState('/test'))
            print('ALL LOCALIZATION RETRY TESTS PASSED (private master; no physical robot commands)',flush=True)
            return
        send(0.6,0)
        assert client.wait_for_result(rospy.Duration(35)), 'SCAN task timed out'
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        assert state['motion']
        print('PASS: real SCAN planning + B-spline tracking reaches any-yaw goal',flush=True)
        send(state['x'],state['y'],0.5,True)
        assert client.wait_for_result(rospy.Duration(15))
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        assert abs(state['yaw']-0.5)<0.15
        print('PASS: fixed final yaw alignment',flush=True)
        send(3.0,0)
        assert client.wait_for_result(rospy.Duration(75)), 'Long detour timed out'
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        print('PASS: nonidentity map/odom transform and long SCAN detour with replanning',flush=True)

        # Correct ONLY map->odom during execution. Odom and local cloud stay
        # continuous; the map goal must acquire a corrected odom target WITHOUT
        # the previous stop/stabilize/global-reset cycle.
        routes_before = len(state['routes'])
        targets_before = len(state['targets'])
        send(3.8,0)
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        state['tf_offset'] = 0.2
        assert client.wait_for_result(rospy.Duration(40))
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        assert 'WAITING_FOR_LOCALIZATION' not in state['history']
        assert 'REPLANNING' not in state['history'], str(state['history'])
        assert len(state['routes']) == routes_before+1
        targets = state['targets'][targets_before:]
        assert len(targets) >= 2
        assert len({m.task_id for m in targets}) == 1
        assert math.hypot(state['x']+state['tf_offset']-3.8,state['y']) < 0.17
        assert state['routes'][-1].header.frame_id == 'map'
        print('PASS: continuous odom + independent NDT correction updates targets without global reset',flush=True)

        send(3.0,0)
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        state['tf_offset'] += 1.0
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.ABORTED, str(client.get_result())
        assert 'localization jump' in client.get_result().message, str(client.get_result())
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6,1)
        state['tf_offset'] = 0
        time.sleep(1)
        print('PASS: large localization discontinuity stops instead of chasing a shifted target',flush=True)

        send(state['x']-0.8,state['y'])
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        old_task = state['targets'][-1].task_id
        send(state['x']-0.25,state['y']+0.2)
        assert client.wait_for_result(rospy.Duration(30))
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        assert state['targets'][-1].task_id != old_task
        print('PASS: replacing an executing goal switches task identity and reaches the replacement',flush=True)

        # Force candidate rejection (test-only hook). Production has no hook.
        # Keep REPORTED body velocity nonzero while holding output at zero to
        # prove recovery attempts do not wait for a standstill confirmation.
        routes_before = len(state['routes'])
        send(state['x']-0.6,state['y'])
        wait_until(lambda: math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>0.05,15)
        epoch_before = state['epoch']
        task_before = state['targets'][-1].task_id
        generation_before = state['trajectories'][-1].generation
        state['reported_speed'] = 0.2
        assert obstacle(True).success
        wait_until(lambda: state['task']=='LOCAL_RECOVERY',2)
        wait_until(lambda: state['planner'].recovery_attempts >= 1,2)
        assert state['planner'].state == PlannerState.RECOVERING
        target_count = len(state['targets'])
        until = time.monotonic()+0.25
        while time.monotonic()<until:
            assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            assert state['epoch']==epoch_before
            time.sleep(0.02)
        assert len(state['targets'])==target_count
        # Allow a valid candidate while measured speed is STILL > 0.1 m/s.
        assert obstacle(False).success
        wait_until(lambda: state['planner'].state==PlannerState.TRACKING,2)
        assert state['reported_speed']==0.2
        state['reported_speed']=None
        assert client.wait_for_result(rospy.Duration(30))
        assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
        assert state['epoch']==epoch_before
        assert len(state['routes'])==routes_before+1
        assert state['targets'][-1].task_id==task_before
        assert any(m.task_id==task_before and m.generation>generation_before for m in state['trajectories'])
        print('PASS: emergency stops output, plans with nonzero measured velocity, resumes SAME task on checked new generation',flush=True)

        send(state['x']+0.6,state['y'])
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        assert obstacle(True).success
        wait_until(lambda: state['task']=='LOCAL_RECOVERY',2)
        client.cancel_goal()
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.PREEMPTED
        assert obstacle(False).success
        time.sleep(0.5)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: cancellation during local recovery cannot resume the task',flush=True)

        persistent_local_retry(.5)

        # Pause ONLY the computation loop: callbacks and independent lease
        # renewal keep running. A live renewal worker must not mask this fault.
        routes_before = len(state['routes'])
        send(state['x']+0.6,state['y'])
        wait_until(lambda: math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>0.04,15)
        epoch_before = state['epoch']
        task_before = state['targets'][-1].task_id
        generation_before = state['trajectories'][-1].generation
        assert stall(True).success
        wait_until(lambda: state['gate'].startswith('LEASE_RECOVERY'),2)
        until = time.monotonic()+0.25
        while time.monotonic()<until:
            assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
            assert state['epoch']==epoch_before
            time.sleep(0.02)
        assert stall(False).success
        assert client.wait_for_result(rospy.Duration(30))
        assert client.get_state()==GoalStatus.SUCCEEDED,str(client.get_result())
        assert 'LEASE_RECOVERY' in state['history']
        assert state['epoch']==epoch_before
        assert len(state['routes'])==routes_before+1
        assert state['targets'][-1].task_id==task_before
        assert any(m.task_id==task_before and m.generation>generation_before for m in state['trajectories'])
        print('PASS: stalled computation defeats live renewal worker, stops output, then resets and resumes SAME task/new trajectory',flush=True)

        send(state['x']-0.6,state['y'])
        wait_until(lambda: math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>0.04,15)
        epoch_before = state['epoch']
        assert stall(True).success
        wait_until(lambda: state['gate'].startswith('LEASE_RECOVERY'),2)
        wait_until(lambda: state['epoch']>epoch_before,4)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
        assert stall(False).success
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
        assert 'lease recovery timed out' in client.get_result().message,str(client.get_result())
        time.sleep(0.5)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: persistent computation stall revokes task after recovery window; delayed renewal cannot resume it',flush=True)

        wait_until(lambda: state['gate']=='IDLE',3)
        send(state['x']-0.6,state['y'])
        wait_until(lambda: math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>0.04,15)
        assert stall(True).success
        wait_until(lambda: state['gate'].startswith('LEASE_RECOVERY'),2)
        client.cancel_goal()
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.PREEMPTED
        assert stall(False).success
        time.sleep(0.5)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: cancel during lease recovery immediately stops and cannot be undone by renewal',flush=True)

        send(state['x']-0.6,state['y'])
        wait_until(lambda: math.hypot(state['cmd'].linear.x,state['cmd'].linear.y)>0.04,15)
        epoch_before = state['epoch']
        assert stall(True).success
        wait_until(lambda: state['gate'].startswith('LEASE_RECOVERY'),2)
        state['ndt'] = False
        wait_until(lambda: state['epoch']>epoch_before,1.5)
        assert stall(False).success
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.ABORTED,str(client.get_result())
        state['ndt'] = True
        wait_until(lambda: state['gate']=='IDLE',3)
        time.sleep(0.3)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: NDT fault during lease recovery overrides soft recovery and never resumes the old goal',flush=True)

        send(state['x']+0.6,state['y'])
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        client.cancel_goal()
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.PREEMPTED
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].linear.y)+abs(state['cmd'].angular.z)<1e-6,1)
        time.sleep(0.5)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: cancellation clears motion and old trajectory',flush=True)
        send(state['x']+0.6,state['y'])
        wait_until(lambda: abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)>0.01,15)
        assert obstacle(True).success
        wait_until(lambda: state['task']=='LOCAL_RECOVERY',2)
        state['cloud']=False
        wait_until(lambda: 'Stale cloud' in state['gate'],2)
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.ABORTED
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
        assert obstacle(False).success
        state['cloud']=True
        wait_until(lambda: state['gate'] in ('READY','IDLE'),3)
        time.sleep(0.5)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
        # A new goal works after recovery without any manual unlock.
        send(state['x']+0.3,state['y'])
        assert client.wait_for_result(rospy.Duration(20))
        assert client.get_state()==GoalStatus.SUCCEEDED, str(client.get_result())
        state['ndt']=False
        wait_until(lambda: 'NDT quality' in state['gate'],3)
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
        print('PASS: faults stop motion; recovery automatically permits new goals, not old commands',flush=True)
        assert launch.poll() is None, 'Navigation process exited unexpectedly'
        assert '/ros2qnx' not in str(master.getSystemState('/test'))
        print('ALL ISOLATED TESTS PASSED (no physical robot commands)',flush=True)
    finally:
        done.set()
        for proc in reversed(processes):
            if proc.poll() is None:
                os.killpg(proc.pid,signal.SIGINT)
        for proc in reversed(processes):
            try:
                proc.wait(timeout=8)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid,signal.SIGTERM)
                proc.wait(timeout=5)
        for stream in streams:
            stream.close()


if __name__=='__main__':
    main()
