"""Debounce actual fresh localization samples; never execute through a suspect TF."""
import math
import pathlib
import sys
import unittest
from unittest.mock import Mock,patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
from localization_guard import LocalizationJumpGuard
from navigator import Navigator,TaskCancelled,LocalizationTimeout
import rospy
from geometry_msgs.msg import PoseStamped


class JumpGuardTests(unittest.TestCase):
    def setUp(self):
        self.g=LocalizationJumpGuard()
        self.g.observe(1,(0,0,0),(0,0),(2,0),0.)

    def sample(self,t,transform=(1,0,0),stamp=None):
        return self.g.observe(stamp if stamp is not None else int(t*1000)+1,
                              transform,(0,0),(2,0),t)

    def test_first_outlier_holds_instead_of_aborting(self):
        self.assertEqual(self.sample(.1),'HOLD')
        self.assertEqual(self.g.bad_count,1)
        self.assertEqual(self.g.anchor,(0,0,0))

    def test_permanent_step_is_compared_to_last_good_not_previous_bad(self):
        for t in (.1,.2,.3,.4): self.assertEqual(self.sample(t),'HOLD')
        with self.assertRaisesRegex(RuntimeError,'5 fresh frames'):
            self.sample(.5)
        self.assertEqual(self.g.anchor,(0,0,0))

    def test_rotation_alone_requires_multiple_samples(self):
        for t in (.1,.2,.3,.4): self.assertEqual(self.sample(t,(0,0,.6)),'HOLD')
        with self.assertRaisesRegex(RuntimeError,'localization jump'):
            self.sample(.5,(0,0,.6))

    def test_duplicate_or_reordered_timestamps_cannot_inflate_count(self):
        self.sample(.1,stamp=100)
        for t,stamp in ((.2,100),(.3,99),(.4,100),(.5,98)):
            self.assertEqual(self.sample(t,stamp=stamp),'HOLD')
        self.assertEqual(self.g.bad_count,1)

    def test_frame_count_alone_without_duration_cannot_abort(self):
        for i in range(1,8): self.assertEqual(self.sample(i*.01),'HOLD')
        with self.assertRaisesRegex(RuntimeError,'localization jump'):
            self.sample(.4)

    def test_duration_alone_without_new_frames_cannot_confirm_jump(self):
        self.sample(.1,stamp=100)
        self.assertEqual(self.sample(.8,stamp=100),'HOLD')
        self.assertEqual(self.g.bad_count,1)

    def test_transient_recovers_only_after_three_good_fresh_samples(self):
        self.sample(.1); self.sample(.2)
        self.assertEqual(self.sample(.3,(0,0,0)),'HOLD')
        self.assertEqual(self.sample(.4,(0,0,0)),'HOLD')
        self.assertEqual(self.sample(.5,(0,0,0)),'RECOVERED')
        self.assertFalse(self.g.pending)

    def test_duplicate_good_sample_does_not_release_hold(self):
        self.sample(.1)
        for t in (.2,.3,.4,.5): self.assertEqual(self.sample(t,(0,0,0),200),'HOLD')
        self.assertEqual(self.g.good_count,1)

    def test_a_bad_sample_interrupts_good_recovery_sequence(self):
        self.sample(.1); self.sample(.2,(0,0,0)); self.sample(.3,(0,0,0));self.sample(.4)
        self.assertEqual(self.g.good_count,0)
        for t in (.5,.6): self.assertEqual(self.sample(t,(0,0,0)),'HOLD')
        self.assertEqual(self.sample(.7,(0,0,0)),'RECOVERED')

    def test_alternating_bad_good_remains_stopped_then_times_out(self):
        for i in range(1,21): self.sample(i*.1,(1 if i%2 else 0,0,0))
        with self.assertRaisesRegex(RuntimeError,'did not settle'):
            self.sample(2.2)

    def test_regular_corrections_update_baseline_without_hold(self):
        for i in range(1,8): self.assertEqual(self.sample(i*.1,(i*.1,0,0)),'OK')
        self.assertAlmostEqual(self.g.anchor[0],.7)

    def test_long_guide_is_clipped_to_one_metre_for_jump_probes(self):
        self.g.reset();self.g.observe(1,(0,0,0),(10,0),(15,0),0.)
        # Rotate about robot, not distant map origin or 5 m target.
        theta=.2
        trans=(10-10*math.cos(theta),-10*math.sin(theta),theta)
        self.assertEqual(self.g.observe(2,trans,(10,0),(15,0),.1),'OK')

    def test_reset_only_at_new_task_discards_old_pending_state(self):
        self.sample(.1);self.g.reset()
        self.assertEqual(self.sample(.2),'OK')

    def test_invalid_configuration_rejected(self):
        for kw in ({'confirm_frames':1},{'recover_frames':True},{'confirm_time':0},
                   {'hold_timeout':.2},{'distance_limit':float('nan')}):
            with self.assertRaises(ValueError): LocalizationJumpGuard(**kw)


class NavigatorJumpHoldTests(unittest.TestCase):
    def setUp(self):
        n=self.n=Navigator.__new__(Navigator)
        n.jump_guard=LocalizationJumpGuard();n.jump_resume_pending=False
        n.jump_guard.observe(1,(0,0,0),(0,0),(2,0),0.)
        n.stop,n.clear_scan,n.state,n.server,n.check_task=Mock(),Mock(),Mock(),Mock(),Mock()
        n.last_remaining=2.
        self.t=.1
        self.transforms=iter([(1,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)])
        def snapshot():
            p=PoseStamped();p.header.stamp=rospy.Time.from_sec(100+self.t)
            return p,next(self.transforms),.327
        n.snapshot=Mock(side_effect=snapshot)
        def sleep(dt): self.t+=.1
        for p in (patch('navigator.time.monotonic',side_effect=lambda:self.t),
                  patch('navigator.time.sleep',side_effect=sleep)):
            p.start();self.addCleanup(p.stop)

    def test_checked_snapshot_stops_resets_once_and_returns_only_recovered_transform(self):
        robot,transform,_=self.n.checked_snapshot(10,(2,0))
        self.assertEqual(transform,(0,0,0))
        self.assertGreaterEqual(self.n.stop.call_count,3)
        self.n.clear_scan.assert_called_once()
        self.assertTrue(self.n.jump_resume_pending)
        self.assertEqual(self.n.jump_guard.bad_count,0)

    def test_cancel_during_hold_cannot_return_pose_for_motion(self):
        self.n.check_task.side_effect=[None,TaskCancelled()]
        with self.assertRaises(TaskCancelled): self.n.checked_snapshot(10)
        self.n.stop.assert_called()

    def test_hard_input_failure_interrupts_hold(self):
        self.n.check_task.side_effect=[None,RuntimeError('Stale cloud')]
        with self.assertRaisesRegex(RuntimeError,'Stale cloud'): self.n.checked_snapshot(10)

    def test_tf_loss_still_uses_localization_timeout_recovery(self):
        old=self.n.snapshot.side_effect
        def snapshot():
            if self.t>.1: raise LocalizationTimeout('Stale map/body TF')
            return old()
        self.n.snapshot.side_effect=snapshot
        with self.assertRaises(LocalizationTimeout): self.n.checked_snapshot(10)
        self.assertTrue(self.n.jump_guard.pending)
        self.assertEqual(self.n.jump_guard.anchor,(0,0,0))

    def test_failed_reset_never_releases_hold(self):
        self.n.clear_scan.side_effect=RuntimeError('SCAN reset failed')
        with self.assertRaisesRegex(RuntimeError,'reset failed'): self.n.checked_snapshot(10)


if __name__=='__main__': unittest.main()
