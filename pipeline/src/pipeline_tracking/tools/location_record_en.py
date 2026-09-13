#!/usr/bin/python

from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QRadioButton
)
from PyQt5.QtGui import QIntValidator

import sys
import rospy
import json
import os
import tf
import signal
import sys

break_flag = False
def signal_handler(sig, frame):
    global break_flag
    break_flag = True
    sys.exit(0)

class LocationRecorder(QWidget):
    def __init__(self):
        super(LocationRecorder, self).__init__()
        self.InitUI()
        self.robot_record_pose = None
        self.option = None
        self.tf_listener = tf.TransformListener()
        self.show()

    def InitUI(self):
        self.setWindowTitle('DR Location Recorder')

        self.layout = QVBoxLayout()
        self.option_layout = QHBoxLayout()
        self.even_low_speed_radio_button = QRadioButton('even slow gait')
        self.option_layout.addWidget(self.even_low_speed_radio_button)
        self.even_medium_speed_radio_button = QRadioButton('even medium gait')
        self.option_layout.addWidget(self.even_medium_speed_radio_button)
        self.uneven_high_step_radio_button = QRadioButton("uneven high step gait")
        self.option_layout.addWidget(self.uneven_high_step_radio_button)

        self.order_layout = QHBoxLayout()
        self.order_layout.addWidget(QLabel("location number:"))
        self.order_edit = QLineEdit("")
        self.order_edit.setValidator(QIntValidator())
        self.order_layout.addWidget(self.order_edit)

        self.text_content = QTextEdit()
        self.text_content.setReadOnly(True)
        self.even_low_speed_radio_button.setChecked(True)

        self.record_layout = QHBoxLayout()
        self.receive_button = QPushButton("get location")
        self.record_layout.addWidget(self.receive_button)
        self.record_button = QPushButton("record location")
        self.record_layout.addWidget(self.record_button)

        self.layout.addLayout(self.option_layout)
        self.layout.addLayout(self.order_layout)
        self.layout.addWidget(self.text_content)
        self.layout.addLayout(self.record_layout)
        self.setLayout(self.layout)

        self.receive_button.clicked.connect(self.Receive)
        self.record_button.clicked.connect(self.Record)

    def ListenTF(self):
        try:
            (pos, ori) = self.tf_listener.lookupTransform(
                "map", "base_link", rospy.Duration(0.0)
            )
            msg_dict = {
                "pos_x": pos[0],
                "pos_y": pos[1],
                "pos_z": pos[2],
                "ori_x": ori[0],
                "ori_y": ori[1],
                "ori_z": ori[2],
                "ori_w": ori[3],
            }
            self.robot_record_pose = msg_dict
            return True
        except tf.Exception as e:
            print ("listen to tf failed")
            return False

    def UpdateOption(self):
        self.option = {}
        self.option["even_low_speed"] = self.even_low_speed_radio_button.isChecked()
        self.option["even_medium_speed"] = self.even_medium_speed_radio_button.isChecked()
        self.option["uneven_high_step"] = self.uneven_high_step_radio_button.isChecked()

    def Receive(self):
        while not self.ListenTF():
            global break_flag
            if break_flag:
                break
            rospy.sleep(1.0)
        self.UpdateOption()
        display_msg = "Robot:\n" + json.dumps(self.robot_record_pose, indent=4) + "\n"
        display_msg += "Option:\n" + json.dumps(self.option, indent=4) + "\n"
        self.text_content.setText(display_msg)

    def Record(self):
        order = self.order_edit.text()
        order = int(order)
        new_record = {
            "order": order,
            "robot_pose": self.robot_record_pose,
            "option": self.option,
        }
        data_dir = str(os.path.dirname(os.path.abspath(__file__))) + "/../data"
        os.system("mkdir -p " + data_dir)
        data_dir = data_dir + "/" + str(order) + ".json"
        with open(data_dir, "w+") as out:
            json.dump(new_record, out, indent=4)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    app = QApplication(sys.argv)
    rospy.init_node("location_recorder")
    lr = LocationRecorder()
    sys.exit(app.exec_())

