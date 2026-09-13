#!/usr/bin/env bash
set -eo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/env.sh"
if [[ ! -x "$SCAN_MAP_NAV_ROOT/devel/lib/scan_map_navigation/map_scan_planner" ]]; then
  echo 'Run ./build.sh first.' >&2
  exit 1
fi
/usr/bin/python3 "$SCAN_MAP_NAV_ROOT/src/scan_map_navigation/scripts/preflight.py"
exec roslaunch scan_map_navigation navigation.launch "$@"
