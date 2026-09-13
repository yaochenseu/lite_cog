#!/usr/bin/env python3

import argparse
import math
import os
import sys

import actionlib
import rospy
import tf
import yaml
from actionlib_msgs.msg import GoalStatus
from dynamic_reconfigure.client import Client as DynamicReconfigureClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


WAYPOINT_FILE = "/home/ysc/lite_cog/system/map/waypoints.yaml"
MOVE_BASE_ACTION = "/move_base"
TEB_CONFIG_SERVER = "/move_base/TebLocalPlannerROS"
DEFAULT_BASE_FRAME = "base_link"
ANY_YAW_TOLERANCE = math.pi


def load_waypoints():
    with open(WAYPOINT_FILE, "r", encoding="utf-8") as stream:
        document = yaml.safe_load(stream) or {}

    waypoints = document.get("waypoints")
    if not isinstance(waypoints, dict):
        raise RuntimeError("waypoints.yaml does not contain a 'waypoints' mapping")

    return document.get("frame_id", "map"), waypoints


def print_waypoints(waypoints):
    for name, waypoint in waypoints.items():
        position = waypoint.get("position", {})
        mode = waypoint.get("orientation_mode", "fixed")
        print(
            "{:<16} x={:>8.3f}  y={:>8.3f}  orientation={}".format(
                name,
                float(position.get("x", 0.0)),
                float(position.get("y", 0.0)),
                mode,
            )
        )


def normalized_orientation(orientation):
    values = [float(orientation.get(key, 0.0)) for key in ("x", "y", "z", "w")]
    norm = math.sqrt(sum(value * value for value in values))
    if norm < 1.0e-9:
        raise RuntimeError("waypoint contains an invalid zero-length quaternion")
    return tuple(value / norm for value in values)


def current_planar_orientation(frame_id):
    listener = tf.TransformListener()
    listener.waitForTransform(frame_id, DEFAULT_BASE_FRAME, rospy.Time(0), rospy.Duration(3.0))
    _, rotation = listener.lookupTransform(frame_id, DEFAULT_BASE_FRAME, rospy.Time(0))
    yaw = tf.transformations.euler_from_quaternion(rotation)[2]
    quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, yaw)
    return quaternion, yaw


def build_goal(frame_id, waypoint):
    position = waypoint.get("position")
    if not isinstance(position, dict):
        raise RuntimeError("waypoint does not contain a position")

    mode = waypoint.get("orientation_mode", "fixed")
    if mode == "fixed":
        orientation = waypoint.get("orientation")
        if not isinstance(orientation, dict):
            raise RuntimeError("fixed-orientation waypoint has no orientation")
        quaternion = normalized_orientation(orientation)
        yaw_description = "fixed"
    elif mode == "any":
        try:
            quaternion, yaw = current_planar_orientation(frame_id)
            yaw_description = "any (placeholder uses current yaw {:.1f} deg)".format(
                math.degrees(yaw)
            )
        except (tf.Exception, tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            quaternion = (0.0, 0.0, 0.0, 1.0)
            yaw_description = "any (TF unavailable; placeholder uses 0 deg)"
    else:
        raise RuntimeError("unsupported orientation_mode: {}".format(mode))

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = frame_id
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = float(position["x"])
    goal.target_pose.pose.position.y = float(position["y"])
    # Navigation is two-dimensional even if Publish Point returned a small z value.
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.x = quaternion[0]
    goal.target_pose.pose.orientation.y = quaternion[1]
    goal.target_pose.pose.orientation.z = quaternion[2]
    goal.target_pose.pose.orientation.w = quaternion[3]
    return goal, mode, yaw_description


def main():
    parser = argparse.ArgumentParser(description="Navigate to a named Lite3 waypoint")
    parser.add_argument("waypoint", nargs="?", help="waypoint name, for example: hall")
    parser.add_argument("--list", action="store_true", help="list saved waypoints")
    parser.add_argument("--cancel", action="store_true", help="cancel all move_base goals")
    args = parser.parse_args()

    try:
        frame_id, waypoints = load_waypoints()
    except (OSError, yaml.YAMLError, RuntimeError) as error:
        print("Error loading {}: {}".format(WAYPOINT_FILE, error), file=sys.stderr)
        return 2

    if args.list:
        print_waypoints(waypoints)
        return 0

    if not args.waypoint and not args.cancel:
        parser.error("provide a waypoint name, --list, or --cancel")

    rospy.init_node("goto_waypoint", anonymous=True)
    move_base = actionlib.SimpleActionClient(MOVE_BASE_ACTION, MoveBaseAction)
    print("Waiting for {}...".format(MOVE_BASE_ACTION))
    if not move_base.wait_for_server(rospy.Duration(10.0)):
        print("Error: /move_base action server is not available", file=sys.stderr)
        return 3

    if args.cancel:
        move_base.cancel_all_goals()
        rospy.sleep(0.2)
        print("All move_base goals cancelled.")
        return 0

    if args.waypoint not in waypoints:
        print("Unknown waypoint: {}".format(args.waypoint), file=sys.stderr)
        print("Available waypoints:", file=sys.stderr)
        print_waypoints(waypoints)
        return 2

    try:
        goal, orientation_mode, yaw_description = build_goal(
            frame_id, waypoints[args.waypoint]
        )
    except (KeyError, TypeError, ValueError, RuntimeError) as error:
        print("Invalid waypoint '{}': {}".format(args.waypoint, error), file=sys.stderr)
        return 2

    teb_client = None
    previous_yaw_tolerance = None

    try:
        if orientation_mode == "any":
            try:
                teb_client = DynamicReconfigureClient(TEB_CONFIG_SERVER, timeout=5.0)
                configuration = teb_client.get_configuration(timeout=5.0)
                previous_yaw_tolerance = float(configuration["yaw_goal_tolerance"])
                teb_client.update_configuration(
                    {"yaw_goal_tolerance": ANY_YAW_TOLERANCE}
                )
                print(
                    "Final orientation is unrestricted; yaw tolerance temporarily set to pi."
                )
            except Exception as error:
                print(
                    "Error: unable to configure unrestricted final orientation: {}".format(
                        error
                    ),
                    file=sys.stderr,
                )
                return 4

        position = goal.target_pose.pose.position
        print(
            "Sending '{}' to x={:.3f}, y={:.3f}, orientation={}.".format(
                args.waypoint, position.x, position.y, yaw_description
            )
        )
        move_base.send_goal(goal)
        move_base.wait_for_result()
        state = move_base.get_state()
        status_text = move_base.get_goal_status_text()

        if state == GoalStatus.SUCCEEDED:
            print("Arrived at '{}'.".format(args.waypoint))
            return 0

        print(
            "Navigation to '{}' ended with state {}: {}".format(
                args.waypoint, state, status_text
            ),
            file=sys.stderr,
        )
        return 5
    except rospy.ROSInterruptException:
        move_base.cancel_goal()
        print("Navigation interrupted; goal cancelled.", file=sys.stderr)
        return 130
    finally:
        if teb_client is not None and previous_yaw_tolerance is not None:
            try:
                teb_client.update_configuration(
                    {"yaw_goal_tolerance": previous_yaw_tolerance}
                )
                print(
                    "Restored yaw_goal_tolerance to {:.3f}.".format(
                        previous_yaw_tolerance
                    )
                )
            except Exception as error:
                print(
                    "Warning: failed to restore yaw_goal_tolerance: {}".format(error),
                    file=sys.stderr,
                )


if __name__ == "__main__":
    sys.exit(main())
