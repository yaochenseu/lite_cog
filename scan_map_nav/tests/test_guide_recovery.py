import pathlib
import sys
import unittest
import yaml
from unittest.mock import Mock, patch
import rospy
from visualization_msgs.msg import Marker
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
from rolling_route import OrderedRoute, GuideRecovery
from navigator import Navigator


class GuideRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.route=OrderedRoute([(0,0),(8,0)],lookahead=2.)
        self.visible=lambda a,b: True
        self.normal,_=self.route.select((0,0))
        self.guide=GuideRecovery()
        self.guide.observe_motion((0,0),False)

    def fail(self,arc=2.):
        return self.guide.failed(self.route,(0,0),arc,self.visible)

    def test_third_failed_round_extends_then_one_half_metre_per_failure(self):
        self.assertIsNone(self.fail()); self.assertIsNone(self.fail())
        for arc in (2.5,3.,3.5,4.,4.5,5.):
            choice,actual,offset=self.fail(arc-.5)
            self.assertAlmostEqual(actual,arc)
            self.assertAlmostEqual(choice[0][0],arc)
            self.assertAlmostEqual(offset,arc-2.)
        for _ in range(5): self.assertIsNone(self.fail(5.))
        self.assertAlmostEqual(self.guide.active_arc,5.)

    def test_extension_follows_bent_path_arc_not_world_x(self):
        self.route=OrderedRoute([(0,0),(0,2),(.1,6)],lookahead=2.)
        self.route.select((0,0))
        self.fail(); self.fail()
        choice,arc,_=self.fail()
        self.assertEqual(choice[0],self.route.at(2.5))
        self.assertAlmostEqual(arc,2.5)

    def test_right_angle_is_not_cut_to_reach_extension(self):
        self.route=OrderedRoute([(0,0),(2,0),(2,6)],lookahead=2.)
        self.route.select((0,0))
        self.fail(); self.fail()
        self.assertIsNone(self.fail())
        self.assertIsNone(self.guide.active_arc)

    def test_invisible_stages_skipped_without_publishing_them(self):
        self.visible=lambda a,b: b[0]>3.1
        self.fail(); self.fail()
        self.assertAlmostEqual(self.fail()[1],3.5)

    def test_goal_clamping_never_overshoots_or_repeats_same_trial(self):
        self.route=OrderedRoute([(0,0),(3.2,0)],lookahead=2.)
        self.route.select((0,0))
        self.fail(); self.fail()
        current=2.
        for expected in (2.5,3.,3.2):
            candidate,arc,_=self.fail(current)
            self.assertAlmostEqual(arc,expected)
            current=arc
        self.assertTrue(candidate[1])
        self.assertIsNone(self.fail(current))

    def test_already_final_guide_does_not_extend(self):
        self.route=OrderedRoute([(0,0),(1.2,0)],lookahead=2.)
        self.route.select((0,0))
        for _ in range(5): self.assertIsNone(self.fail(1.2))
        self.assertIsNone(self.guide.active_arc)

    def test_hold_extended_target_until_normal_rolling_guide_catches_up(self):
        self.fail(); self.fail(); self.fail()
        self.assertTrue(self.guide.observe_motion((.21,0),True))
        self.assertEqual(self.guide.failures,0)
        normal,_=self.route.select((.21,0))
        choice,arc=self.guide.choose(self.route,(.21,0),normal,self.visible)
        self.assertAlmostEqual(arc,2.5)  # Moving must not pull the working point back to 2.21.
        normal,_=self.route.select((.5,0))
        choice,arc=self.guide.choose(self.route,(.5,0),normal,self.visible)
        self.assertAlmostEqual(arc,2.5)
        self.assertIsNone(self.guide.active_arc)

    def test_normal_motion_clears_consecutive_failure_count(self):
        self.fail(); self.fail()
        for x in (.1,.15,.199):
            self.assertFalse(self.guide.observe_motion((x,0),True))
            self.assertEqual(self.guide.failures,2)
        self.assertTrue(self.guide.observe_motion((.2,0),True))
        self.assertEqual(self.guide.failures,0)
        self.assertIsNone(self.fail())

    def test_tracking_label_and_map_correction_do_not_count_as_movement(self):
        self.fail(); self.fail(); self.fail()
        for _ in range(5):
            self.assertFalse(self.guide.observe_motion((0,0),True))
        normal,_=self.route.select((.5,0))
        self.guide.choose(self.route,(.5,0),normal,self.visible)
        self.assertEqual(self.guide.failures,3)
        self.assertEqual(self.guide.limit_arc,5.)

    def test_motion_while_blocked_is_not_a_successful_scan_trial(self):
        self.fail(); self.fail(); self.fail()
        self.assertFalse(self.guide.observe_motion((.21,0),False))
        self.assertEqual(self.guide.failures,3)

    def test_new_blockage_after_real_motion_requires_three_failures_again(self):
        self.fail(); self.fail(); self.fail()
        self.guide.observe_motion((.21,0),True)
        self.assertIsNone(self.fail(2.5)); self.assertIsNone(self.fail(2.5))
        self.assertAlmostEqual(self.fail(2.5)[1],3.)

    def test_limit_is_frozen_until_actual_motion_not_advanced_by_map_jitter(self):
        self.fail(); self.fail(); self.fail()
        self.route.select((.05,0))
        current=2.5
        for expected in (3.,3.5,4.,4.5,5.):
            _,current,_=self.fail(current)
            self.assertAlmostEqual(current,expected)
        self.assertIsNone(self.fail(current))

    def test_small_back_and_forth_motion_does_not_accumulate_travel_to_clear_count(self):
        self.fail(); self.fail()
        for x in (.1,-.1,.15,-.15,0.,.199):
            self.assertFalse(self.guide.observe_motion((x,0),True))
            self.assertEqual(self.guide.failures,2)

    def test_limit_is_ahead_of_current_progress_not_map_origin(self):
        self.route.progress=2.
        self.route.select((2.,0))
        for _ in range(2):
            self.assertIsNone(self.guide.failed(self.route,(2.,0),4.,self.visible))
        current=4.
        for expected in (4.5,5.,5.5,6.,6.5,7.):
            _,current,_=self.guide.failed(self.route,(2.,0),current,self.visible)
            self.assertAlmostEqual(current,expected)
        self.assertIsNone(self.guide.failed(self.route,(2.,0),current,self.visible))

    def test_partial_progress_does_not_extend_to_a_point_behind_current_guide(self):
        self.fail(2.); self.fail(2.05)
        candidate,arc,_=self.fail(2.15)
        self.assertAlmostEqual(arc,2.65)  # Step from the current, not the first failed point.

    def test_crossing_does_not_jump_to_later_return_branch(self):
        self.route=OrderedRoute([(0,0),(6,0),(6,2),(0,2),(0,0),(2,-1)],lookahead=2.)
        self.route.select((0,0))
        self.fail(); self.fail()
        self.assertEqual(self.fail()[0][0],(2.5,0.))

    def test_new_task_or_route_reset_clears_extension(self):
        self.fail(); self.fail(); self.fail()
        self.guide.reset()
        self.assertIsNone(self.guide.active_arc)
        self.assertIsNone(self.fail())

    def test_invalid_parameters_rejected(self):
        for args in ((0,.5,5.,.1),(3,0,5.,.1),(3,.5,0,.1),(3,.5,5.,0),
                     (3,float('nan'),5.,.1),(3,.5,float('inf'),.1),(3,.5,5.,float('nan'))):
            with self.assertRaises(ValueError): GuideRecovery(*args)


