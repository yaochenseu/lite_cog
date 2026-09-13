#!/usr/bin/python3
"""Automatic health-based velocity output with a wall-clock watchdog."""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import threading
import time
import rospy
import rosgraph
from geometry_msgs.msg import Twist
from scan_map_navigation.msg import VelocityCommand, NavigationControl
from sensor_msgs.msg import PointCloud2, Imu
from nav_msgs.msg import Odometry
from hdl_localization.msg import ScanMatchingStatus
from std_msgs.msg import Bool, String, UInt32
from nav_math import fresh


class Gate:
    def __init__(self):
        self.lock = threading.RLock()
        self.was_healthy = False
        self.command_epoch = 0
        self.inputs = {}
        self.command = None
        self.command_time = None
        self.control = None
        self.control_time = None
        self.conflict = 'Checking velocity publishers'
        self.master = rosgraph.Master(rospy.get_name())
        self.output_topic = rospy.get_param('~output_topic', '/cmd_vel')
        self.output = rospy.Publisher(self.output_topic, Twist, queue_size=1)
        self.epoch_pub = rospy.Publisher('/scan_map_nav/command_epoch', UInt32, queue_size=1, latch=True)
        self.epoch_pub.publish(UInt32(self.command_epoch))
        self.preview = rospy.Publisher('/scan_map_nav/cmd_vel_preview', Twist, queue_size=1)
        self.ready = rospy.Publisher('/scan_map_nav/ready', Bool, queue_size=1)
        self.state = rospy.Publisher('/scan_map_nav/gate_state', String, queue_size=1, latch=True)
        self.allowed = rospy.Publisher('/scan_map_nav/execution_allowed', Bool, queue_size=1)
        self.timeout = rospy.get_param('~sensor_timeout', 0.7)
        self.min_inliers = rospy.get_param('~min_inlier_fraction', 0.5)
        self.max_error = rospy.get_param('~max_matching_error', 0.3)
        self.vx = rospy.get_param('~max_vx', 0.35)
        self.vy = rospy.get_param('~max_vy', 0.25)
        self.wz = rospy.get_param('~max_wz', 0.8)
        self.reverse = rospy.get_param('~max_reverse_vx', 0.18)
        for key, topic, msgtype in [('cloud','/rslidar_points',PointCloud2),
                                    ('odom','/leg_odom2',Odometry),
                                    ('imu','/imu/data',Imu),
                                    ('ndt','/status',ScanMatchingStatus),
                                    ('planner','/scan_local/heartbeat',Bool)]:
            rospy.Subscriber(topic, msgtype, self.receive, callback_args=key, queue_size=1)
        rospy.Subscriber('/scan_map_nav/desired_cmd', VelocityCommand, self.desired, queue_size=1)
        rospy.Subscriber('/scan_map_nav/control', NavigationControl, self.lease, queue_size=1)
        rospy.on_shutdown(self.shutdown)
        threading.Thread(target=self.audit_loop, daemon=True).start()

    def receive(self, msg, key):
        with self.lock:
            self.inputs[key] = (msg, time.monotonic())

    def desired(self, msg):
        with self.lock:
            self.command, self.command_time = msg, time.monotonic()

    def lease(self, msg):
        with self.lock:
            self.control, self.control_time = msg, time.monotonic()

    def audit_loop(self):
        while not rospy.is_shutdown():
            try:
                pubs, _, _ = self.master.getSystemState()
                forbidden = []
                for topic, nodes in pubs:
                    if topic in (self.output_topic, '/cmd_vel_corrected'):
                        forbidden.extend(n for n in nodes if n != rospy.get_name())
                value = 'Other velocity publishers: '+', '.join(sorted(set(forbidden))) if forbidden else ''
            except Exception as exc:
                value = 'Cannot audit ROS publishers: '+str(exc)
            with self.lock:
                self.conflict = value
            time.sleep(1.0)

    def healthy(self):
        if self.conflict:
            return self.conflict
        wall, now = time.monotonic(), rospy.Time.now().to_sec()
        lease = self.control
        if (lease is not None and lease.mode != NavigationControl.STOP and
                lease.epoch == self.command_epoch and
                not fresh(self.control_time,lease.header.stamp.to_sec(),wall,now,0.5)):
            return 'Task lease expired'
        for key in ('cloud','odom','imu','ndt','planner'):
            if key not in self.inputs:
                return 'Waiting for '+key
            msg, received = self.inputs[key]
            stamp = msg.header.stamp.to_sec() if hasattr(msg, 'header') else now
            if not fresh(received, stamp, wall, now, self.timeout):
                return 'Stale '+key
        status = self.inputs['ndt'][0]
        if (not status.has_converged or not math.isfinite(status.matching_error) or
                status.matching_error > self.max_error or
                not math.isfinite(status.inlier_fraction) or status.inlier_fraction < self.min_inliers):
            return 'NDT quality below threshold'
        if not self.inputs['planner'][0].data:
            return 'SCAN emergency/not ready'
        cloud = self.inputs['cloud'][0]
        if cloud.width*cloud.height == 0 or not {'x','y','z'}.issubset({f.name for f in cloud.fields}):
            return 'Empty/invalid point cloud'
        odom = self.inputs['odom'][0]
        q = odom.pose.pose.orientation
        p = odom.pose.pose.position
        if (odom.header.frame_id != 'odom' or odom.child_frame_id != 'base_link' or
                not all(math.isfinite(v) for v in (p.x,p.y,p.z,q.x,q.y,q.z,q.w)) or
                abs(sum(v*v for v in (q.x,q.y,q.z,q.w))-1) > 0.1):
            return 'Invalid body odom frame/pose'
        return ''

    def refresh_health(self, reason):
        healthy = not reason
        if self.was_healthy and not healthy:
            # Revoke the running task's command epoch. Recovery is automatic,
            # but commands from the interrupted task must never become valid again.
            self.command_epoch = (self.command_epoch + 1) % (2**32)
            self.epoch_pub.publish(UInt32(self.command_epoch))
        if not healthy or not self.was_healthy:
            self.command = None
        self.was_healthy = healthy
        return healthy

    def current_command(self, message):
        return message is not None and message.epoch == self.command_epoch

    def select_command(self, ready):
        """Constant-time arbitration; no TF, planning or collision service calls."""
        cmd = Twist()
        if not ready:
            return cmd, False, ''
        lease = self.control
        if lease is None or lease.mode == NavigationControl.STOP:
            return cmd, False, 'IDLE'
        wall, now = time.monotonic(), rospy.Time.now().to_sec()
        if (lease.header.frame_id != 'odom' or lease.epoch != self.command_epoch or
                not lease.task_id or lease.mode not in (NavigationControl.TRACK,NavigationControl.ALIGN) or
                not math.isfinite(lease.yaw) or
                not fresh(self.control_time,lease.header.stamp.to_sec(),wall,now,0.5)):
            return cmd, False, 'Task lease invalid/expired'
        envelope = self.command
        if (not self.current_command(envelope) or envelope.task_id != lease.task_id or
                envelope.mode != lease.mode):
            return cmd, False, 'WAITING_FOR_CONTROLLER'
        message = envelope.command
        if (message.header.frame_id != 'base_link' or
                not fresh(self.command_time,message.header.stamp.to_sec(),wall,now,0.25)):
            return cmd, False, 'Controller command expired'
        values = message.twist.linear.x,message.twist.linear.y,message.twist.angular.z
        if not all(math.isfinite(v) for v in values):
            return cmd, False, 'Invalid controller command'
        cmd.linear.x = max(-self.reverse,min(self.vx,values[0]))
        cmd.linear.y = max(-self.vy,min(self.vy,values[1]))
        cmd.angular.z = max(-self.wz,min(self.wz,values[2]))
        return cmd, True, 'READY'

    def shutdown(self):
        for _ in range(3):
            self.output.publish(Twist())

    def run(self):
        while not rospy.is_shutdown():
            with self.lock:
                reason = self.healthy()
                ready = self.refresh_health(reason)
                cmd, allowed, execution_state = self.select_command(ready)
                self.preview.publish(cmd)
                self.output.publish(cmd)
                self.allowed.publish(Bool(allowed))
                self.ready.publish(Bool(ready))
                self.state.publish(String(reason or execution_state))
            time.sleep(0.02)


if __name__ == '__main__':
    rospy.init_node('scan_velocity_gate')
    Gate().run()
