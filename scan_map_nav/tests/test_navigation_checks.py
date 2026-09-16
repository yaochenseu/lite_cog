#!/usr/bin/python3
import ast
import math
import pathlib
import sys
import threading
import time
import unittest
import xml.etree.ElementTree as ET
import yaml
from unittest.mock import Mock, patch
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src/scan_map_navigation/scripts'))
import rospy
from nav_msgs.msg import Path, OccupancyGrid
from geometry_msgs.msg import PoseStamped
from navigator import Navigator
from rolling_route import OrderedRoute, planar_transform, transform_point, correction_size
from scan_map_navigation.msg import PlannerState, NavigationControl, LeaseRecovery
from navigator import TaskCancelled


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
    def plan_fixture(self):
        nav = Navigator.__new__(Navigator)
        nav.lookahead,nav.corner_cut = 0.9,0.12
        nav.path,nav.check_task = Mock(),Mock()
        start,goal = PoseStamped(),PoseStamped()
        start.header.frame_id = goal.header.frame_id = 'map'
        start.pose.orientation.w = goal.pose.orientation.w = 1
        goal.pose.position.x = 2.5
        path = Path()
        path.header.frame_id = 'map'
        path.poses = [start,goal]
        nav.plan = Mock()
        nav.call = Mock(return_value=Mock(plan=path))
        return nav,start,goal

    def test_active_navigation_builds_rolling_route(self):
        nav,start,goal=self.plan_fixture()
        route = nav.make_route(start,goal,200)
        self.assertIsInstance(route,OrderedRoute)
        first,_ = route.select((0,0))
        second,_ = route.select((0.4,0))
        self.assertAlmostEqual(first[0][0],0.9)
        self.assertAlmostEqual(second[0][0],1.3)
        self.assertEqual(nav.path.publish.call_args.args[0].header.frame_id,'map')

    def test_cancel_during_planning_never_commits_route(self):
        nav,start,goal=self.plan_fixture()
        nav.check_task.side_effect=[None,TaskCancelled()]
        with self.assertRaises(TaskCancelled):
            nav.make_route(start,goal,200)
        nav.path.publish.assert_not_called()

    def test_empty_or_wrong_frame_route_rejected(self):
        nav,start,goal=self.plan_fixture()
        nav.call.return_value.plan.header.frame_id='odom'
        with self.assertRaisesRegex(RuntimeError,'map frame'):
            nav.make_route(start,goal,200)
        nav.call.return_value.plan.header.frame_id='map'
        nav.call.return_value.plan.poses=[]
        with self.assertRaisesRegex(RuntimeError,'Invalid/empty'):
            nav.make_route(start,goal,200)
        nav.path.publish.assert_not_called()

    def test_latched_static_map_does_not_need_sensor_timestamps(self):
        nav=Navigator.__new__(Navigator)
        msg=OccupancyGrid()
        msg.header.frame_id='map'
        msg.header.stamp=rospy.Time.from_sec(1)
        msg.info.width=msg.info.height=20
        msg.info.resolution=.1
        msg.info.origin.orientation.w=1
        msg.data=[0]*400
        nav.grid=msg
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(10000)):
            self.assertTrue(nav.visible((.1,.1),(.9,.1)))
        msg.data[2*20+5]=100
        self.assertFalse(nav.visible((.1,.2),(.9,.2)))
        nav.grid=None
        self.assertFalse(nav.visible((.1,.1),(.9,.1)))

    def test_rolling_config_and_recovery_budgets_preserved(self):
        config = yaml.safe_load((ROOT/'src/scan_map_navigation/config/rolling.yaml').read_text())
        expected = dict(lookahead=2.0,corner_cut=0.12,target_step=0.08,target_period=0.05,
                        correction_step=0.08,stall_timeout=15.0,max_replans=2,
                        local_recovery_limit=4.0,local_retry_wait=0.2,lease_progress_timeout=0.3,
                        loop_period=0.05,
                        jump_confirm_frames=5,jump_confirm_time=.3,
                        jump_recover_frames=3,jump_recover_time=.15,jump_hold_timeout=2.,
                        guide_extension_failures=3,guide_extension_step=.5,
                        guide_extension_max_ahead=5.,guide_extension_motion=.2)
        for key,value in expected.items():
            self.assertEqual(config[key],value)
        for key in ('guide_spacing','guide_reach_radius','guide_progress_timeout',
                    'max_route_deviation','deviation_timeout','path_check_horizon',
                    'trial_stage_budget','trial_total_budget','trial_max_deviation','block_confirm_time',
                    'target_resend','target_near_distance','guide_extension_offsets'):
            self.assertNotIn(key,config)

    def test_recovery_visibility_allows_static_occupied_target_but_not_unknown_or_bounds(self):
        nav=Navigator.__new__(Navigator)
        grid=OccupancyGrid();grid.info.width=grid.info.height=20
        grid.header.frame_id='map'
        grid.info.resolution=.1;grid.info.origin.orientation.w=1
        grid.data=[0]*400;nav.grid=grid
        # Include an occupied goal cell, not just a wall on the connecting line.
        grid.data[2*20+5]=100;grid.data[2*20+9]=100
        self.assertFalse(nav.visible((.15,.25),(.95,.25)))
        self.assertTrue(nav.recovery_visible((.15,.25),(.95,.25)))
        grid.data[2*20+7]=-1
        self.assertFalse(nav.recovery_visible((.15,.25),(.95,.25)))
        self.assertFalse(nav.recovery_visible((.15,.25),(2.5,.25)))
        nav.grid=None
        self.assertFalse(nav.recovery_visible((.15,.25),(.95,.25)))

    def lease_nav(self):
        nav = Navigator.__new__(Navigator)
        nav.task_id,nav.task_epoch = 7,1
        nav.control_lock = threading.RLock()
        nav.control = Mock()
        nav.server = Mock()
        nav.server.is_preempt_requested.return_value = False
        nav.lease_progress_timeout = 0.3
        nav.task_lease_watchdog = True
        nav.control_intent = None
        nav.lease_recovery_done = 0
        return nav

    def test_independent_renewal_keeps_computation_stamp(self):
        nav = self.lease_nav()
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            nav.lease(NavigationControl.TRACK)
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100.2)):
            nav.renew_lease()
        self.assertEqual(nav.control.publish.call_count,2)
        self.assertEqual(nav.control.publish.call_args.args[0].header.stamp.to_sec(),100)

    def test_live_renewal_worker_does_not_mask_stalled_computation(self):
        nav = self.lease_nav()
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            nav.lease(NavigationControl.TRACK)
        nav.control_progress = time.monotonic()-0.31
        nav.renew_lease()
        self.assertEqual(nav.control.publish.call_count,1)

    def test_disabled_watchdog_renews_intent_without_faking_new_computation(self):
        nav = self.lease_nav()
        nav.task_lease_watchdog = False
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            nav.lease(NavigationControl.TRACK)
        nav.control_progress = time.monotonic()-5
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(105)):
            nav.renew_lease()
        self.assertEqual(nav.control.publish.call_count,2)
        self.assertEqual(nav.control.publish.call_args.args[0].header.stamp.to_sec(),100)
        nav.server.is_preempt_requested.return_value = True
        nav.renew_lease()
        self.assertEqual(nav.control.publish.call_count,2)
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(105)):
            nav.stop()
            nav.renew_lease()
        self.assertEqual(nav.control.publish.call_args.args[0].mode,NavigationControl.STOP)

    def test_disabled_watchdog_ignores_old_recovery_request(self):
        nav = self.lease_nav()
        nav.task_lease_watchdog = False
        nav.lease_request = LeaseRecovery(recovery_id=3,task_id=7,epoch=1)
        nav.clear_scan = Mock()
        self.assertFalse(nav.recover_lease(200))
        nav.clear_scan.assert_not_called()

    def test_launch_defaults_watchdog_off_and_forwards_one_switch(self):
        launch=ET.parse(str(ROOT/'src/scan_map_navigation/launch/navigation.launch')).getroot()
        self.assertEqual(launch.find("arg[@name='task_lease_watchdog']").get('default'),'false')
        for node in ('scan_navigator','scan_velocity_gate'):
            param=launch.find("node[@name='%s']/param[@name='task_lease_watchdog']"%node)
            self.assertEqual(param.get('value'),'$(arg task_lease_watchdog)')
            self.assertEqual(param.get('type'),'bool')
        includes=launch.findall('include')
        local_include=next(i for i in includes if i.get('file').endswith('/launch/scan_local.launch'))
        self.assertEqual(local_include.find("arg[@name='task_lease_watchdog']").get('value'),
                         '$(arg task_lease_watchdog)')
        local=ET.parse(str(ROOT/'src/scan_map_navigation/launch/scan_local.launch')).getroot()
        self.assertEqual(local.find("arg[@name='task_lease_watchdog']").get('default'),'false')
        param=local.find("param[@name='scan_controller/task_lease_watchdog']")
        self.assertEqual(param.get('value'),'$(arg task_lease_watchdog)')
        self.assertEqual(param.get('type'),'bool')

    def test_stop_replaces_worker_intent_and_cancel_cannot_rearm_it(self):
        nav = self.lease_nav()
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            nav.lease(NavigationControl.TRACK)
            nav.stop()
            nav.renew_lease()
            self.assertEqual(nav.control.publish.call_args.args[0].mode,NavigationControl.STOP)
            nav.server.is_preempt_requested.return_value = True
            with self.assertRaises(TaskCancelled):
                nav.lease(NavigationControl.TRACK)
        self.assertEqual(nav.control_intent.mode,NavigationControl.STOP)

    def test_planner_timeout_is_shared_by_gate_and_controller(self):
        launch=ET.parse(str(ROOT/'src/scan_map_navigation/launch/navigation.launch')).getroot()
        self.assertEqual(launch.find("arg[@name='planner_timeout']").get('default'),'3.0')
        p=launch.find("node[@name='scan_velocity_gate']/param[@name='planner_timeout']")
        self.assertEqual((p.get('value'),p.get('type')),('$(arg planner_timeout)','double'))
        inc=next(i for i in launch.findall('include') if i.get('file').endswith('/scan_local.launch'))
        self.assertEqual(inc.find("arg[@name='planner_timeout']").get('value'),'$(arg planner_timeout)')
        local=ET.parse(str(ROOT/'src/scan_map_navigation/launch/scan_local.launch')).getroot()
        self.assertEqual(local.find("arg[@name='planner_timeout']").get('default'),'3.0')
        p=local.find("param[@name='scan_controller/planner_timeout']")
        self.assertEqual((p.get('value'),p.get('type')),('$(arg planner_timeout)','double'))
        source=(ROOT/'src/scan_map_navigation/src/closed_loop_controller.cpp').read_text()
        self.assertIn('nh.param("planner_timeout", planner_timeout, 3.0)',source)
        self.assertIn('(ros::WallTime::now()-planner_received).toSec() > planner_timeout',source)
        self.assertIn('(ros::WallTime::now()-gate_received).toSec() > 0.15',source)

    def test_recovery_ack_follows_both_resets(self):
        nav = self.lease_nav()
        nav.lease_request = LeaseRecovery(recovery_id=3,task_id=7,epoch=1)
        nav.check_task,nav.state,nav.lease_ack = Mock(),Mock(),Mock()
        events = []
        nav.clear_scan = Mock(side_effect=lambda: events.append('reset'))
        nav.lease_ack.publish.side_effect = lambda m: events.append('ack')
        with patch('rospy.Time.now',return_value=rospy.Time.from_sec(100)):
            self.assertTrue(nav.recover_lease(200))
        self.assertEqual(events,['reset','ack'])
        self.assertFalse(nav.recover_lease(200))

    def test_failed_reset_never_acknowledges_recovery(self):
        nav = self.lease_nav()
        nav.lease_request = LeaseRecovery(recovery_id=3,task_id=7,epoch=1)
        nav.check_task,nav.state,nav.lease_ack = Mock(),Mock(),Mock()
        nav.clear_scan = Mock(side_effect=RuntimeError('reset failed'))
        with self.assertRaises(RuntimeError):
            nav.recover_lease(200)
        nav.lease_ack.publish.assert_not_called()

    def test_recovery_state_from_previous_reset_is_ignored(self):
        nav = Navigator.__new__(Navigator)
        nav.task_id,nav.task_epoch,nav.minimum_generation = 12,1,8
        nav.planner_status = PlannerState(task_id=12,epoch=1,generation=7,state=PlannerState.BLOCKED)
        self.assertIsNone(nav.local_state())
        nav.planner_status.generation = 8
        self.assertIsNotNone(nav.local_state())
        nav.planner_status.task_id = 11
        self.assertIsNone(nav.local_state())

    def test_local_recovery_uses_measured_velocity_without_speed_wait(self):
        source = (ROOT/'src/scan_map_navigation/src/scan_replan_fsm.cpp').read_text()
        body = source[source.index('void SCANReplanFSM::runLocalRecovery()'):source.index('bool SCANReplanFSM::validateLocalTrajectory()')]
        self.assertIn('start_vel_ = odom_vel_',body)
        self.assertNotIn('odom_vel_.norm() <',body)
        self.assertNotIn('callEmergencyStop',body)

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
        nav.localization_timeout=1.2
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

    def test_active_chain_is_static_without_runtime_map_dependency(self):
        source=(ROOT/'src/scan_map_navigation/scripts/navigator.py').read_text()
        gate=(ROOT/'src/scan_map_navigation/scripts/velocity_gate.py').read_text()
        self.assertIn("rospy.Subscriber('/map'",source)
        for code in (source,gate):
            self.assertNotIn('/scan_map_nav/planning_grid',code)
            self.assertNotIn('Runtime planning map',code)
        self.assertNotIn('AdaptiveLookahead',source)
        self.assertNotIn('AsyncPlan',source)
        launch=ET.parse(str(ROOT/'src/scan_map_navigation/launch/navigation.launch')).getroot()
        self.assertIsNone(launch.find("node[@type='runtime_map']"))
        config=yaml.safe_load((ROOT/'src/scan_map_navigation/config/global.yaml').read_text())
        self.assertEqual([v['type'] for v in config['global_costmap']['plugins']],
                         ['costmap_2d::StaticLayer','costmap_2d::InflationLayer'])
        self.assertEqual(config['global_costmap']['static_layer']['map_topic'],'/map')


if __name__ == '__main__':
    unittest.main()
