#!/usr/bin/env bash
# Source this file. Do not enable nounset: ROS generated setup scripts use unset variables.
SCAN_MAP_NAV_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source /opt/ros/noetic/setup.bash
source /home/ysc/lite_cog/nav/devel/setup.bash --extend
source /home/ysc/lite_cog/SCAN-Planner/devel/setup.bash --extend
if [[ -f "$SCAN_MAP_NAV_ROOT/devel/setup.bash" ]]; then
  source "$SCAN_MAP_NAV_ROOT/devel/setup.bash" --extend
fi
