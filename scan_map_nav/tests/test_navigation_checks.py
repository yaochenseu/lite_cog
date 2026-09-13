#!/usr/bin/python3
import ast
import math
import pathlib
import sys
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import Mock, patch
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src/scan_map_navigation/scripts'))
import rospy
from nav_msgs.msg import OccupancyGrid
from navigator import Navigator
from rolling_route import OrderedRoute, planar_transform, transform_point, correction_size


class RollingRouteTests(unittest.TestCase):
    def test_advances_target_before_stopping(self):
        route = OrderedRoute([(0,0),(3,0)])
        first,_ = route.select((0,0))
        second,_ = route.select((0.4,0))
        self.assertAlmostEqual(first[0][0],0.9)
        self.assertAlmostEqual(second[0][0],1.3)
        self.assertFalse(second[1])

    def test_final_endpoint(self):
        route = OrderedRoute([(0,0),(0.6,0)])
        choice,_ = route.select((0,0))
        self.assertEqual(choice,((0.6,0.0),True))

    def test_does_not_cut_right_angle(self):
        route = OrderedRoute([(0,0),(0.6,0),(0.6,2)])
        choice,_ = route.select((0,0))
        self.assertEqual(choice[0],(0.6,0))
        self.assertFalse(choice[1])

    def test_does_not_skip_to_crossing_branch(self):
        route = OrderedRoute([(0,0),(2,0),(2,2),(0,2),(0,0),(2,-1)])
        choice,_ = route.select((0.05,0))
        self.assertLess(route.progress,0.1)
        self.assertAlmostEqual(choice[0][1],0)

    def test_progress_does_not_reverse(self):
        route = OrderedRoute([(0,0),(3,0)])
        route.select((0.4,0))
        route.select((0.1,0))
        self.assertAlmostEqual(route.progress,0.4)

    def test_wall_prevents_target_shortcut(self):
        route = OrderedRoute([(0,0),(0.4,0),(1,0)])
        choice,_ = route.select((0,0),lambda a,b: b[0]<0.5)
        self.assertEqual(choice[0],(0.4,0))
        choice,_ = route.select((0,0),lambda a,b: False)
        self.assertIsNone(choice)

    def test_localization_updates_target_not_odom(self):
        old = planar_transform((1,2,0.2),(4,5,0.5))
        new = planar_transform((1.2,2,0.2),(4,5,0.5))
        self.assertAlmostEqual(transform_point(new,(1.2,2))[0],4)
        self.assertAlmostEqual(transform_point(new,(1.2,2))[1],5)
        shift,_ = correction_size(old,new,[(1,2),(2,2)])
        self.assertAlmostEqual(shift,0.2)

    def test_rotations_near_robot_not_origin(self):
        old = planar_transform((10,0,0),(10,0,0))
        new = planar_transform((10,0,0.1),(10,0,0))
        shift,yaw = correction_size(old,new,[(10,0),(10.9,0)])
        self.assertLess(shift,0.1)
        self.assertAlmostEqual(yaw,0.1)

    def test_reject_degenerate_route(self):
        with self.assertRaises(ValueError):
            OrderedRoute([(1,1),(1,1)])


class NavigationWiringTests(unittest.TestCase):
    def test_manager_does_not_handle_velocities_or_collision_services(self):
        source = (ROOT/'src/scan_map_navigation/scripts/navigator.py').read_text()
        for token in ('desired_cmd','raw_cmd','safe_command','CheckPoses','wait_for_localization'):
            self.assertNotIn(token,source)
        tree = ast.parse(source)
        functions = {n.name:n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)}
        self.assertNotIn('clear_scan',ast.unparse(functions['publish_target']) if hasattr(ast,'unparse') else source[source.index('    def publish_target'):source.index('    def execute')])

    def test_launch_uses_rolling_targets(self):
        launch = ET.parse(str(ROOT/'src/scan_map_navigation/launch/scan_local.launch')).getroot()
        node = launch.find("node[@name='scan_local']")
        self.assertEqual(node.find("param[@name='fsm/navi_mode']").get('value'),'4')

    def test_snapshot_uses_one_stamp(self):
        nav = Navigator.__new__(Navigator)
        nav.tf = Mock()
        stamp = rospy.Time.from_sec(100)
        nav.tf.getLatestCommonTime.return_value = stamp
        nav.tf.lookupTransform.side_effect = [((1,2,0),(0,0,0,1)),((4,5,0.3),(0,0,0,1))]
        with patch('rospy.Time.now',return_value=stamp):
            pose,transform,height = nav.snapshot()
        self.assertEqual([c.args[2] for c in nav.tf.lookupTransform.call_args_list],[stamp,stamp])
        self.assertEqual(pose.header.stamp,stamp)
        self.assertEqual(transform,(3,3,0))
        self.assertEqual(height,0.3)

    def test_visibility_is_map_topology_not_footprint(self):
        nav = Navigator.__new__(Navigator)
        grid = nav.grid = OccupancyGrid()
        grid.header.frame_id = 'map'
        grid.info.resolution = 0.1
        grid.info.width = grid.info.height = 20
        grid.info.origin.orientation.w = 1
        grid.data = [0]*400
        self.assertTrue(nav.visible((0.1,0.1),(1,0.1)))
        grid.data[1*20+5] = 100
        self.assertFalse(nav.visible((0.1,0.1),(1,0.1)))


if __name__ == '__main__':
    unittest.main()
