#!/usr/bin/python3
import argparse
import math
import sys
import time
import yaml
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from scan_map_navigation.msg import NavigateAction, NavigateGoal


def main():
    parser = argparse.ArgumentParser(description='Navigate to a named map waypoint using SCAN.')
    parser.add_argument('name', nargs='?')
    parser.add_argument('--file', default='/home/ysc/lite_cog/system/map/waypoints.yaml')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--cancel', action='store_true')
    parser.add_argument('--any-yaw', action='store_true', help='Ignore saved final heading for this task')
    args = parser.parse_args()
    if args.list:
        with open(args.file) as stream:
            data = yaml.safe_load(stream)
        for name, wp in data['waypoints'].items():
            print('{}: ({:.3f}, {:.3f}), {}'.format(name,wp['position']['x'],wp['position']['y'],
                                                  wp.get('orientation_mode','fixed')))
        return 0
    if not args.cancel and not args.name:
        parser.error('Provide a waypoint name, --list, or --cancel')
    rospy.init_node('scan_goto', anonymous=True, disable_signals=True)
    client = actionlib.SimpleActionClient('/scan_map_nav/navigate',NavigateAction)
    if not client.wait_for_server(rospy.Duration(5)):
        print('SCAN navigation action unavailable; start ./start_nav.sh first.',file=sys.stderr)
        return 1
    if args.cancel:
        client.cancel_all_goals()
        time.sleep(0.3)
        print('Cancellation requested.')
        return 0
    with open(args.file) as stream:
        data = yaml.safe_load(stream)
    wp = data['waypoints'][args.name]
    goal = NavigateGoal()
    goal.target_pose.header.frame_id = data.get('frame_id','map')
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = float(wp['position']['x'])
    goal.target_pose.pose.position.y = float(wp['position']['y'])
    goal.require_yaw = not args.any_yaw and wp.get('orientation_mode','fixed') != 'any'
    q = wp.get('orientation')
    if goal.require_yaw:
        if q is None:
            raise ValueError('Fixed-yaw waypoint has no orientation')
        values = [float(q[k]) for k in ('x','y','z','w')]
        norm = math.sqrt(sum(v*v for v in values))
        if not math.isfinite(norm) or norm < 1e-6:
            raise ValueError('Invalid waypoint quaternion')
        target = goal.target_pose.pose.orientation
        target.x,target.y,target.z,target.w = [v/norm for v in values]
    else:
        goal.target_pose.pose.orientation.w = 1
    last = [None]
    def feedback(msg):
        if msg.state != last[0]:
            print('{}: {:.2f} m remaining'.format(msg.state,msg.distance_remaining),flush=True)
            last[0] = msg.state
    try:
        print('Going to {} ({})'.format(args.name,'fixed yaw' if goal.require_yaw else 'any yaw'))
        client.send_goal(goal,feedback_cb=feedback)
        while not client.wait_for_result(rospy.Duration(0.2)):
            pass
        result = client.get_result()
        print(result.message if result else 'No action result')
        return 0 if client.get_state() == GoalStatus.SUCCEEDED else 1
    except KeyboardInterrupt:
        client.cancel_goal()
        client.wait_for_result(rospy.Duration(2))
        print('Goal cancelled.')
        return 130


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyError,ValueError,OSError,yaml.YAMLError) as exc:
        print(str(exc),file=sys.stderr)
        sys.exit(2)
