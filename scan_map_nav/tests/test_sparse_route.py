import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
from sparse_route import SparseRoute, GuideProgress, local_jump_probes
from rolling_route import distance, correction_size, planar_transform


class SparseRouteTests(unittest.TestCase):
    def test_dense_straight_path_becomes_few_stable_guides(self):
        route = SparseRoute([(i/20,0) for i in range(201)])
        self.assertEqual(len(route.points),5)  # 10m, four 2.5m segments
        first,_ = route.select((0,0))
        self.assertEqual(first,((2.5,0),False))
        self.assertEqual(route.select((1.5,0))[0],first)
        self.assertEqual(route.select((2.1,0))[0],((5,0),False))

    def test_short_open_route_goes_directly_to_final_goal(self):
        route = SparseRoute([(0,0),(.1,0),(.8,0),(2.7,0)])
        self.assertEqual(route.points,[(0,0),(2.7,0)])
        self.assertEqual(route.select((0,0))[0],((2.7,0),True))

    def test_detour_does_not_drag_target_toward_robot_or_reset_progress(self):
        route = SparseRoute([(0,0),(3,0),(6,0)])
        first,_ = route.select((0,0))
        choice,deviation = route.select((1,1.5))
        self.assertEqual(choice,first)
        self.assertEqual(route.index,1)
        self.assertAlmostEqual(deviation,1.5)

    def test_corner_retained_and_switch_needs_next_corridor_visibility(self):
        route = SparseRoute([(0,0),(2,0),(2,2)])
        self.assertEqual(route.points,[(0,0),(2,0),(2,2)])
        self.assertEqual(route.select((1.6,0),lambda a,b: b!=(2,2))[0],((2,0),False))
        self.assertEqual(route.select((1.6,0),lambda a,b: True)[0],((2,2),True))

    def test_small_geometric_bend_cannot_be_removed_through_wall(self):
        def visible(a,b):
            return not (a==(0,0) and b==(2,0))
        route = SparseRoute([(0,0),(1,.1),(2,0)],visible)
        self.assertIn((1,.1),route.points)

    def test_no_nearest_point_jump_to_later_parallel_corridor(self):
        route = SparseRoute([(0,0),(2,0),(2,2),(0,2),(0,.1)])
        first,_ = route.select((0,.15))
        self.assertEqual(first,((2,0),False))
        self.assertEqual(route.index,1)

    def test_passing_intermediate_point_does_not_require_exact_arrival(self):
        route = SparseRoute([(0,0),(3,0),(6,0)])
        self.assertEqual(route.select((3.6,.2))[0],((6,0),True))

    def test_no_corner_switch_through_wall_when_almost_at_guide(self):
        route = SparseRoute([(0,0),(2,0),(2,2)])
        choice,_ = route.select((1.9,0),lambda a,b: False)
        self.assertIsNone(choice)
        self.assertEqual(route.index,1)

    def test_final_guide_not_consumed_at_intermediate_radius(self):
        route = SparseRoute([(0,0),(2,0)])
        self.assertEqual(route.select((1.6,0))[0],((2,0),True))

    def test_endpoints_spacing_and_invalid_input(self):
        route = SparseRoute([(0,0),(0,0),(7,0)])
        self.assertEqual(route.points[-1],(7,0))
        self.assertTrue(all(distance(a,b)<=3 for a,b in zip(route.points,route.points[1:])))
        for points in ([(0,0),(float('nan'),0)],[(0,0),(0,0)]):
            with self.assertRaises(ValueError): SparseRoute(points)
        with self.assertRaises(ValueError): SparseRoute([(0,0),(1,0)],lambda a,b:False)

    def test_localization_does_not_mutate_map_guides(self):
        route = SparseRoute([(0,0),(3,0),(6,0)])
        route.select((.1,0))
        before = list(route.points)
        route.select((.3,.1))
        self.assertEqual(route.points,before)

    def test_distant_guide_does_not_amplify_localization_jump_check(self):
        old = planar_transform((10,0,0),(10,0,0))
        new = planar_transform((10,0,.2),(10,0,0))
        shift,turn = correction_size(old,new,local_jump_probes((10,0),(20,0)))
        self.assertLess(shift,.21)
        self.assertAlmostEqual(turn,.2)
        self.assertGreater(correction_size(old,(old[0]+1,old[1],old[2]),
                                          local_jump_probes((10,0),(20,0)))[0],.8)


class GuideProgressTests(unittest.TestCase):
    def test_lateral_detour_over_old_threshold_is_allowed(self):
        progress = GuideProgress()
        self.assertEqual(progress.update(1,3,0,0),'')
        self.assertEqual(progress.update(1,3.5,1.5,20),'')
        self.assertEqual(progress.update(1,2.8,1.5,30),'')
        self.assertEqual(progress.update(1,2.8,0,60),'')

    def test_persistent_excessive_deviation_not_one_frame(self):
        progress = GuideProgress()
        self.assertEqual(progress.update(1,4,3.5,0),'')
        self.assertEqual(progress.update(1,4,3.5,2),'')
        self.assertIn('deviation',progress.update(1,4,3.5,3))

    def test_no_endless_motion_without_useful_progress(self):
        progress = GuideProgress()
        progress.update(1,3,0,0)
        self.assertIn('No useful progress',progress.update(1,3.1,1,46))
        self.assertEqual(progress.update(2,4,0,47),'')

    def test_deviation_timer_cleared_when_back_in_corridor(self):
        progress = GuideProgress()
        progress.update(1,3,4,0)
        progress.update(1,3,2,2)
        self.assertEqual(progress.update(1,3,4,3),'')


if __name__ == '__main__':
    unittest.main()
