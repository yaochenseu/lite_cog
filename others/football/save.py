#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

# 初始化ROS节点
rospy.init_node('image_listener', anonymous=True)

# 创建一个CvBridge对象，用于ROS图像消息和OpenCV图像之间的转换
bridge = CvBridge()

# 标志，用于确保只保存一次图片
saved = False

# 定义一个回调函数，用于处理接收到的图像消息
def image_callback(data):
    global saved
    if not saved:
        try:
            # 将ROS图像消息转换为OpenCV图像
            cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
            
            # 保存图片
            cv2.imwrite('received_image.jpg', cv_image)
            rospy.loginfo("Saved image")
            saved = True  # 更新标志，表示图片已保存
            
        except CvBridgeError as e:
            print(e)

# 创建一个订阅者，订阅/camera/color/image_raw话题，回调函数为image_callback
image_sub = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)

# 循环等待回调函数，当按下Ctrl+C时退出
rospy.spin()