class TargetCadenceTests(unittest.TestCase):
    def setUp(self):
        self.nav=Navigator.__new__(Navigator)
        self.nav.target_step=.08; self.nav.target_period=.05
        self.nav.correction_step=.08

    def due(self,new,elapsed=.11,transform=(0,0,0),final=False):
        return self.nav.target_update_due(new,final,(.9,0),False,transform,(0,0,0),elapsed)

    def test_point_advances_well_before_robot_reaches_previous_guide(self):
        self.assertTrue(self.due((1.,0)))

    def test_small_change_no_longer_bypasses_threshold_near_guide(self):
        self.assertFalse(self.due((.94,0),30.))

    def test_period_still_bounds_publish_rate(self):
        self.assertFalse(self.due((1.1,0),.02))
        self.assertTrue(self.due((1.1,0),.06))

    def test_unchanged_target_never_resends_on_timer(self):
        for elapsed in (.5,1.,2.,30.,300.):
            with self.subTest(elapsed=elapsed):
                self.assertFalse(self.due((.9,0),elapsed))

    def test_first_target_is_not_throttled(self):
        self.assertTrue(self.nav.target_update_due((2.,0),False,None,None,(0,0,0),None,0))

    def test_final_flag_change_is_delivered_even_at_same_position(self):
        self.assertTrue(self.due((.9,0),final=True))
        self.assertFalse(self.due((.9,0),elapsed=.02,final=True))

    def test_small_motion_accumulates_against_last_sent_not_last_observed(self):
        for point in (.93,.96):
            self.assertFalse(self.due((point,0)))
        self.assertTrue(self.due((.99,0)))

    def test_subthreshold_localization_jitter_does_not_resend(self):
        for offset in (-.04,.04,-.07,.07):
            self.assertFalse(self.due((.9,0),30.,transform=(offset,0,0)))

    def test_significant_localization_translation_updates_unchanged_map_target(self):
        self.assertTrue(self.due((.9,0),transform=(.09,0,0)))

    def test_localization_rotation_is_measured_at_guide_not_map_origin(self):
        self.assertFalse(self.nav.target_update_due((2.,0),False,(2.,0),False,
                                                   (0,0,.03),(0,0,0),.1))
        self.assertTrue(self.nav.target_update_due((2.,0),False,(2.,0),False,
                                                  (0,0,.05),(0,0,0),.1))


