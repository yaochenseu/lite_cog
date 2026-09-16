"""Historical runtime-map navigator tests; not part of static rollback tests.

Requires the pre-rollback Navigator from the saved archive. The active static
navigator intentionally has no background route replacement.

No ROS master, no hardware publishers: mocked transport, real execution loop,
real async worker, real permission/preemption functions and route acceptance.
"""
import copy
import pathlib
import sys
import threading
import time
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'src/scan_map_navigation/scripts'))
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
from scan_map_navigation.msg import NavigateGoal,NavigationControl,PlannerState
from navigator import Navigator,TaskCancelled
from planning_grid import AdaptiveLookahead
from test_adaptive_navigation import grid


class AsyncExecutionTests(unittest.TestCase):
    def exercise(self,cancel_during_request):
        nav=Navigator.__new__(Navigator)
        for key,value in dict(poisoned=False,command_epoch=0,task_id=0,task_epoch=0,
                task_timeout=10,xy_tolerance=.15,yaw_tolerance=.12,lookahead=.9,corner_cut=.12,
                trial_stage_budget=10,trial_total_budget=30,trial_restore_time=1.5,
                block_confirm_time=1,path_check_horizon=2,progress_timeout=3,stall_timeout=15,
                jump_distance=.8,jump_yaw=.5,service_timeout=2,replan_interval=.1,max_replans=2,
                trial_max_deviation=2,local_recovery_limit=4,target_period=.3,target_step=.18,
                correction_step=.08,test_stalled=False,pending_plan=None,control_intent=None).items():
            setattr(nav,key,value)
        nav.control_lock=threading.RLock()
        nav.control,nav.state,nav.target,nav.target_marker,nav.path,nav.server=[Mock() for _ in range(6)]
        cancelled,trigger,entered,release=[threading.Event() for _ in range(4)]
        nav.server.is_preempt_requested.side_effect=cancelled.is_set
        nav.server.is_active.return_value=True
        def check(deadline):
            if cancelled.is_set(): raise TaskCancelled()
        nav.check_task=check
        nav.clear_scan=Mock()
        nav.recover_lease=Mock(return_value=False)
        robot=PoseStamped(); robot.header.frame_id='map'; robot.pose.orientation.w=1
        goal=copy.deepcopy(robot); goal.pose.position.x=2.5
        nav.snapshot=lambda: (robot,(0,0,0),.327)
        view=grid(); nav.map_snapshot=lambda: view
        nav.local_state=lambda: PlannerState(task_id=nav.task_id,epoch=0,generation=1,state=PlannerState.TRACKING)
        def target(msg):
            if not entered.is_set(): trigger.set()
        nav.target.publish.side_effect=target
        calls=[]
        def plan(start,end,tolerance):
            calls.append((start,end))
            if len(calls)>1:
                entered.set()
                release.wait(1.5)
                trigger.clear()
            path=Path(); path.header.frame_id='map'; path.poses=[copy.deepcopy(start),copy.deepcopy(end)]
            return Mock(plan=path)
        nav.plan=plan
        # Fault injection at the policy boundary requests a global replacement
        # while a previously checked trajectory is still TRACKING. Selection,
        # async dispatch, lease renewal and acceptance are the real code.
        original=AdaptiveLookahead.exhausted
        with patch('rospy.Time.now',side_effect=lambda: rospy.Time.from_sec(time.time())), \
             patch('rospy.is_shutdown',return_value=False), \
             patch.object(AdaptiveLookahead,'exhausted',lambda obj,now: trigger.is_set() or original(obj,now)):
            runner=threading.Thread(target=nav.execute,args=(NavigateGoal(goal,False),))
            runner.start()
            try:
                self.assertTrue(entered.wait(3),'Background replan not entered')
                start_count=nav.control.publish.call_count
                time.sleep(.25)
                messages=[c.args[0] for c in nav.control.publish.call_args_list[start_count:]]
                self.assertGreaterEqual(len(messages),2)
                self.assertTrue(all(m.mode==NavigationControl.TRACK for m in messages))
                self.assertEqual(nav.clear_scan.call_count,1,'Background planning reset a checked trajectory')
                self.assertEqual(nav.path.publish.call_count,1,'Unfinished candidate was committed')
                task=nav.task_id
                if cancel_during_request:
                    cancelled.set()
                    runner.join(2)
                    self.assertFalse(runner.is_alive())
                    release.set()
                    self.assertTrue(nav.pending_plan.done.wait(1))
                    self.assertEqual(nav.path.publish.call_count,1,'Cancelled worker committed a late route')
                    self.assertEqual(nav.control.publish.call_args.args[0].mode,NavigationControl.STOP)
                    nav.server.set_preempted.assert_called_once()
                else:
                    release.set()
                    deadline=time.monotonic()+2
                    while nav.path.publish.call_count<2 and time.monotonic()<deadline:
                        time.sleep(.02)
                    self.assertEqual(nav.path.publish.call_count,2)
                    self.assertEqual(nav.task_id,task)
                    self.assertEqual(nav.clear_scan.call_count,1)
                    self.assertEqual(nav.control.publish.call_args.args[0].mode,NavigationControl.TRACK)
            finally:
                release.set(); cancelled.set(); runner.join(3)
                self.assertFalse(runner.is_alive())

    def test_background_replan_preserves_tracking_and_commits_without_reset(self):
        self.exercise(False)

    def test_cancel_during_background_planning_rejects_late_result(self):
        self.exercise(True)


if __name__=='__main__': unittest.main()
