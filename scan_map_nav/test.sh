#!/usr/bin/env bash
set -eo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/env.sh"
/usr/bin/python3 -m unittest discover -s "$SCAN_MAP_NAV_ROOT/tests" -p 'test_*.py'
exec /usr/bin/python3 "$SCAN_MAP_NAV_ROOT/tests/isolated_navigation.py"
