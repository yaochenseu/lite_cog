#!/usr/bin/python3
import math
import pathlib
import sys
import unittest
from unittest.mock import Mock, patch
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src/scan_map_navigation/scripts'))
from route_recovery import nearby_probes, transform_shift, StableTransformWindow, RefreshBudget
from legacy_navigator import Navigator, TaskCancelled
from nav_msgs.msg import Odometry


def transform(x=0, y=0, yaw=0):
    t = np.eye(4)
    c,s = math.cos(yaw),math.sin(yaw)
    t[:2,:2] = [[c,-s],[s,c]]
    t[:2,3] = [x,y]
    return t


class RouteGeometryTests(unittest.TestCase):
    def test_translation_is_detected(self):
        old,new = transform(),transform(x=0.4)
        probes = nearby_probes(old,(3,0,0),[(0,0),(8,0)])
        self.assertAlmostEqual(transform_shift(old,new,probes)[0],0.4)

    def test_rotation_about_robot_not_about_remote_origin(self):
        old = transform()
        new = transform(yaw=math.radians(6))
        robot = np.array([4,0,0,1])
        new[:2,3] = (robot-new.dot(robot))[:2]
        self.assertGreater(np.linalg.norm(new[:2,3]),0.35)  # old test falsely stopped
        probes = nearby_probes(old,(4,0,0),[(0,0),(20,0)],horizon=1.5)
        shift,yaw = transform_shift(old,new,probes)
        self.assertLess(shift,0.16)
        self.assertAlmostEqual(yaw,math.radians(6))

    def test_probes_keep_bend_and_limit_horizon(self):
        probes = nearby_probes(transform(),(0.5,0,0),[(0,0),(1,0),(1,10)],1.5)
        self.assertTrue(any(np.allclose(p,[1,0,0]) for p in probes))
        self.assertTrue(np.allclose(probes[-1],[1,1,0]))

    def test_robot_anchor_uses_inverse_reference(self):
        probes = nearby_probes(transform(10,-2,math.pi/2),(10,-1,0),[(0,0),(3,0)])
        self.assertTrue(np.allclose(probes[0],[1,0,0]))

    def test_nonfinite_tf_rejected(self):
        t = transform()
        t[0,3] = float('nan')
        with self.assertRaises(ValueError):
            transform_shift(transform(),t,[[0,0,0]])

    def test_yaw_wrap(self):
        _,yaw = transform_shift(transform(yaw=math.pi-0.01),transform(yaw=-math.pi+0.01),[[0,0,0]])
        self.assertAlmostEqual(yaw,0.02)


class StabilityTests(unittest.TestCase):
    def setUp(self):
        self.window = StableTransformWindow(1.0,0.05,0.04)
        self.probes = [[0,0,0],[1,0,0]]

    def test_needs_full_stable_window(self):
        self.assertFalse(self.window.update(0,transform(),self.probes))
        self.assertFalse(self.window.update(0.9,transform(),self.probes))
        self.assertTrue(self.window.update(1.0,transform(),self.probes))

    def test_cumulative_drift_resets_window(self):
        for i in range(10):
            self.assertFalse(self.window.update(i*0.2,transform(x=i*0.02),self.probes))

    def test_moving_or_missing_tf_resets_window(self):
        self.window.update(0,transform(),self.probes)
        self.assertFalse(self.window.update(1,transform(),self.probes,stopped=False))
        self.assertFalse(self.window.update(2,transform(),self.probes))
        self.assertFalse(self.window.update(2.5,None,self.probes))
        self.assertFalse(self.window.update(3,transform(),self.probes))

    def test_budget_and_cooldown(self):
        budget = RefreshBudget(2,2.0)
        budget.last_plan = 10
        self.assertFalse(budget.cooled_down(11.9))
        self.assertTrue(budget.cooled_down(12))
        budget.begin()
        budget.begin()
        with self.assertRaisesRegex(RuntimeError,'limit'):
            budget.begin()


class RecoveryWaitTests(unittest.TestCase):
    def setUp(self):
        self.nav = Navigator.__new__(Navigator)
        self.nav.recovery = dict(wait_timeout=8.0,stable_duration=1.0,stable_distance=0.05,
                                 stable_yaw=0.04,stopped_speed=0.05,stopped_yaw_speed=0.1)
        self.nav.odom = Odometry()
        self.nav.stop = Mock()
        self.nav.clear_scan = Mock()
        self.nav.report = Mock()
        self.nav.check_task = Mock()
        self.nav.map_pose = Mock()
        self.nav.map_to_odom = Mock(return_value=(transform(),0))
        self.clock = [0.0]
        self.budget = RefreshBudget(3,2.0)
        self.budget.last_plan = 0

    def wait(self):
        with patch('legacy_navigator.time.monotonic',side_effect=lambda: self.clock[0]), \
             patch('legacy_navigator.time.sleep',side_effect=lambda dt: self.clock.__setitem__(0,self.clock[0]+dt)):
            return self.nav.wait_for_localization([[0,0,0],[1,0,0]], self.budget, 7, 300, 2.0)

    def test_pause_clear_stabilize_cooldown_then_replan(self):
        self.assertTrue(np.allclose(self.wait(),transform()))
        self.nav.clear_scan.assert_called_once()
        self.assertGreater(self.nav.stop.call_count,10)
        self.assertGreaterEqual(self.clock[0],2)
        self.assertEqual(self.nav.report.call_args_list[-1].args[0],'REPLANNING_AFTER_LOCALIZATION')

    def test_cancel_during_wait_never_resumes(self):
        self.nav.check_task.side_effect = TaskCancelled()
        with self.assertRaises(TaskCancelled):
            self.wait()
        self.assertEqual(self.nav.report.call_count,1)

    def test_unstable_tf_times_out_stopped(self):
        self.nav.map_to_odom.side_effect = lambda: (transform(x=0.2*(int(self.clock[0]*10)%2)),0)
        with self.assertRaisesRegex(RuntimeError,'stabilize'):
            self.wait()
        self.assertGreaterEqual(self.clock[0],8)
        self.assertEqual(self.nav.report.call_count,1)

    def test_fault_or_task_deadline_is_not_ignored(self):
        self.nav.check_task.side_effect = RuntimeError('Task deadline exceeded')
        with self.assertRaisesRegex(RuntimeError,'deadline'):
            self.wait()
        self.assertEqual(self.nav.report.call_count,1)

    def test_refresh_limit_stops_before_reset(self):
        self.budget.count = 3
        with self.assertRaisesRegex(RuntimeError,'limit'):
            self.wait()
        self.nav.stop.assert_called_once()
        self.nav.clear_scan.assert_not_called()


if __name__ == '__main__':
    unittest.main()
