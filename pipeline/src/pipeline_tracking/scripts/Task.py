#!/usr/bin/python

import os
import time
import json
import rospy
from TaskPoint import TaskPoint
from TaskTransfer import TaskTransfer
import numpy as np
import tf
from RobotCommander import RobotCommander

class Task:
    def __init__(self):
        self.tf_listener = tf.TransformListener()
        self.task_points = []
        self.src_index = 0
        self.des_index = 0
        self.ntask = 0
        self.robot_commander = RobotCommander()
        self.robot_transfer = TaskTransfer()

    def LoadTaskpoints(self):
        folder = str(os.path.dirname(os.path.abspath(__file__))) + "/../data"
        task_json = None
        if os.path.exists(folder):
            task_json = os.listdir(folder)

        if not task_json:
            raise Exception("No valid task point to tranverse!")

        task_list = []
        for i, file_name in enumerate(task_json):
            with open(folder + "/" + file_name, "r") as json_fp:
                waypoint_record = json.load(json_fp)
                task_list.append(waypoint_record)
        task_list = sorted(task_list, key=lambda s: s["order"])
        for waypoint_record in task_list:
            self.task_points.append(TaskPoint(waypoint_record))

    def GetInitialPose(self):
        self.initial_pose = None
        RATE = 50
        while not self.initial_pose:
            try:
                (pos, ori) = self.tf_listener.lookupTransform(
                    "/map", "/base_link", rospy.Duration(0.0)
                )
                msg_list = [pos[0], pos[1], pos[2], ori[0], ori[1], ori[2], ori[3]]
                self.initial_pose = msg_list
                rospy.sleep(1.0 / RATE)
            except tf.Exception as e:
                print("listen to tf failed")

    def GetBestTaskIndex(self):
        self.GetInitialPose()
        initial_task_point = TaskPoint()
        initial_task_point.SetRobotPose(self.initial_pose)
        dist_list = [initial_task_point.CalDistance(task_point) for task_point in self.task_points]
        return np.argmin(np.array(dist_list)), initial_task_point

    def Init(self):
        # load points
        self.LoadTaskpoints()
        nearest_index, initial_point = self.GetBestTaskIndex()

        # go to the nearest point
        self.robot_transfer.TaskTransfer(initial_point, self.task_points[nearest_index])

        # set next point
        self.ntask = self.task_points.__len__()
        self.src_index = nearest_index
        self.des_index = (nearest_index + 1) % self.ntask

    def Run(self):        
        while not rospy.is_shutdown():
            self.robot_commander.StartContinuousMotionGait()    
            time.sleep(0.5)

            self.robot_commander.SetZeroVelocity()
            time.sleep(0.5)

            # switch gait
            if(self.task_points[self.src_index].IsEvenLowSpeedGait()):
                self.robot_commander.SetEvenSlowSpeedGait()
            if(self.task_points[self.src_index].IsEvenMediumSpeedGait()):
                self.robot_commander.SetEvenMediumSpeedGait()
            if(self.task_points[self.src_index].IsUnevenHighStepGait()):
                self.robot_commander.SetUnevenHighStepGait()
            time.sleep(0.5)

            # switch point
            self.robot_transfer.TaskTransfer(
                self.task_points[self.src_index], self.task_points[self.des_index]
            )
            self.src_index = self.des_index
            self.des_index = (self.des_index + 1) % self.ntask
            time.sleep(0.5)

        self.robot_commander.StopContinuousMotionGait()

if __name__ == "__main__":
    rospy.init_node("autonomous_2d_navigation")
    task = Task()
    task.Init()
    task.Run()
