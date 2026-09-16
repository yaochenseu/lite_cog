"""Localization-only retry budget, fresh-data proof and hard-fault vetoes."""
import pathlib
import sys
import time
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import Mock, patch
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src/scan_map_navigation/scripts'))
import rospy
from geometry_msgs.msg import PoseStamped
from hdl_localization.msg import ScanMatchingStatus
from std_msgs.msg import String
from navigator import Navigator, LocalizationTimeout, TaskCancelled


class LocalizationRetryTests(unittest.TestCase):
    def setUp(self):
        self.clock=patch('rospy.Time.now',return_value=rospy.Time.from_sec(100))
        self.clock.start(); self.addCleanup(self.clock.stop)
        self.shutdown=patch('rospy.is_shutdown',return_value=False)
        self.shutdown.start(); self.addCleanup(self.shutdown.stop)
        n=self.nav=Navigator.__new__(Navigator)
        n.stop,n.clear_scan,n.state,n.server=Mock(),Mock(),Mock(),Mock()
        n.target_marker=Mock()
        n.server.is_preempt_requested.return_value=False
        n.server.is_active.return_value=True
        n.hard_fault_serial=n.hard_fault_baseline=0
        n.hard_fault_reason=''
        n.last_fault=''; n.localization_anchor=None; n.last_remaining=2.
        n.task_timeout=30.; n.localization_retries=3
        n.localization_retry_wait=.02; n.localization_timeout=1.2
        n.jump_distance=.8; n.jump_yaw=.5
        n.ready=True; n.ready_time=time.monotonic()
        n.ndt_min_inliers=.5; n.ndt_max_error=.3
        status=ScanMatchingStatus(has_converged=True,matching_error=.02,inlier_fraction=.9)
        status.header.stamp=rospy.Time.from_sec(100.1)
        n.on_ndt(status)

    def test_retry_same_goal_new_attempt_without_resetting_deadline(self):
        n=self.nav; request=object()
        n.execute_attempt=Mock(side_effect=[LocalizationTimeout('Stale ndt'),None])
        n.wait_localization=Mock(return_value=True)
        n.execute(request)
        self.assertEqual(n.execute_attempt.call_count,2)
        calls=n.execute_attempt.call_args_list
        self.assertEqual(calls[0].args,calls[1].args)
        self.assertIs(calls[1].args[0],request)
        n.server.set_aborted.assert_not_called()
        self.assertGreaterEqual(n.clear_scan.call_count,2)
        n.target_marker.publish.assert_called_once()
        self.assertEqual(n.target_marker.publish.call_args.args[0].action,2)  # Marker.DELETE

    def test_continuous_outage_has_only_three_wait_windows(self):
        n=self.nav
        n.execute_attempt=Mock(side_effect=LocalizationTimeout('Stale ndt'))
        n.wait_localization=Mock(return_value=False)
        n.execute(object())
        self.assertEqual(n.execute_attempt.call_count,1)
        self.assertEqual(n.wait_localization.call_count,3)
        self.assertIn('exhausted (3 retries)',n.server.set_aborted.call_args.args[0].message)

    def test_budget_shared_across_repeated_successful_recoveries(self):
        n=self.nav
        n.execute_attempt=Mock(side_effect=LocalizationTimeout('Stale ndt'))
        n.wait_localization=Mock(return_value=True)
        n.execute(object())
        self.assertEqual(n.execute_attempt.call_count,4)
        self.assertEqual(n.wait_localization.call_count,3)
        n.server.set_aborted.assert_called_once()

    def test_other_fault_not_retried(self):
        n=self.nav
        n.execute_attempt=Mock(side_effect=RuntimeError('NDT quality below threshold'))
        n.wait_localization=Mock()
        n.execute(object())
        n.wait_localization.assert_not_called()
        n.server.set_aborted.assert_called_once()

    def test_cancel_during_wait_does_not_restart(self):
        n=self.nav
        n.execute_attempt=Mock(side_effect=LocalizationTimeout('Stale ndt'))
        n.wait_localization=Mock(side_effect=TaskCancelled())
        n.execute(object())
        n.server.set_preempted.assert_called_once()
        n.server.set_aborted.assert_not_called()
        self.assertEqual(n.execute_attempt.call_count,1)

    def test_old_tf_cannot_release_wait_even_if_gate_ready(self):
        n=self.nav; robot=PoseStamped(); robot.header.stamp=rospy.Time.from_sec(99.9)
        n.snapshot=Mock(return_value=(robot,(0,0,0),.327))
        self.assertFalse(n.wait_localization(time.monotonic()+1,rospy.Time.from_sec(100),'RECOVERY'))
        n.stop.assert_called()

    def test_new_fresh_tf_allows_replan_not_direct_motion(self):
        n=self.nav; robot=PoseStamped(); robot.header.stamp=rospy.Time.from_sec(100.1)
        n.snapshot=Mock(return_value=(robot,(0,0,0),.327))
        self.assertTrue(n.wait_localization(time.monotonic()+1,rospy.Time.from_sec(100),'RECOVERY'))
        n.stop.assert_called()

    def test_new_tf_with_old_ndt_does_not_release_wait(self):
        n=self.nav; robot=PoseStamped(); robot.header.stamp=rospy.Time.from_sec(100.1)
        n.snapshot=Mock(return_value=(robot,(0,0,0),.327))
        n.latest_ndt[0].header.stamp=rospy.Time.from_sec(99.9)
        self.assertFalse(n.wait_localization(time.monotonic()+1,rospy.Time.from_sec(100),'RECOVERY'))
        n.stop.assert_called()

    def test_new_ndt_must_be_fresh_and_good_quality(self):
        n=self.nav; after=rospy.Time.from_sec(100)
        self.assertTrue(n.recovered_ndt(after))
        n.latest_ndt[0].has_converged=False
        self.assertFalse(n.recovered_ndt(after))
        n.latest_ndt[0].has_converged=True
        n.latest_ndt=(n.latest_ndt[0],time.monotonic()-1.3)
        self.assertFalse(n.recovered_ndt(after))

    def test_hard_fault_veto_survives_later_ndt_timeout_report(self):
        n=self.nav
        n.on_fault(String('Stale cloud'))
        n.on_fault(String('Stale ndt'))
        with self.assertRaisesRegex(RuntimeError,'Non-retryable'):
            n.wait_localization(time.monotonic()+1,rospy.Time.from_sec(100),'RECOVERY')

    def test_jump_during_recovery_not_hidden_by_retry(self):
        n=self.nav; n.localization_anchor=(0,0,0)
        robot=PoseStamped(); robot.header.stamp=rospy.Time.from_sec(100.1)
        n.snapshot=Mock(return_value=(robot,(1,0,0),.327))
        with self.assertRaisesRegex(RuntimeError,'localization jump'):
            n.wait_localization(time.monotonic()+1,rospy.Time.from_sec(100),'RECOVERY')

    def test_tf_timeout_matches_ndt_not_other_sensor_timeout(self):
        n=self.nav; n.tf=Mock()
        n.tf.getLatestCommonTime.return_value=rospy.Time.from_sec(99)
        n.tf.lookupTransform.side_effect=[((0,0,0),(0,0,0,1)),((0,0,.3),(0,0,0,1))]
        n.snapshot()
        n.tf.getLatestCommonTime.return_value=rospy.Time.from_sec(98.7)
        with self.assertRaises(LocalizationTimeout): n.snapshot()
        n.tf.getLatestCommonTime.return_value=rospy.Time.from_sec(100.5)
        with self.assertRaisesRegex(RuntimeError,'Invalid localization TF'): n.snapshot()

    def test_launch_shares_localization_timeout_and_finite_retry_defaults(self):
        launch=ET.parse(str(ROOT/'src/scan_map_navigation/launch/navigation.launch')).getroot()
        self.assertEqual(launch.find("arg[@name='localization_timeout']").get('default'),'1.2')
        self.assertEqual(launch.find("arg[@name='localization_retries']").get('default'),'3')
        self.assertEqual(launch.find("arg[@name='localization_retry_wait']").get('default'),'3.0')
        for node,param in [('scan_navigator','localization_timeout'),('scan_velocity_gate','localization_timeout'),
                           ('scan_global','global_costmap/transform_tolerance')]:
            self.assertEqual(launch.find("node[@name='%s']/param[@name='%s']"%(node,param)).get('value'),
                             '$(arg localization_timeout)')


if __name__=='__main__': unittest.main()
