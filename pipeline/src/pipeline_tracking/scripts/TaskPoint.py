#!/usr/bin/python
"""
Copyright (c) Deep Robotics Inc. - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Author: Haoyi Han <hanhaoyi@deeprobotics.cn>, Feb, 2020
"""
import time
from tf import transformations
from RobotCommander import RobotCommander
import rospy

import tf
import copy


class TaskPoint:
    """Property and method about a task point.

    Attributes:
        pose: the pose of robot in this wappoint.
        name: waypoint name.
    """

    def __init__(self, record=None):
        if not record:
            record = {
                "order": 0,
                "robot_pose": {
                    "pos_x": 0.0,
                    "pos_y": 0.0,
                    "pos_z": 0.0,
                    "ori_x": 0.0,
                    "ori_y": 0.0,
                    "ori_z": 0.0,
                    "ori_w": 1.0,
                },
                "option": {
                    "even_low_speed": False,
                    "even_medium_speed": False,
                    "uneven_high_step": False,
                },
            }
        self.pre_task_point = None
        self.record = copy.deepcopy(record)
        self.tf_listener = tf.TransformListener()
        self.Update()

    def SetPreTaskPoint(self, src_point):
        self.pre_task_point = src_point

    def GetPreTaskPoint(self):
        return self.pre_task_point.record["order"]

    def IsOrderEqual(self, num):
        return self.record["order"] == num

    def IsEvenLowSpeedGait(self):
        return self.record["option"]["even_low_speed"]

    def IsEvenMediumSpeedGait(self):
        return self.record["option"]["even_medium_speed"]

    def IsUnevenHighStepGait(self):
        return self.record["option"]["uneven_high_step"]

    def Update(self):
        self.robot_pose = self.record["robot_pose"]
        pose = []
        pose.append(self.robot_pose["pos_x"])
        pose.append(self.robot_pose["pos_y"])
        pose.append(self.robot_pose["pos_z"])
        pose.append(self.robot_pose["ori_x"])
        pose.append(self.robot_pose["ori_y"])
        pose.append(self.robot_pose["ori_z"])
        pose.append(self.robot_pose["ori_w"])
        self.posX = pose[0]
        self.posY = pose[1]
        self.yaw = transformations.euler_from_quaternion(pose[3:])[2]
        self.name = "waypoint_" + str(self.record["order"])

    def SetRobotPose(self, robot_pose):
        self.record["robot_pose"]["pos_x"] = robot_pose[0]
        self.record["robot_pose"]["pos_y"] = robot_pose[1]
        self.record["robot_pose"]["pos_z"] = robot_pose[2]
        self.record["robot_pose"]["ori_x"] = robot_pose[3]
        self.record["robot_pose"]["ori_y"] = robot_pose[4]
        self.record["robot_pose"]["ori_z"] = robot_pose[5]
        self.record["robot_pose"]["ori_w"] = robot_pose[6]
        self.Update()

    def GetPoseX(self):
        return self.posX

    def GetPoseY(self):
        return self.posY

    def GetYaw(self):
        return self.yaw

    def CalDistance(self, other):
        return (
            (self.GetPoseX() - other.GetPoseX()) ** 2
            + (self.GetPoseY() - other.GetPoseY()) ** 2
        ) ** 0.5
