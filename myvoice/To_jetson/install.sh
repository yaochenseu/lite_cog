#!/usr/bin/env bash
set -euo pipefail

bundle_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python_bin=python3
while [[ $# -gt 0 ]]; do
  case "$1" in
    --python)
      [[ $# -ge 2 ]] || { echo '--python 后需要 Python 路径' >&2; exit 2; }
      python_bin="$2"
      shift 2
      ;;
    -h|--help)
      echo '用法: bash install.sh [--python /usr/bin/python3]'
      echo '在 Jetson ARM64 上联网安装系统依赖、Python 环境和设备访问权限。'
      exit 0
      ;;
    *) echo "未知参数: $1" >&2; exit 2 ;;
  esac
done

if [[ "$(uname -s)" != Linux || "$(uname -m)" != aarch64 ]]; then
  echo '请在 Jetson 的 ARM64 Ubuntu 系统运行此安装脚本。' >&2
  exit 1
fi
if [[ "$EUID" -eq 0 ]]; then
  echo '请以普通用户运行 bash install.sh，脚本会自行调用 sudo。' >&2
  exit 1
fi
"$python_bin" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else "需要 Python 3.8 或以上；可通过 --python 指定解释器。")'

sudo apt-get update
sudo apt-get install -y python3-venv python3-dev build-essential libffi-dev \
  ca-certificates alsa-utils espeak-ng libespeak-ng1

"$python_bin" -m venv "$bundle_dir/.venv"
"$bundle_dir/.venv/bin/python3" -m pip install --upgrade pip
"$bundle_dir/.venv/bin/python3" -m pip install -r "$bundle_dir/requirements.txt"
"$bundle_dir/.venv/bin/python3" -m pip check

chmod 600 "$bundle_dir/Text_to_Speech/iflytek.env"
chmod +x "$bundle_dir/run" "$bundle_dir/test.sh" \
  "$bundle_dir/Speech_to_Text/stt" "$bundle_dir/Text_to_Speech/tts"
sudo usermod -aG dialout,audio "$(id -un)"
bash "$bundle_dir/run" check
echo '安装完成。注销并重新登录后，运行 ./run stt --record。'
