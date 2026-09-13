#!/usr/bin/python

import rospy
import actionlib
from tf.transformations import *
from pipeline.msg import MoveBaseAction, MoveBaseGoal

class TaskTransfer:
    def __init__(self):
        self.moveBaseClient = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.moveBaseClient.wait_for_server()
        rospy.loginfo("Action 'move_base' is up!")

    def IsPlanFailed(self):
        return self.moveBaseClient.get_state() == actionlib.GoalStatus.ABORTED
    
    def IsActionSucceeded(self):
        return self.moveBaseClient.get_state() == actionlib.GoalStatus.SUCCEEDED

    def TaskTransfer(self, src_point, des_point):
        des_point.SetPreTaskPoint(src_point)
        goal_msg = MoveBaseGoal()
        goal_msg.target_pose.header.stamp = rospy.Time.now()
        goal_msg.target_pose.header.frame_id = "map"
        goal_msg.target_pose.pose.position.x = des_point.GetPoseX()
        goal_msg.target_pose.pose.position.y = des_point.GetPoseY()
        goal_msg.target_pose.pose.position.z = 0
        my_q = quaternion_from_euler(0, 0, des_point.GetYaw())
        goal_msg.target_pose.pose.orientation.x = my_q[0]
        goal_msg.target_pose.pose.orientation.y = my_q[1]
        goal_msg.target_pose.pose.orientation.z = my_q[2]
        goal_msg.target_pose.pose.orientation.w = my_q[3]

        not_done = True
        while not_done and not rospy.is_shutdown():
            self.moveBaseClient.send_goal(goal_msg)
            rospy.logwarn(
                "Transfer from [%s] to [%s]" % (src_point.name, des_point.name)
            )

            done = self.moveBaseClient.wait_for_result(timeout=rospy.Duration(5.0))
            not_done = (not done) or (
                self.moveBaseClient.get_state() != actionlib.GoalStatus.SUCCEEDED
            )
