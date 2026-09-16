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
from scan_map_navigation.msg import VelocityCommand, NavigationControl, PlannerState, LeaseRecovery
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
        self.previous_fault_reason = ''
        self.inputs = {}
        self.command = None
        self.command_time = None
        self.control = None
        self.control_time = None
        self.lease_hold = None
        self.lease_hold_ack = False
        self.lease_hold_started = 0.0
        self.recovery_id = 0
        self.task_lease_watchdog = rospy.get_param('~task_lease_watchdog',False)
        if type(self.task_lease_watchdog) is not bool:
            raise ValueError('task_lease_watchdog must be a boolean')
        self.lease_recovery_timeout = rospy.get_param('~lease_recovery_timeout', 2.0)
        if not math.isfinite(self.lease_recovery_timeout) or self.lease_recovery_timeout <= 0:
            raise ValueError('Invalid lease_recovery_timeout')
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
        self.lease_request = rospy.Publisher('/scan_map_nav/lease_recovery', LeaseRecovery, queue_size=1, latch=True)
        self.lease_request.publish(LeaseRecovery())
        self.last_fault = rospy.Publisher('/scan_map_nav/last_fault', String, queue_size=10, latch=True)
        self.last_fault.publish(String(''))
        self.timeout = rospy.get_param('~sensor_timeout', 0.7)
        self.planner_timeout = rospy.get_param('~planner_timeout', 3.0)
        if not math.isfinite(self.planner_timeout) or self.planner_timeout <= 0:
            raise ValueError('Invalid planner_timeout')
        self.localization_timeout = rospy.get_param('~localization_timeout', 1.2)
        if not math.isfinite(self.localization_timeout) or self.localization_timeout <= 0:
            raise ValueError('Invalid localization_timeout')
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
                                    ('planner','/scan_local/heartbeat',Bool),
                                    ('execution','/scan_map_nav/planner_state',PlannerState)]:
            rospy.Subscriber(topic, msgtype, self.receive, callback_args=key, queue_size=1)
        rospy.Subscriber('/scan_map_nav/desired_cmd', VelocityCommand, self.desired, queue_size=1)
        rospy.Subscriber('/scan_map_nav/control', NavigationControl, self.lease, queue_size=1)
        rospy.Subscriber('/scan_map_nav/lease_recovery_ack', LeaseRecovery, self.ack_recovery, queue_size=1)
        rospy.on_shutdown(self.shutdown)
        threading.Thread(target=self.audit_loop, daemon=True).start()

    def receive(self, msg, key):
        with self.lock:
            if key == 'execution':
                previous = self.inputs.get(key)
                if previous and msg.header.stamp < previous[0].header.stamp:
                    return
                revoked = (previous is not None and msg.generation != previous[0].generation)
                if revoked or msg.state in (PlannerState.RECOVERING,PlannerState.BLOCKED):
                    # Stop on receipt, not after a TF/service/next task loop.
                    self.output.publish(Twist())
                    self.allowed.publish(Bool(False))
            self.inputs[key] = (msg, time.monotonic())

    def desired(self, msg):
        with self.lock:
            self.command, self.command_time = msg, time.monotonic()

    def lease(self, msg):
        with self.lock:
            if self.control is not None and (msg.task_id < self.control.task_id or
                    (msg.task_id == self.control.task_id and msg.header.stamp < self.control.header.stamp)):
                return
            self.control, self.control_time = msg, time.monotonic()

    def ack_recovery(self, msg):
        with self.lock:
            hold = self.lease_hold
            if (hold is not None and (msg.recovery_id,msg.task_id,msg.epoch) ==
                    (hold.recovery_id,hold.task_id,hold.epoch) and
                    msg.header.stamp >= hold.header.stamp):
                self.lease_hold_ack = True

    def clear_lease_hold(self):
        self.lease_hold = None
        self.lease_hold_ack = False
        self.lease_request.publish(LeaseRecovery())

    def lease_watchdog(self):
        """Soft timeout latches STOP; renewal alone NEVER releases an old spline."""
        if not self.task_lease_watchdog:
            return ''
        lease = self.control
        hold = self.lease_hold
        if hold is not None and (lease is None or lease.task_id != hold.task_id or
                                 lease.epoch != hold.epoch or hold.epoch != self.command_epoch):
            self.clear_lease_hold()
            hold = None
        active = (lease is not None and lease.mode != NavigationControl.STOP and
                  lease.epoch == self.command_epoch)
        wall, now = time.monotonic(), rospy.Time.now().to_sec()
        expired = active and not fresh(self.control_time,lease.header.stamp.to_sec(),wall,now,0.5)
        if expired and hold is None:
            self.recovery_id += 1
            hold = LeaseRecovery(recovery_id=self.recovery_id,task_id=lease.task_id,epoch=lease.epoch)
            hold.header.stamp = rospy.Time.now()
            hold.header.frame_id = 'odom'
            status = self.inputs.get('execution')
            hold.generation = status[0].generation if status is not None else 0
            self.lease_hold,self.lease_hold_started,self.lease_hold_ack = hold,wall,False
            self.command = None
            self.output.publish(Twist())
            self.allowed.publish(Bool(False))
            self.lease_request.publish(hold)
            rospy.logwarn('Lease temporarily expired: stopping task %d, recovery %d',hold.task_id,hold.recovery_id)
        if hold is None:
            return ''
        # STOP (cancel, reset or global planning) remains stopped, never causes
        # movement or a timeout revocation of an already cancelled task.
        if active and wall-self.lease_hold_started >= self.lease_recovery_timeout:
            return 'Task lease recovery timed out; navigation loop unresponsive'
        status = self.inputs.get('execution')
        if (self.lease_hold_ack and status is not None and
                status[0].task_id == hold.task_id and status[0].epoch == hold.epoch and
                status[0].generation > hold.generation and
                fresh(status[1],status[0].header.stamp.to_sec(),wall,now,self.planner_timeout) and not expired):
            # Reset proof + explicit acknowledgement. State/command generation
            # checks below still require a checked NEW trajectory before moving.
            self.command = None
            self.clear_lease_hold()
        return ''

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
        # A localization timeout must not mask another, non-retryable fault.
        for key in ('cloud','odom','imu','planner','execution'):
            if key not in self.inputs:
                return 'Waiting for '+key
            msg, received = self.inputs[key]
            stamp = msg.header.stamp.to_sec() if hasattr(msg, 'header') else now
            limit = self.planner_timeout if key in ('planner','execution') else self.timeout
            if not fresh(received, stamp, wall, now, limit):
                return 'Stale '+key
        if 'ndt' not in self.inputs:
            return 'Waiting for ndt'
        status, ndt_received = self.inputs['ndt']
        if (not status.has_converged or not math.isfinite(status.matching_error) or
                status.matching_error > self.max_error or
                not math.isfinite(status.inlier_fraction) or status.inlier_fraction < self.min_inliers):
            return 'NDT quality below threshold'
        ndt_stamp = status.header.stamp.to_sec()
        if ndt_stamp <= 0 or now-ndt_stamp < -0.2:
            return 'Invalid ndt timestamp'
        if not self.inputs['planner'][0].data:
            return 'SCAN odometry not ready'
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
        if not fresh(ndt_received, ndt_stamp, wall, now, self.localization_timeout):
            return 'Stale ndt'
        return self.lease_watchdog()

    def refresh_health(self, reason):
        healthy = not reason
        # Report reason changes even while already stopped: a later cloud or
        # quality fault must veto a pending localization-only retry.
        if reason and reason != self.previous_fault_reason:
            self.last_fault.publish(String(reason))
        self.previous_fault_reason = reason
        if self.was_healthy and not healthy:
            # Revoke the running task's command epoch. Recovery is automatic,
            # but commands from the interrupted task must never become valid again.
            self.command_epoch = (self.command_epoch + 1) % (2**32)
            self.epoch_pub.publish(UInt32(self.command_epoch))
            rospy.logwarn('Task revoked: %s (epoch %d)',reason,self.command_epoch)
        if not healthy or not self.was_healthy:
            self.command = None
        if not healthy and self.lease_hold is not None:
            self.clear_lease_hold()
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
        if self.lease_hold is not None:
            return cmd, False, 'LEASE_RECOVERY: stopped, waiting for navigation reset'
        wall, now = time.monotonic(), rospy.Time.now().to_sec()
        stamp = lease.header.stamp.to_sec()
        if (lease.header.frame_id != 'odom' or lease.epoch != self.command_epoch or
                not lease.task_id or lease.mode not in (NavigationControl.TRACK,NavigationControl.ALIGN) or
                not math.isfinite(lease.yaw) or not math.isfinite(stamp) or stamp <= 0 or now-stamp < -0.2 or
                (self.task_lease_watchdog and not fresh(self.control_time,stamp,wall,now,0.5))):
            return cmd, False, 'Task lease invalid/expired'
        status = self.inputs['execution'][0]
        if (status.header.frame_id != 'odom' or status.task_id != lease.task_id or status.epoch != lease.epoch):
            return cmd, False, 'WAITING_FOR_PLANNER_STATE'
        if status.state == PlannerState.RECOVERING:
            return cmd, False, 'LOCAL_RECOVERY: '+status.reason
        if status.state == PlannerState.BLOCKED:
            return cmd, False, 'LOCAL_BLOCKED: '+status.reason
        required_state = PlannerState.TRACKING if lease.mode == NavigationControl.TRACK else PlannerState.ALIGNING
        if status.state != required_state:
            return cmd, False, 'WAITING_FOR_SAFE_TRAJECTORY'
        envelope = self.command
        if (not self.current_command(envelope) or envelope.task_id != lease.task_id or
                envelope.mode != lease.mode or envelope.generation != status.generation):
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
