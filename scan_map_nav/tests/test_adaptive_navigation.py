#!/usr/bin/python3
import math
import pathlib
import sys
import threading
import time
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
from scan_map_navigation.msg import PlanningGrid as GridMsg
from planning_grid import PlanningGrid, BlockageConfirmation, AdaptiveLookahead
from rolling_route import OrderedRoute
from async_plan import AsyncPlan


def grid():
    msg=GridMsg(valid=True,revision=1)
    msg.header.frame_id='map'
    msg.info.width=msg.info.height=120
    msg.info.resolution=.05
    msg.info.origin.position.x=msg.info.origin.position.y=-3
    msg.info.origin.orientation.w=1
    msg.occupancy=[0]*14400; msg.topology=[0]*14400; msg.costs=[0]*14400
    return PlanningGrid(msg)


class AdaptiveTests(unittest.TestCase):
    def test_normal_point_is_point_nine_not_path_check_horizon(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        choice=g.candidate(route,(0,0),.9)
        self.assertAlmostEqual(choice[0][0],.9)
        g.occupancy[g.cell(1.9,0)]=100
        self.assertTrue(g.route_blocked(route,2))
        self.assertEqual(choice,g.candidate(route,(0,0),.9))

    def test_forward_check_includes_body_width(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        g.occupancy[g.cell(1.5,.3)]=100
        self.assertTrue(g.visible((0,0),(2,0),False))
        self.assertTrue(g.route_blocked(route,2))

    def test_new_box_can_lie_between_robot_and_longer_target(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        for x in (.75,.8,.85):
            for y in (-.1,0,.1):
                g.occupancy[g.cell(x,y)]=100
        self.assertIsNone(g.candidate(route,(0,0),.9))
        self.assertIsNotNone(g.candidate(route,(0,0),1.6))
        self.assertFalse(g.visible((0,0),(1.6,0),False))

    def test_candidate_body_must_fit_not_just_center(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        g.occupancy[g.cell(1.6,.3)]=100
        self.assertIsNone(g.candidate(route,(0,0),1.6))

    def test_prior_wall_not_shortcut_but_confirmed_removal_opens_it(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        i=g.cell(.8,0)
        g.topology[i]=g.occupancy[i]=100
        self.assertIsNone(g.candidate(route,(0,0),1.6))
        g.topology[i]=g.occupancy[i]=0
        self.assertIsNotNone(g.candidate(route,(0,0),1.6))

    def test_corner_not_cut_by_longer_target(self):
        g=grid(); route=OrderedRoute([(0,0),(.6,0),(.6,2)])
        self.assertAlmostEqual(g.candidate(route,(0,0),.9)[0][0],.6)
        self.assertIsNone(g.candidate(route,(0,0),1.6))

    def test_unknown_target_not_assumed_free(self):
        g=grid(); route=OrderedRoute([(0,0),(2.5,0)])
        g.occupancy[g.cell(1.6,0)]=-1
        self.assertIsNone(g.candidate(route,(0,0),1.6))

    def test_distinct_map_updates_required_to_confirm(self):
        c=BlockageConfirmation(1)
        self.assertFalse(c.update(True,1,0))
        self.assertFalse(c.update(True,1,2))
        self.assertTrue(c.update(True,2,2.1))
        self.assertFalse(c.update(False,3,2.2))
        self.assertFalse(c.update(True,4,2.3))

    def test_ladder_and_hold(self):
        a=AdaptiveLookahead()
        choose=lambda d: ((d,0),False)
        for now,d in enumerate((1.3,1.6,2.)):
            self.assertEqual(a.advance(now,choose),((d,0),False))
            self.assertEqual(a.target,((d,0),False))
        self.assertIsNone(a.advance(3,choose))

    def test_no_feasible_target_escalates(self):
        a=AdaptiveLookahead()
        self.assertIsNone(a.advance(1,lambda d: None))

    def test_stage_and_total_budgets(self):
        a=AdaptiveLookahead(stage_budget=5,total_budget=8)
        a.advance(0,lambda d: ((d,0),False))
        self.assertFalse(a.expired(4))
        self.assertTrue(a.expired(5))
        a.advance(5,lambda d: ((d,0),False))
        self.assertTrue(a.exhausted(8))
        self.assertIsNone(a.advance(8,lambda d: ((d,0),False)))

    def test_gradual_restore_needs_stable_clear_tracking(self):
        a=AdaptiveLookahead(restore_time=1)
        for t in (0,1,2): a.advance(t,lambda d: ((d,0),False))
        self.assertFalse(a.restore(True,3))
        self.assertFalse(a.restore(False,3.5))
        self.assertFalse(a.restore(True,4))
        self.assertTrue(a.restore(True,5))
        self.assertAlmostEqual(a.distance,1.6)
        self.assertTrue(a.restore(True,6))
        self.assertAlmostEqual(a.distance,1.3)
        self.assertTrue(a.restore(True,7))
        self.assertAlmostEqual(a.distance,.9)

    def test_async_planning_never_blocks_caller_or_commits_execution(self):
        release=threading.Event()
        job=AsyncPlan(lambda: (release.wait(1),'candidate')[1],42)
        self.assertFalse(job.done.is_set())
        self.assertEqual(job.task_id,42)
        release.set()
        self.assertTrue(job.done.wait(1))
        self.assertEqual(job.result,'candidate')

    def test_worker_failure_is_data_not_background_motion(self):
        job=AsyncPlan(lambda: 1/0,42)
        self.assertTrue(job.done.wait(1))
        self.assertIsInstance(job.error,ZeroDivisionError)


if __name__=='__main__':
    unittest.main()
