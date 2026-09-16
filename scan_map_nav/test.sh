#!/usr/bin/env bash
set -eo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/env.sh"
/usr/bin/python3 -m unittest discover -s "$SCAN_MAP_NAV_ROOT/tests" -p 'test_*.py'
SCAN_NAV_SCENARIO=guide_extension /usr/bin/python3 "$SCAN_MAP_NAV_ROOT/tests/isolated_navigation.py"
SCAN_NAV_SCENARIO=local_recovery /usr/bin/python3 "$SCAN_MAP_NAV_ROOT/tests/isolated_navigation.py"
SCAN_NAV_SCENARIO=localization /usr/bin/python3 "$SCAN_MAP_NAV_ROOT/tests/isolated_navigation.py"
/usr/bin/python3 "$SCAN_MAP_NAV_ROOT/tests/isolated_navigation.py"
