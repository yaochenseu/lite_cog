#!/usr/bin/env bash
set -euo pipefail

bundle_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python_bin="$bundle_dir/.venv/bin/python3"
if [[ ! -x "$python_bin" ]]; then
  echo '请先在 Jetson 上运行 bash install.sh。' >&2
  exit 1
fi
cd "$bundle_dir"
"$python_bin" -B -m unittest wake.test_m260c_wake -v
cd "$bundle_dir/Speech_to_Text"
"$python_bin" -B -m unittest discover -s tests -v
cd "$bundle_dir/Text_to_Speech"
"$python_bin" -B -m unittest discover -s tests -v
