#!/usr/bin/python3
"""Actual runtime fusion + Dijkstra on a private master; no robot controller."""
import copy
import math
import os
import pathlib
import signal
import socket
import subprocess
import tempfile
import threading
import time
import xmlrpc.client
from synthetic_lidar import scan
from isolated_navigation import wait_until


def main():
    logs=tempfile.mkdtemp(prefix='scan_runtime_map_test_')
    print('Runtime map integration logs: '+logs,flush=True)
    with socket.socket() as s:
        s.bind(('127.0.0.1',0)); port=s.getsockname()[1]
    assert port!=11311
    os.environ.update(ROS_MASTER_URI='http://127.0.0.1:'+str(port),ROS_IP='127.0.0.1',
                      ROS_HOSTNAME='localhost',ROS_HOME=logs,ROS_LOG_DIR=logs)
    processes=[]; streams=[]; done=threading.Event()
    def start(cmd,name):
        stream=open(os.path.join(logs,name+'.log'),'w'); streams.append(stream)
        p=subprocess.Popen(cmd,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        processes.append(p); return p
    try:
        start(['roscore','-p',str(port)],'master')
        master=xmlrpc.client.ServerProxy(os.environ['ROS_MASTER_URI'])
        wait_until(lambda: master.getPid('/test')[0]==1)
        import rospy
        import tf
        from std_msgs.msg import Header
        from nav_msgs.msg import OccupancyGrid
        from nav_msgs.srv import GetPlan
        from geometry_msgs.msg import PoseStamped
        from sensor_msgs.msg import PointCloud2
        from sensor_msgs import point_cloud2
        from hdl_localization.msg import ScanMatchingStatus
        from scan_map_navigation.msg import PlanningGrid
        rospy.init_node('runtime_map_test',disable_signals=True)
        prior_pub=rospy.Publisher('/map',OccupancyGrid,queue_size=1,latch=True)
        cloud_pub=rospy.Publisher('/rslidar_points',PointCloud2,queue_size=1)
        ndt_pub=rospy.Publisher('/status',ScanMatchingStatus,queue_size=1)
        broadcaster=tf.TransformBroadcaster()
        prior=OccupancyGrid()
        prior.header.frame_id='map'
        prior.info.width=prior.info.height=100; prior.info.resolution=.1
        prior.info.origin.position.x=prior.info.origin.position.y=-5
        prior.info.origin.orientation.w=1
        prior.data=[0]*10000
        def index(x,y): return math.floor((y+5)/.1)*100+math.floor((x+5)/.1)
        for y in range(100):
            for x in range(100):
                if x in (0,99) or y in (0,99) or (60<=x<=62 and 47<=y<=52) or (x==80 and 30<=y<=69):
                    prior.data[y*100+x]=100
        original=copy.deepcopy(prior.data)
        prior_pub.publish(prior)
        wall=((3,-2,0),(3.1,2,1.2))
        old_box=((1,-.3,0),(1.3,.3,.65))
        new_box=((1.6,-.25,0),(1.9,.25,.65))
        state=dict(boxes=[wall,old_box],cloud=True,ndt=True,tf=True,tf_delay=0.,map=None,fault=None)
        observations=[]; cloud_stamps=set()
        def on_map(msg):
            state['map']=msg
            observations.append((time.monotonic(),msg.header.stamp.to_nsec(),
                                 (rospy.Time.now()-msg.header.stamp).to_sec(),msg.valid))
        rospy.Subscriber('/scan_map_nav/planning_grid',PlanningGrid,on_map,queue_size=1)
        def sensors():
            tick=0
            try:
                while not done.is_set():
                    stamp=rospy.Time.now()
                    if state['tf']:
                        # NDT map->odom is deliberately late; body/lidar TF is
                        # current. No latest-TF fallback is permitted by the test.
                        map_stamp=stamp-rospy.Duration(state['tf_delay'])
                        broadcaster.sendTransform((0,0,0),(0,0,0,1),map_stamp,'odom','map')
                        broadcaster.sendTransform((0,0,.327),(0,0,0,1),stamp,'base_link','odom')
                        broadcaster.sendTransform((.187,0,.073),tf.transformations.quaternion_from_euler(0,math.pi/10,0),
                                                  stamp,'rslidar','base_link')
                    if tick%5==0:
                        status=ScanMatchingStatus(has_converged=state['ndt'],matching_error=.01,inlier_fraction=.9)
                        status.header=Header(stamp=stamp,frame_id='rslidar'); ndt_pub.publish(status)
                        if state['cloud']:
                            points=scan(0,0,0,state['boxes'])
                            cloud_stamps.add(stamp.to_nsec())
                            cloud_pub.publish(point_cloud2.create_cloud_xyz32(Header(stamp=stamp,frame_id='rslidar'),points))
                    tick+=1; time.sleep(.02)
            except Exception as exc:
                state['fault']=exc
        threading.Thread(target=sensors,daemon=True).start()
        root=pathlib.Path(__file__).resolve().parents[1]
        subprocess.check_call(['rosparam','load',str(root/'src/scan_map_navigation/config/global.yaml'),'/scan_global'])
        start(['rosrun','scan_map_navigation','runtime_map','__name:=scan_runtime_map'],'runtime')
        start(['rosrun','scan_map_navigation','map_global_planner','__name:=scan_global'],'global')
        wait_until(lambda: state['map'] is not None and state['map'].valid,30)
        rospy.wait_for_service('/scan_global/make_plan',timeout=10)
        plan=rospy.ServiceProxy('/scan_global/make_plan',GetPlan)
        def pose(x,y):
            p=PoseStamped(); p.header.frame_id='map'; p.pose.position.x=x; p.pose.position.y=y
            p.pose.orientation.w=1; return p
        def path(): return plan(pose(0,0),pose(2.4,0),0).plan
        before=path()
        assert max(abs(p.pose.position.y) for p in before.poses)>.55
        old=index(1.15,.05); halo=index(1.45,.05)
        added_cells=[index(1.55,.05),index(1.65,.05)] # observed front surface, not occluded box interior
        assert state['map'].occupancy[old]==100
        assert state['map'].costs[halo]>0
        print('PASS: actual Dijkstra detours around old prior obstacle',flush=True)
        state['boxes']=[wall]
        wait_until(lambda: state['map'].occupancy[old]==0 and state['map'].costs[halo]==0,15)
        after=path()
        assert max(abs(p.pose.position.y) for p in after.poses)<.3
        assert prior.data==original
        print('PASS: positive multi-height free rays remove old obstacle AND halo; Dijkstra reopens passage; prior unchanged',flush=True)
        state['boxes']=[wall,new_box]
        wait_until(lambda: any(state['map'].occupancy[k]==100 for k in added_cells),5)
        added=next(k for k in added_cells if state['map'].occupancy[k]==100)
        assert state['map'].topology[added]==0
        reroute=path()
        assert max(abs(p.pose.position.y) for p in reroute.poses)>.45
        print('PASS: new lidar-only obstacle changes actual Dijkstra route without modifying prior topology',flush=True)
        # Reproduce real NDT latency (> the former 50ms callback wait). The
        # queue must retain clouds while newer, not-yet-transformable ones arrive.
        for delay in (.18,.30):
            state['tf_delay']=delay
            time.sleep(1.2) # finish transition from the previous TF history
            begin=time.monotonic(); first=len(observations)
            while time.monotonic()-begin<4:
                current=state['map']
                assert current.valid and (rospy.Time.now()-current.header.stamp).to_sec()<.7, \
                    'Delayed TF starved the runtime map (delay %.2fs)'%delay
                time.sleep(.02)
            rows=observations[first:]
            assert len(rows)>=10,('Insufficient delayed-TF updates',delay,len(rows))
            assert all(valid and delay-.03<=age<.7 and stamp in cloud_stamps
                       for _,stamp,age,valid in rows),rows
            assert all(b[1]>a[1] for a,b in zip(rows,rows[1:])), 'Replayed/duplicate map evidence'
            gaps=[b[0]-a[0] for a,b in zip(rows,rows[1:])]
            assert max(gaps)<.6,gaps
            assert path().poses,'Dijkstra unavailable under bounded TF delay'
            print('PASS: %.0fms late NDT TF: %d updates/4s, max gap %.3fs; exact source stamps, fresh map and Dijkstra'%(
                  delay*1000,len(rows),max(gaps)),flush=True)
        # A TF arriving beyond the original freshness limit cannot rejuvenate
        # expired queued observations, even with healthy current lidar/NDT.
        state['tf_delay']=.95
        time.sleep(1.5)
        frozen=state['map']
        time.sleep(.5)
        assert state['map'].header.stamp==frozen.header.stamp
        assert (rospy.Time.now()-state['map'].header.stamp).to_sec()>.7
        try:
            path()
            raise AssertionError('Planner accepted TF/clouds beyond freshness budget')
        except rospy.ServiceException:
            pass
        state['tf_delay']=0.
        wait_until(lambda: state['map'].valid and
                   (rospy.Time.now()-state['map'].header.stamp).to_sec()<.4,5)
        print('PASS: over-budget TF expires queued clouds; recovery selects fresh data, not old backlog',flush=True)
        # The old new-box region is now occluded by a nearer wider object.
        state['boxes']=[wall,((.7,-.7,0),(1,.7,.9))]
        time.sleep(2)
        assert state['map'].occupancy[added]==100
        print('PASS: occluded obstacle is not erased by missing returns',flush=True)
        state['cloud']=False
        time.sleep(1)
        frozen=state['map']
        time.sleep(1)
        assert state['map'].revision==frozen.revision and state['map'].occupancy[added]==100
        try:
            path()
            raise AssertionError('Planner accepted stale sensor-derived map')
        except rospy.ServiceException:
            pass
        print('PASS: lidar dropout never becomes free space; planner rejects stale map',flush=True)
        # Fresh clouds without their timestamped TF must not be projected with
        # an old/latest transform or used to erase the occluded obstacle.
        state['tf']=False; state['cloud']=True
        time.sleep(1.2)
        frozen=state['map']
        time.sleep(.8)
        assert state['map'].revision==frozen.revision and state['map'].occupancy[added]==100
        assert (rospy.Time.now()-state['map'].header.stamp).to_sec()>.7
        try:
            path()
            raise AssertionError('Planner accepted clouds without timestamped TF')
        except rospy.ServiceException:
            pass
        print('PASS: missing timestamped TF adds no evidence; stale map rejects planning',flush=True)
        state['tf']=True
        wait_until(lambda: state['map'].valid and
                   (rospy.Time.now()-state['map'].header.stamp).to_sec()<.5,5)
        state['ndt']=False
        wait_until(lambda: not state['map'].valid,3)
        assert state['map'].occupancy[added]==100
        print('PASS: unreliable NDT rejects map updates without clearing evidence',flush=True)
        assert state['fault'] is None,state['fault']
        assert '/ros2qnx' not in str(master.getSystemState('/test'))
        print('ALL RUNTIME MAP INTEGRATION TESTS PASSED (no robot controllers)',flush=True)
    finally:
        done.set()
        for p in reversed(processes):
            if p.poll() is None: os.killpg(p.pid,signal.SIGINT)
        for p in reversed(processes):
            try: p.wait(timeout=8)
            except subprocess.TimeoutExpired:
                os.killpg(p.pid,signal.SIGTERM); p.wait(timeout=5)
        for stream in streams: stream.close()


if __name__=='__main__': main()
