#!/usr/bin/python3
import pathlib
import io
import sys
import threading
import time
import unittest
from unittest.mock import patch, Mock
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
import rospy
from rospy.msg import serialize_message
from scan_map_navigation.msg import VelocityCommand, NavigationControl
from sensor_msgs.msg import PointCloud2,PointField,Imu
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool
from hdl_localization.msg import ScanMatchingStatus
from velocity_gate import Gate


class GateTests(unittest.TestCase):
    def setUp(self):
        self.clock = patch('rospy.Time.now',return_value=rospy.Time.from_sec(100))
        self.clock.start()
        self.addCleanup(self.clock.stop)
        g = self.g = Gate.__new__(Gate)
        g.lock = threading.RLock()
        g.was_healthy = False
        g.command_epoch = 0
        g.conflict = ''
        g.timeout = 0.7
        g.min_inliers,g.max_error = 0.5,0.3
        g.command = VelocityCommand(epoch=0)
        g.control = NavigationControl(epoch=0,task_id=1,mode=NavigationControl.TRACK)
        g.control.header.frame_id = 'odom'
        g.control.header.stamp = rospy.Time.from_sec(100)
        g.control_time = time.monotonic()
        g.command_time = time.monotonic()
        g.vx,g.vy,g.wz,g.reverse = 0.35,0.25,0.8,0.18
        g.output = Mock()
        g.epoch_pub = Mock()
        cloud=PointCloud2()
        cloud.width=cloud.height=1
        cloud.fields=[PointField(name=n,datatype=7,count=1) for n in ('x','y','z')]
        odom=Odometry()
        odom.header.frame_id='odom'
        odom.child_frame_id='base_link'
        odom.pose.pose.orientation.w=1
        ndt=ScanMatchingStatus(has_converged=True,matching_error=0.01,inlier_fraction=0.9)
        g.inputs={}
        for key,m in (('cloud',cloud),('odom',odom),('imu',Imu()),('ndt',ndt),('planner',Bool(True))):
            if hasattr(m,'header'):
                m.header.stamp=rospy.Time.from_sec(100)
            g.inputs[key]=(m,time.monotonic())

    def test_healthy_start_needs_no_unlock(self):
        self.assertEqual(self.g.healthy(),'')
        self.assertTrue(self.g.refresh_health(self.g.healthy()))
        self.assertTrue(self.g.was_healthy)
        self.assertIsNone(self.g.command)
        self.g.epoch_pub.publish.assert_not_called()

    def test_conflicting_publisher_prevents_motion(self):
        self.g.conflict='Other velocity publishers: /old_navigation'
        self.assertFalse(self.g.refresh_health(self.g.healthy()))
        self.assertFalse(self.g.was_healthy)

    def test_empty_cloud(self):
        self.g.inputs['cloud'][0].width=0
        self.assertIn('Empty',self.g.healthy())

    def test_stale_planner(self):
        m,_=self.g.inputs['planner']
        self.g.inputs['planner']=(m,time.monotonic()-1)
        self.assertIn('Stale planner',self.g.healthy())

    def test_ndt_invalid(self):
        self.g.inputs['ndt'][0].matching_error=float('nan')
        self.assertIn('NDT quality',self.g.healthy())

    def test_wrong_odom_frame(self):
        self.g.inputs['odom'][0].child_frame_id='wrong'
        self.assertIn('Invalid body odom',self.g.healthy())

    def test_fault_recovery_automatically_ready_but_rejects_old_task(self):
        self.g.refresh_health('')
        old = VelocityCommand(epoch=0)
        self.g.command = old
        self.assertFalse(self.g.refresh_health('Stale cloud'))
        self.assertIsNone(self.g.command)
        self.assertEqual(self.g.command_epoch,1)
        self.g.refresh_health('Stale cloud')
        self.g.epoch_pub.publish.assert_called_once()
        self.assertTrue(self.g.refresh_health(''))
        self.assertFalse(self.g.current_command(old))
        self.assertTrue(self.g.current_command(VelocityCommand(epoch=1)))

    def test_ros_serialization_preserves_task_epoch(self):
        wire = io.BytesIO()
        serialize_message(wire,99,VelocityCommand(epoch=7))
        restored = VelocityCommand().deserialize(wire.getvalue()[4:])
        self.assertEqual(restored.epoch,7)

    def valid_command(self):
        cmd = self.g.command
        cmd.task_id = 1
        cmd.mode = NavigationControl.TRACK
        cmd.command.header.frame_id = 'base_link'
        cmd.command.header.stamp = rospy.Time.from_sec(100)
        cmd.command.twist.linear.x = 0.3

    def test_direct_controller_command_and_limits(self):
        self.valid_command()
        self.g.command.command.twist.linear.x = 2
        cmd,allowed,state = self.g.select_command(True)
        self.assertTrue(allowed)
        self.assertEqual(state,'READY')
        self.assertEqual(cmd.linear.x,0.35)

    def test_cancel_blocks_fresh_old_command(self):
        self.valid_command()
        self.g.control.mode = NavigationControl.STOP
        cmd,allowed,_ = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(cmd.linear.x,0)

    def test_previous_task_cannot_move_replacement_task(self):
        self.valid_command()
        self.g.control.task_id = 2
        _,allowed,state = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(state,'WAITING_FOR_CONTROLLER')

    def test_old_tracking_command_cannot_leak_into_alignment(self):
        self.valid_command()
        self.g.control.mode = NavigationControl.ALIGN
        _,allowed,_ = self.g.select_command(True)
        self.assertFalse(allowed)

    def test_stale_command_explicitly_freezes_execution(self):
        self.valid_command()
        self.g.command_time -= 0.3
        cmd,allowed,state = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(cmd.linear.x,0)
        self.assertEqual(state,'Controller command expired')

    def test_stale_manager_lease_stops_execution(self):
        self.valid_command()
        self.g.control_time -= 0.6
        _,allowed,state = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(state,'Task lease invalid/expired')

    def test_expired_active_lease_revokes_task_epoch(self):
        self.g.refresh_health('')
        self.g.control_time -= 0.6
        self.assertEqual(self.g.healthy(),'Task lease expired')
        self.g.refresh_health(self.g.healthy())
        self.assertEqual(self.g.command_epoch,1)


if __name__=='__main__':
    unittest.main()
