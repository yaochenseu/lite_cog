"""Read-only configuration checks; no ROS master or robot connection."""
import pathlib
import unittest
import xml.etree.ElementTree as ET
import yaml

PACKAGE = pathlib.Path(__file__).resolve().parents[1] / 'src/scan_map_navigation'


class InflationConfigTests(unittest.TestCase):
    def test_requested_global_radius_keeps_occupied_and_unknown_policy(self):
        config = yaml.safe_load((PACKAGE / 'config/global.yaml').read_text())
        costmap = config['global_costmap']
        self.assertEqual(costmap['inflation_layer']['inflation_radius'], 0.10)
        self.assertEqual(costmap['inflation_layer']['cost_scaling_factor'], 5.0)
        self.assertTrue(costmap['track_unknown_space'])
        self.assertFalse(config['GlobalPlanner']['allow_unknown'])
        self.assertEqual(config['GlobalPlanner']['lethal_cost'], 253)

    def test_global_footprint_not_shrunk(self):
        costmap = yaml.safe_load((PACKAGE / 'config/global.yaml').read_text())['global_costmap']
        self.assertEqual(costmap['footprint'],
                         [[-.53, -.35], [-.53, .35], [.53, .35], [.53, -.35]])
        self.assertEqual(costmap['footprint_padding'], 0.0)

    def test_scan_local_body_dimensions_not_shrunk(self):
        launch = ET.parse(str(PACKAGE / 'launch/scan_local.launch')).getroot()
        node = launch.find("node[@name='scan_local']")
        for name, value in [('grid_map/double_cylinder_radius', .35),
                            ('grid_map/double_cylinder_offset', .18)]:
            self.assertEqual(float(node.find("param[@name='%s']" % name).get('value')), value)


if __name__ == '__main__':
    unittest.main()
