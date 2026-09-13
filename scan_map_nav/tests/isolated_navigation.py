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
        from scan_map_navigation.msg import NavigateAction,NavigateGoal,LocalTarget
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
                 'tf_offset':0.0,'wobble':False,'task':'','history':[],'routes':[],'targets':[]}
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
        rospy.Subscriber('/scan_map_nav/local_target',LocalTarget,
                         lambda m: state['targets'].append(m),queue_size=10)
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
        grid.header.stamp=rospy.Time.now()
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
                odom.twist.twist=cmd
                odom_pub.publish(odom)
                imu=Imu()
                imu.header=odom.header
                imu.header.frame_id='base_link'
                imu.orientation.w=1
                imu.linear_acceleration.z=9.81
                imu_pub.publish(imu)
                if tick%5==0:
                    ndt=ScanMatchingStatus()
                    ndt.header=Header(stamp=stamp,frame_id='rslidar')
                    ndt.has_converged=state['ndt']
                    ndt.matching_error=0.01
                    ndt.inlier_fraction=0.9
                    ndt_pub.publish(ndt)
                    if state['cloud']:
                        points=[(3.5*math.cos(a*math.pi/90),3.5*math.sin(a*math.pi/90),0.0) for a in range(180)]
                        cy,sy=math.cos(state['yaw']),math.sin(state['yaw'])
                        cp,sp=math.cos(math.pi/10),math.sin(math.pi/10)
                        # Return points from the static wall in the MID360 frame.
                        for j in range(35):
                            dx,dy=1.55-state['x'],-0.75+j*0.05-state['y']
                            bx=cy*dx+sy*dy-0.187
                            by=-sy*dx+cy*dy
                            bz=0.3-0.327-0.073
                            points.append((cp*bx-sp*bz,by,sp*bx+cp*bz))
                        cloud_pub.publish(point_cloud2.create_cloud_xyz32(Header(stamp=stamp,frame_id='rslidar'),points))
                tick+=1
                time.sleep(0.02)
        threading.Thread(target=sensors,daemon=True).start()
        launch=start(['roslaunch','scan_map_navigation','navigation.launch','localization:=false',
                      'rviz:=false','output_topic:=/test/cmd_vel'],'navigation')
        rospy.wait_for_service('/scan_global/make_plan',timeout=60)
        rospy.wait_for_service('/scan_local/check_poses',timeout=60)
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
        state['cloud']=False
        wait_until(lambda: 'Stale cloud' in state['gate'],2)
        assert client.wait_for_result(rospy.Duration(5))
        assert client.get_state()==GoalStatus.ABORTED
        assert abs(state['cmd'].linear.x)+abs(state['cmd'].angular.z)<1e-6
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
