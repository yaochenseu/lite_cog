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
from scan_map_navigation.msg import VelocityCommand, NavigationControl, PlannerState, LeaseRecovery
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
        g.previous_fault_reason = ''
        g.lease_hold = None
        g.lease_hold_ack = False
        g.lease_hold_started = 0
        g.recovery_id = 0
        g.lease_recovery_timeout = 2.0
        g.lease_request = Mock()
        g.last_fault = Mock()
        g.conflict = ''
        g.timeout = 0.7
        g.localization_timeout = 1.2
        g.min_inliers,g.max_error = 0.5,0.3
        g.command = VelocityCommand(epoch=0)
        g.control = NavigationControl(epoch=0,task_id=1,mode=NavigationControl.TRACK)
        g.control.header.frame_id = 'odom'
        g.control.header.stamp = rospy.Time.from_sec(100)
        g.control_time = time.monotonic()
        g.command_time = time.monotonic()
        g.vx,g.vy,g.wz,g.reverse = 0.35,0.25,0.8,0.18
        g.output = Mock()
        g.allowed = Mock()
        g.epoch_pub = Mock()
        cloud=PointCloud2()
        cloud.width=cloud.height=1
        cloud.fields=[PointField(name=n,datatype=7,count=1) for n in ('x','y','z')]
        odom=Odometry()
        odom.header.frame_id='odom'
        odom.child_frame_id='base_link'
        odom.pose.pose.orientation.w=1
        ndt=ScanMatchingStatus(has_converged=True,matching_error=0.01,inlier_fraction=0.9)
        execution=PlannerState(task_id=1,epoch=0,generation=0,state=PlannerState.TRACKING)
        execution.header.frame_id='odom'
        g.inputs={}
        for key,m in (('cloud',cloud),('odom',odom),('imu',Imu()),('ndt',ndt),('planner',Bool(True)),('execution',execution)):
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

    def test_static_navigation_needs_no_runtime_grid(self):
        self.assertNotIn('map',self.g.inputs)
        self.assertEqual(self.g.healthy(),'')
        # Unused historical runtime-grid data must not revoke a static task.
        self.g.inputs['map']=(Mock(),time.monotonic()-100)
        self.assertEqual(self.g.healthy(),'')

    def test_sensor_freshness_still_required_without_runtime_grid(self):
        for key in ('cloud','odom','imu','ndt','execution'):
            msg,received=self.g.inputs[key]
            self.g.inputs[key]=(msg,time.monotonic()-1.3)
            self.assertEqual(self.g.healthy(),'Stale '+key)
            self.g.inputs[key]=(msg,received)

    def test_ndt_invalid(self):
        self.g.inputs['ndt'][0].matching_error=float('nan')
        self.assertIn('NDT quality',self.g.healthy())

    def test_ndt_one_second_old_allowed_but_other_inputs_not_relaxed(self):
        self.g.inputs['ndt'][0].header.stamp=rospy.Time.from_sec(99)
        self.assertEqual(self.g.healthy(),'')
        self.g.inputs['cloud'][0].header.stamp=rospy.Time.from_sec(99)
        self.assertEqual(self.g.healthy(),'Stale cloud')

    def test_ndt_age_over_new_limit_and_bad_stamp(self):
        status=self.g.inputs['ndt'][0]
        status.header.stamp=rospy.Time.from_sec(98.7)
        self.assertEqual(self.g.healthy(),'Stale ndt')
        status.header.stamp=rospy.Time.from_sec(100.5)
        self.assertEqual(self.g.healthy(),'Invalid ndt timestamp')

    def test_bad_quality_or_other_fault_not_masked_by_stale_ndt(self):
        status=self.g.inputs['ndt'][0]
        status.header.stamp=rospy.Time.from_sec(98)
        status.has_converged=False
        self.assertEqual(self.g.healthy(),'NDT quality below threshold')
        status.has_converged=True
        self.g.inputs['cloud'][0].width=0
        self.assertEqual(self.g.healthy(),'Empty/invalid point cloud')

    def test_new_hard_fault_reported_while_already_stopped(self):
        self.g.refresh_health('')
        self.g.refresh_health('Stale ndt')
        self.g.refresh_health('NDT quality below threshold')
        self.assertEqual(self.g.last_fault.publish.call_args.args[0].data,'NDT quality below threshold')
        self.assertEqual(self.g.command_epoch,1)

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
        self.g.inputs['execution'][0].task_id = 2
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

    def test_expired_active_lease_stops_but_preserves_task_epoch(self):
        self.g.refresh_health('')
        self.g.control_time -= 0.6
        self.assertEqual(self.g.healthy(),'')
        self.g.refresh_health(self.g.healthy())
        self.assertEqual(self.g.command_epoch,0)
        self.assertIsNotNone(self.g.lease_hold)
        self.assertEqual(self.g.select_command(True)[2],'LEASE_RECOVERY: stopped, waiting for navigation reset')
        self.assertEqual(self.g.output.publish.call_args.args[0].linear.x,0)

    def start_hold(self):
        self.g.refresh_health('')
        self.g.control_time -= 0.6
        self.assertEqual(self.g.healthy(),'')
        self.g.control_time = time.monotonic()
        self.g.command = VelocityCommand(epoch=0)
        self.valid_command()
        return self.g.lease_hold

    def test_renewal_alone_cannot_release_old_trajectory(self):
        self.start_hold()
        self.assertEqual(self.g.healthy(),'')
        self.assertFalse(self.g.select_command(True)[1])
        # Even a newer planner generation is insufficient without a manager ACK.
        self.g.inputs['execution'][0].generation = 1
        self.assertEqual(self.g.healthy(),'')
        self.assertFalse(self.g.select_command(True)[1])

    def test_ack_requires_reset_and_fresh_new_generation_command(self):
        hold = self.start_hold()
        self.g.ack_recovery(hold)
        self.assertEqual(self.g.healthy(),'')
        self.assertIsNotNone(self.g.lease_hold)  # same generation: no reset proof
        self.g.inputs['execution'][0].generation = 1
        self.assertEqual(self.g.healthy(),'')
        self.assertIsNone(self.g.lease_hold)
        self.assertIsNone(self.g.command)
        self.g.command = VelocityCommand(epoch=0)
        self.valid_command()
        self.assertFalse(self.g.select_command(True)[1])
        self.g.command.generation = 1
        self.assertTrue(self.g.select_command(True)[1])

    def test_persistent_lease_hold_revokes_task(self):
        self.start_hold()
        self.g.lease_hold_started -= 2.1
        self.assertIn('recovery timed out',self.g.healthy())
        self.g.refresh_health(self.g.healthy())
        self.assertEqual(self.g.command_epoch,1)
        self.assertIsNone(self.g.lease_hold)

    def test_late_ack_cannot_extend_recovery_deadline(self):
        hold = self.start_hold()
        self.g.ack_recovery(hold)
        self.g.inputs['execution'][0].generation = 1
        self.g.lease_hold_started -= 2.1
        self.assertIn('recovery timed out',self.g.healthy())

    def test_sensor_fault_during_lease_hold_still_revokes_task(self):
        self.start_hold()
        self.g.inputs['ndt'][0].has_converged = False
        self.g.refresh_health(self.g.healthy())
        self.assertEqual(self.g.command_epoch,1)

    def test_cancellation_during_lease_hold_stays_stopped(self):
        self.start_hold()
        self.g.control.mode = NavigationControl.STOP
        self.g.lease_hold_started -= 3
        self.assertEqual(self.g.healthy(),'')
        self.assertFalse(self.g.select_command(True)[1])

    def test_previous_recovery_ack_cannot_release_new_hold(self):
        hold = self.start_hold()
        ack = LeaseRecovery(recovery_id=hold.recovery_id,task_id=2,epoch=0)
        ack.header.stamp = hold.header.stamp
        self.g.ack_recovery(ack)
        self.assertFalse(self.g.lease_hold_ack)

    def test_replacement_task_is_not_held_by_previous_request(self):
        self.start_hold()
        self.g.control.task_id = 2
        self.assertEqual(self.g.healthy(),'')
        self.assertIsNone(self.g.lease_hold)

    def test_delayed_track_lease_cannot_override_newer_stop(self):
        old = self.g.control
        stop = NavigationControl(epoch=0,task_id=1,mode=NavigationControl.STOP)
        stop.header.stamp = rospy.Time.from_sec(100.1)
        stop.header.frame_id = 'odom'
        self.g.lease(stop)
        self.g.lease(old)
        self.assertEqual(self.g.control.mode,NavigationControl.STOP)

    def test_emergency_holds_velocity_without_revoking_task(self):
        self.g.refresh_health('')
        self.g.command = VelocityCommand(epoch=0)
        self.valid_command()
        self.g.inputs['execution'][0].state = PlannerState.RECOVERING
        self.assertEqual(self.g.healthy(),'')
        self.assertTrue(self.g.refresh_health(self.g.healthy()))
        cmd,allowed,state = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(cmd.linear.x,0)
        self.assertTrue(state.startswith('LOCAL_RECOVERY'))
        self.assertEqual(self.g.command_epoch,0)

    def test_old_trajectory_cannot_resume_when_planner_recovers(self):
        self.valid_command()
        self.g.inputs['execution'][0].generation = 1
        _,allowed,_ = self.g.select_command(True)
        self.assertFalse(allowed)
        self.g.command.generation = 1
        self.assertTrue(self.g.select_command(True)[1])

    def test_new_trajectory_does_not_wait_for_standstill(self):
        self.valid_command()
        self.g.inputs['odom'][0].twist.twist.linear.x = 0.2
        self.assertEqual(self.g.healthy(),'')
        self.assertTrue(self.g.select_command(True)[1])

    def test_recovery_notification_immediately_sends_zero(self):
        status = PlannerState(task_id=1,state=PlannerState.RECOVERING,generation=1)
        status.header.stamp = rospy.Time.from_sec(100)
        self.g.receive(status,'execution')
        self.assertEqual(self.g.output.publish.call_args.args[0].linear.x,0)
        self.assertFalse(self.g.allowed.publish.call_args.args[0].data)

    def test_stale_execution_state_remains_a_real_fault(self):
        msg,_ = self.g.inputs['execution']
        self.g.inputs['execution'] = msg,time.monotonic()-1
        self.assertEqual(self.g.healthy(),'Stale execution')

    def test_blocked_is_not_permission_to_replay_old_commands(self):
        self.valid_command()
        self.g.inputs['execution'][0].state = PlannerState.BLOCKED
        self.assertEqual(self.g.healthy(),'')
        cmd,allowed,state = self.g.select_command(True)
        self.assertFalse(allowed)
        self.assertEqual(cmd.linear.x,0)
        self.assertTrue(state.startswith('LOCAL_BLOCKED'))


if __name__=='__main__':
    unittest.main()
