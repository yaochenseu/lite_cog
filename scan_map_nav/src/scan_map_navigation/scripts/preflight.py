#!/usr/bin/python3
"""Read-only startup checks. Never kills existing ROS nodes."""
import sys
import rosgraph

try:
    pubs,subs,services = rosgraph.Master('/scan_map_nav_preflight').getSystemState()
    pub = dict(pubs)
    conflicts = set(pub.get('/cmd_vel', []) + pub.get('/cmd_vel_corrected', []) + pub.get('/map', []))
    nodes = set(n for _,names in pubs+subs+services for n in names)
    conflicts |= nodes.intersection({'/move_base','/scan_planner_node','/closed_loop_controller',
                                    '/scan_navigator','/hdl_localization_nodelet'})
    if conflicts:
        raise RuntimeError('Stop the old navigation/localization first: '+', '.join(sorted(conflicts)))
    missing = [t for t in ('/rslidar_points','/imu/data','/leg_odom2') if not pub.get(t)]
    if missing:
        raise RuntimeError('Missing publishers: '+', '.join(missing))
    print('Preflight passed. Motion is available automatically when inputs are healthy; no goal is sent automatically.')
except Exception as exc:
    print('Preflight failed: '+str(exc), file=sys.stderr)
    sys.exit(1)