class TargetMarkerTests(unittest.TestCase):
    def test_stationary_target_marker_persists_without_command_refresh_and_can_be_cleared(self):
        nav=Navigator.__new__(Navigator)
        nav.task_epoch=1; nav.task_id=2
        nav.target=Mock(); nav.target_marker=Mock()
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            nav.publish_target((2.,0),False,(0,0,0),.327)
        marker=nav.target_marker.publish.call_args.args[0]
        self.assertEqual(marker.action,Marker.ADD)
        self.assertEqual(marker.lifetime.to_sec(),0.)
        nav.clear_target_marker()
        deleted=nav.target_marker.publish.call_args.args[0]
        self.assertEqual(deleted.action,Marker.DELETE)
        self.assertEqual((deleted.ns,deleted.id),(marker.ns,marker.id))
        nav.target.publish.assert_called_once()


class TwoMetreConfigTests(unittest.TestCase):
    def setUp(self):
        path=pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/config/rolling.yaml'
        self.config=yaml.safe_load(path.read_text())

    def route(self,points):
        return OrderedRoute(points,self.config['lookahead'],self.config['corner_cut'])

    def test_actual_config_sends_two_metres_ahead_and_rolls_forward(self):
        route=self.route([(0,0),(5,0)])
        first,_=route.select((0,0)); second,_=route.select((.1,0))
        self.assertEqual(first,((2.,0.),False))
        self.assertAlmostEqual(second[0][0],2.1)

    def test_actual_config_still_clamps_goal_and_does_not_cut_corner(self):
        short=self.route([(0,0),(1.2,0)])
        choice,_=short.select((0,0))
        self.assertEqual(choice,((1.2,0.),True))
        corner=self.route([(0,0),(.6,0),(.6,3)])
        choice,_=corner.select((0,0))
        self.assertEqual(choice,((.6,0.),False))

    def test_recovery_extends_two_metre_guide_to_five_metres(self):
        route=self.route([(0,0),(8,0)]); route.select((0,0))
        guide=GuideRecovery(self.config['guide_extension_failures'],self.config['guide_extension_step'],
                            self.config['guide_extension_max_ahead'],self.config['guide_extension_motion'])
        visible=lambda a,b: True
        self.assertIsNone(guide.failed(route,(0,0),2.,visible))
        self.assertIsNone(guide.failed(route,(0,0),2.,visible))
        current=2.
        for expected in (2.5,3.,3.5,4.,4.5,5.):
            _,current,_=guide.failed(route,(0,0),current,visible)
            self.assertAlmostEqual(current,expected)
        self.assertIsNone(guide.failed(route,(0,0),current,visible))


if __name__=='__main__': unittest.main()
