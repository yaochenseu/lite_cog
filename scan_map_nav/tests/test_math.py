#!/usr/bin/python3
import math
import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
from nav_math import angle, fresh, integrate, thin_points


class GeometryTests(unittest.TestCase):
    def test_body_velocity_transform(self):
        x,y,yaw = integrate(0,0,math.pi/2,1,0,0,2)
        self.assertAlmostEqual(x,0)
        self.assertAlmostEqual(y,2)

    def test_rotation_arc(self):
        x,y,yaw = integrate(0,0,0,1,0,1,math.pi/2)
        self.assertAlmostEqual(x,1)
        self.assertAlmostEqual(y,1)
        self.assertAlmostEqual(yaw,math.pi/2)

    def test_corner_and_endpoint_retained(self):
        points = [(i/10,0) for i in range(11)] + [(1,i/10) for i in range(1,11)]
        output = thin_points(points)
        self.assertIn((1,0),output)
        self.assertEqual(output[-1],(1,1))
        self.assertLess(len(output),len(points))

    def test_repeated_points(self):
        self.assertEqual(thin_points([(0,0)]*5),[(0,0)])
        self.assertEqual(thin_points([]),[])

    def test_watchdog_wall_and_ros(self):
        self.assertTrue(fresh(1,100,1.1,100.1,0.5))
        self.assertFalse(fresh(1,100,2,100,0.5))  # /clock paused
        self.assertFalse(fresh(1,99,1.1,100,0.5))  # stale stamped message
        self.assertFalse(fresh(1,110,1.1,100,0.5))  # future timestamp
        self.assertFalse(fresh(None,100,1.1,100,0.5))

    def test_wrap(self):
        self.assertAlmostEqual(angle(2*math.pi+0.1),0.1)


if __name__ == '__main__':
    unittest.main()
