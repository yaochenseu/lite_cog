"""Local blockage keeps the global route; retries cannot bypass STOP or faults."""
import pathlib
import sys
import unittest
from unittest.mock import Mock, patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src/scan_map_navigation/scripts'))
import rospy
from geometry_msgs.msg import PoseStamped
from scan_map_navigation.msg import NavigateGoal, NavigationControl, PlannerState
from navigator import Navigator, TaskCancelled, LocalizationTimeout
from rolling_route import OrderedRoute
from localization_guard import LocalizationJumpGuard


class LocalRetryTests(unittest.TestCase):
    def setUp(self):
        self.now = 10.
        def sleep(seconds): self.now += seconds
        for replacement in (patch('navigator.time.monotonic',side_effect=lambda: self.now),
                            patch('navigator.time.sleep',side_effect=sleep),
                            patch('rospy.Time.now',side_effect=lambda: rospy.Time.from_sec(100+self.now)),
                            patch('rospy.is_shutdown',return_value=False)):
            replacement.start(); self.addCleanup(replacement.stop)
        n=self.nav=Navigator.__new__(Navigator)
        n.local_retry_wait=1.; n.last_remaining=2.
        n.jump_guard=LocalizationJumpGuard(); n.jump_resume_pending=False
        n.jump_guard.observe(1,(0,0,0),(0,0),None,9.)
        n.jump_distance=.8; n.jump_yaw=.5
        n.hard_fault_serial=n.hard_fault_baseline=0; n.hard_fault_reason=''
        n.server=Mock(); n.server.is_preempt_requested.return_value=False
        n.stop,n.state,n.clear_scan,n.publish_target,n.lease=Mock(),Mock(),Mock(),Mock(),Mock()
        n.check_task=lambda deadline: n.retry_guard(deadline)
        robot=PoseStamped(); robot.pose.orientation.w=1
        n.snapshot=Mock(return_value=(robot,(0,0,0),.327))
        def snapshot():
            robot.header.stamp=rospy.Time.from_sec(100+self.now)
            return robot,(0,0,0),.327
        n.snapshot.side_effect=snapshot

    def test_stop_wait_reset_and_retry_same_target_in_that_order(self):
        n=self.nav; events=[]
        n.stop.side_effect=lambda: events.append(('stop',self.now))
        n.clear_scan.side_effect=lambda: events.append(('reset',self.now))
        n.publish_target.side_effect=lambda *args: events.append(('target',self.now))
        n.lease.side_effect=lambda *args: events.append(('track',self.now))
        transform,stamp=n.retry_local_target((.9,0),False,20,'blocked')
        self.assertGreaterEqual(stamp,11.)
        self.assertEqual([e[0] for e in events[-3:]],['reset','target','track'])
        self.assertTrue(all(e[0]=='stop' for e in events[:-3]))
        n.publish_target.assert_called_once_with((.9,0),False,(0,0,0),.327)
        n.lease.assert_called_once_with(NavigationControl.TRACK)

    def test_cancel_wait_never_resets_or_resends(self):
        n=self.nav
        n.server.is_preempt_requested.side_effect=lambda: self.now>=10.2
        with self.assertRaises(TaskCancelled): n.retry_local_target((.9,0),False,20,'blocked')
        n.clear_scan.assert_not_called(); n.publish_target.assert_not_called(); n.lease.assert_not_called()

    def test_hard_fault_wait_never_resumes(self):
        n=self.nav
        def fault():
            if self.now>=10.2:
                n.hard_fault_serial=1; n.hard_fault_reason='Stale cloud'
        n.stop.side_effect=fault
        with self.assertRaisesRegex(RuntimeError,'Stale cloud'):
            n.retry_local_target((.9,0),False,20,'blocked')
        n.publish_target.assert_not_called(); n.lease.assert_not_called()

    def test_tf_timeout_propagates_to_separate_localization_policy(self):
        n=self.nav; n.snapshot.side_effect=LocalizationTimeout('Stale map/body TF')
        with self.assertRaises(LocalizationTimeout): n.retry_local_target((.9,0),False,20,'blocked')
        n.publish_target.assert_not_called(); n.lease.assert_not_called()

    def test_jump_during_wait_never_resumes(self):
        n=self.nav; robot=n.snapshot.return_value[0]
        def snapshot():
            robot.header.stamp=rospy.Time.from_sec(100+self.now)
            return robot,(1 if self.now>=10.2 else 0,0,0),.327
        n.snapshot.side_effect=snapshot
        with self.assertRaisesRegex(RuntimeError,'localization jump'):
            n.retry_local_target((.9,0),False,20,'blocked')
        n.publish_target.assert_not_called(); n.lease.assert_not_called()

    def test_normal_localization_correction_is_used_for_same_map_target(self):
        n=self.nav; robot=n.snapshot.return_value[0]
        n.snapshot.side_effect=lambda: (robot,(.1 if self.now>=10.2 else 0,0,0),.327)
        n.retry_local_target((.9,0),False,20,'blocked')
        n.publish_target.assert_called_once_with((.9,0),False,(.1,0,0),.327)

    def test_reset_failure_never_releases_track(self):
        n=self.nav; n.clear_scan.side_effect=RuntimeError('reset failed')
        with self.assertRaisesRegex(RuntimeError,'reset failed'):
            n.retry_local_target((.9,0),False,20,'blocked')
        n.publish_target.assert_not_called(); n.lease.assert_not_called()

    def execute_fixture(self,local_state=PlannerState.BLOCKED):
        n=self.nav
        n.poisoned=n.test_stalled=False; n.command_epoch=3; n.minimum_generation=0
        n.xy_tolerance=.15; n.yaw_tolerance=.12; n.target_step=.18
        n.target_period=.3; n.correction_step=.08
        n.loop_period=.05
        n.guide_extension_failures=3; n.guide_extension_step=.5
        n.guide_extension_max_ahead=5.; n.guide_extension_motion=.2
        n.local_recovery_limit=4.; n.stall_timeout=.2; n.local_retry_wait=.2
        n.max_replans=0  # No global recovery allowance: local retries still work.
        n.visible=Mock(return_value=True); n.recover_lease=Mock(return_value=False)
        route=OrderedRoute([(0,0),(2,0)])
        n.make_route=Mock(return_value=route)
        n.local_state=lambda: (PlannerState(state=local_state,generation=1,reason='finishProcess')
                               if n.publish_target.called else None)
        goal=PoseStamped(); goal.header.frame_id='map'
        goal.pose.position.x=2.; goal.pose.orientation.w=1
        return NavigateGoal(target_pose=goal,require_yaw=False),route

    def test_repeated_local_failure_preserves_route_identity_and_task_deadline(self):
        n=self.nav; goal,route=self.execute_fixture()
        with self.assertRaisesRegex(RuntimeError,'Task deadline exceeded'):
            n.execute_attempt(goal,11.2)
        n.make_route.assert_called_once()
        self.assertGreaterEqual(n.publish_target.call_count,3)
        targets=[c.args[0][0] for c in n.publish_target.call_args_list]
        self.assertEqual(targets[:3],[.9,.9,.9])
        self.assertAlmostEqual(targets[3],1.4)
        self.assertLessEqual(max(targets),2.)
        states=[c.args[0].data for c in n.state.publish.call_args_list]
        self.assertIn('BLOCKED_WAIT',states); self.assertIn('LOCAL_RETRY',states)
        self.assertNotIn('REPLANNING_GLOBAL',states)
        self.assertEqual(n.task_epoch,3)

    def test_no_progress_also_retries_locally_without_replanning(self):
        n=self.nav; goal,route=self.execute_fixture(PlannerState.TRACKING)
        with self.assertRaisesRegex(RuntimeError,'Task deadline exceeded'):
            n.execute_attempt(goal,11.2)
        n.make_route.assert_called_once()
        self.assertIn('LOCAL_RETRY',[c.args[0].data for c in n.state.publish.call_args_list])

    def test_tracking_unchanged_target_does_not_resend_but_keeps_lease(self):
        n=self.nav; goal,route=self.execute_fixture(PlannerState.TRACKING)
        n.stall_timeout=15.; n.target_step=.08; n.target_period=.05
        with self.assertRaisesRegex(RuntimeError,'Task deadline exceeded'):
            n.execute_attempt(goal,12.2)
        n.publish_target.assert_called_once()
        n.make_route.assert_called_once()
        self.assertGreater(n.lease.call_count,20)
        self.assertNotIn('LOCAL_RETRY',[c.args[0].data for c in n.state.publish.call_args_list])

    def test_route_deviation_still_uses_global_recovery(self):
        n=self.nav; goal,route=self.execute_fixture()
        n.max_replans=1
        route.select=Mock(return_value=(((.9,0),False),1.))
        with self.assertRaisesRegex(RuntimeError,'Global route invalid/deviated'):
            n.execute_attempt(goal,20)
        self.assertEqual(n.make_route.call_count,2)
        n.publish_target.assert_not_called()

    def jump_execution(self,permanent=False):
        n=self.nav;goal,route=self.execute_fixture(PlannerState.TRACKING)
        n.stall_timeout=15.
        def snapshot():
            robot=PoseStamped();robot.pose.orientation.w=1
            robot.header.stamp=rospy.Time.from_sec(100+self.now)
            bad=self.now>=10.2 and (permanent or self.now<10.31)
            if self.now>=10.9 and not permanent: robot.pose.position.x=2.
            return robot,(1. if bad else 0.,0.,0.),.327
        n.snapshot.side_effect=snapshot
        return goal,route

    def test_transient_jump_keeps_route_and_finishes_with_fresh_target_only(self):
        n=self.nav;goal,route=self.jump_execution()
        n.execute_attempt(goal,15.)
        n.server.set_succeeded.assert_called_once()
        n.make_route.assert_called_once()
        self.assertEqual(n.clear_scan.call_count,2)  # Task start + one suspect-jump reset.
        self.assertEqual(n.publish_target.call_count,2)  # Same guide, new local trajectory after recovery.
        self.assertTrue(all(c.args[2]==(0.,0.,0.) for c in n.publish_target.call_args_list))
        self.assertIn('LOCALIZATION_JUMP_HOLD',[c.args[0].data for c in n.state.publish.call_args_list])
        self.assertEqual(n.task_epoch,3)

    def test_persistent_jump_in_execute_never_publishes_abnormal_target(self):
        n=self.nav;goal,route=self.jump_execution(permanent=True)
        with self.assertRaisesRegex(RuntimeError,'Persistent localization jump'):
            n.execute_attempt(goal,15.)
        n.publish_target.assert_called_once()
        n.make_route.assert_called_once()
        self.assertGreaterEqual(n.jump_guard.bad_count,5)

    def test_cancel_during_jump_in_execute_cannot_resume_old_goal(self):
        n=self.nav;goal,route=self.jump_execution(permanent=True)
        n.server.is_preempt_requested.side_effect=lambda:self.now>=10.3
        with self.assertRaises(TaskCancelled): n.execute_attempt(goal,15.)
        n.publish_target.assert_called_once()
        n.server.set_succeeded.assert_not_called()


if __name__=='__main__': unittest.main()
