#!/usr/bin/env bash
set -Eeuo pipefail

ROS_MASTER_URI="${ROS_MASTER_URI:-http://localhost:11311}"
export ROS_MASTER_URI
SHOW_RVIZ="${SHOW_RVIZ:-false}"
GOAL_SERVICE="/lite3_fixed_forward_goal/send_relative_goal"
LOG_ROOT="${LITE3_NAV_LOG_DIR:-${HOME}/.ros/lite3_navigation}"
LOG_DIR="${LOG_ROOT}/$(date +%Y%m%d_%H%M%S)"

declare -a STARTED_PIDS=()
declare -a STARTED_NAMES=()
INITIAL_FORWARD=""
INITIAL_LEFT=""

usage() {
  cat <<'EOF'
用法：
  /home/ysc/lite_cog/start_lite3_navigation.sh
  /home/ysc/lite_cog/start_lite3_navigation.sh FORWARD LEFT
  /home/ysc/lite_cog/start_lite3_navigation.sh --no-rviz [FORWARD LEFT]

目标是发送命令瞬间相对机器人的坐标（单位：米）：
  FORWARD > 0 前方，FORWARD < 0 后方
  LEFT    > 0 左侧，LEFT    < 0 右侧

示例：
  1.0  0.0    前方 1 米
  0.0 -1.0    右侧 1 米（先右转再过去）
 -1.0  0.0    后方 1 米（先转身再过去）
EOF
}

die() {
  echo "[错误] $*" >&2
  exit 1
}

is_number() {
  [[ "$1" =~ ^[-+]?([0-9]+([.][0-9]*)?|[.][0-9]+)([eE][-+]?[0-9]+)?$ ]]
}

node_exists() {
  rosnode list 2>/dev/null | grep -Fxq "$1"
}

service_exists() {
  rosservice list 2>/dev/null | grep -Fxq "$1"
}

start_component() {
  local name="$1"
  shift
  echo "[启动] ${name}（日志：${LOG_DIR}/${name}.log）"
  "$@" >"${LOG_DIR}/${name}.log" 2>&1 < /dev/null &
  local pid=$!
  STARTED_PIDS+=("${pid}")
  STARTED_NAMES+=("${name}")
}

show_recent_logs() {
  local name
  for name in "${STARTED_NAMES[@]:-}"; do
    if [[ -f "${LOG_DIR}/${name}.log" ]]; then
      echo "----- ${name}.log -----" >&2
      tail -n 25 "${LOG_DIR}/${name}.log" >&2 || true
    fi
  done
}

cleanup() {
  local rc=$?
  trap - EXIT INT TERM
  if ((${#STARTED_PIDS[@]} > 0)); then
    echo
    echo "[关闭] 正在停止本脚本启动的 ROS 进程……"
    local i pid
    for ((i=${#STARTED_PIDS[@]}-1; i>=0; --i)); do
      pid="${STARTED_PIDS[$i]}"
      kill -INT "${pid}" 2>/dev/null || true
    done
    sleep 2
    for pid in "${STARTED_PIDS[@]}"; do
      if kill -0 "${pid}" 2>/dev/null; then
        kill -TERM "${pid}" 2>/dev/null || true
      fi
    done
    wait "${STARTED_PIDS[@]}" 2>/dev/null || true
  fi
  if ((rc != 0)); then
    echo "[提示] 组件日志保存在：${LOG_DIR}" >&2
  fi
  exit "${rc}"
}

wait_for_master() {
  local deadline=$((SECONDS + 20))
  until rosnode list >/dev/null 2>&1; do
    ((SECONDS >= deadline)) && return 1
    sleep 0.5
  done
}

wait_for_topic_message() {
  local topic="$1"
  local seconds="$2"
  echo "[等待] ${topic} 数据（最多 ${seconds}s）"
  timeout "${seconds}" rostopic echo -n 1 "${topic}" >/dev/null 2>&1
}

wait_for_goal_service() {
  local deadline=$((SECONDS + 30))
  until service_exists "${GOAL_SERVICE}"; do
    ((SECONDS >= deadline)) && return 1
    sleep 0.5
  done
}

send_goal() {
  local forward="$1"
  local left="$2"
  if ! is_number "${forward}" || ! is_number "${left}"; then
    echo "[输入错误] 请输入两个数字，例如：1.0 0.0" >&2
    return 2
  fi

  local request
  printf -v request 'forward: %s\nleft: %s' "${forward}" "${left}"
  echo "[目标] forward=${forward} m, left=${left} m"
  rosservice call "${GOAL_SERVICE}" "${request}"
}

while (($# > 0)); do
  case "$1" in
    --no-rviz)
      SHOW_RVIZ=false
      shift
      ;;
    --rviz)
      SHOW_RVIZ=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -* )
      # A negative number is a goal coordinate, not an option.
      if is_number "$1"; then
        break
      fi
      die "未知选项：$1"
      ;;
    *)
      break
      ;;
  esac
done

if (($# == 2)); then
  is_number "$1" && is_number "$2" || die "FORWARD 和 LEFT 必须是数字"
  INITIAL_FORWARD="$1"
  INITIAL_LEFT="$2"
elif (($# != 0)); then
  usage
  die "目标需要两个数：FORWARD LEFT"
fi

trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

mkdir -p "${LOG_DIR}"

# Remove ROS 2 / Conda overlays before loading the three ROS 1 workspaces.
unset ROS_DISTRO ROS_VERSION ROS_PYTHON_VERSION AMENT_PREFIX_PATH COLCON_PREFIX_PATH PYTHONPATH
set +u
source /opt/ros/noetic/setup.bash
source /home/ysc/lite_cog/transfer/devel/setup.bash --extend
source /home/ysc/lite_cog/drivers/mid360_ws/devel/setup.bash --extend
source /home/ysc/lite_cog/SCAN-Planner/devel/setup.bash --extend
set -u

if systemctl is-active --quiet transfer_ros2.service 2>/dev/null; then
  echo "[处理] 停止会占用 UDP 43897 的 transfer_ros2.service"
  sudo -n systemctl stop transfer_ros2.service ||
    die "无法无密码停止 transfer_ros2.service，请先执行：sudo systemctl stop transfer_ros2.service"
fi

if ! rosnode list >/dev/null 2>&1; then
  start_component roscore roscore
  wait_for_master || {
    show_recent_logs
    die "ROS master 启动超时"
  }
else
  echo "[复用] 已存在的 ROS master：${ROS_MASTER_URI}"
fi

if node_exists /scan_planner_node || service_exists "${GOAL_SERVICE}"; then
  die "检测到旧的 SCAN-Planner 正在运行。请先关闭旧 roslaunch，再重新运行本脚本。"
fi

if node_exists /qnx2ros; then
  echo "[复用] 已运行的 ROS1 transfer"
else
  if [[ -n "$(ss -H -lun 'sport = :43897' 2>/dev/null || true)" ]]; then
    die "UDP 43897 已被其他进程占用，无法启动 ROS1 transfer"
  fi
  start_component transfer roslaunch message_transformer message_transformer.launch
fi

if node_exists /livox_lidar_publisher2; then
  echo "[复用] 已运行的 MID360 驱动"
else
  start_component mid360 roslaunch livox_ros_driver2 msg_MID360.launch
fi

wait_for_topic_message /leg_odom2 35 || {
  show_recent_logs
  die "没有收到 /leg_odom2；检查 192.168.1.120、UDP 43897 和机器人上位机"
}

wait_for_topic_message /rslidar_points 45 || {
  show_recent_logs
  die "没有收到 /rslidar_points；检查 MID360 网线、IP 和配置文件"
}

start_component scan_planner roslaunch scan_planner run_lite3.launch "show_rviz:=${SHOW_RVIZ}"
wait_for_goal_service || {
  show_recent_logs
  die "SCAN-Planner 目标服务启动超时"
}

echo
echo "============================================================"
echo "Lite3 导航已就绪。保持实体急停可用。"
echo "直接输入两个数：FORWARD LEFT；输入 help 查看说明；输入 quit 退出。"
echo "例：1 0（前方1m），0 -1（右侧1m），-1 0（转身去后方1m）"
echo "日志目录：${LOG_DIR}"
echo "============================================================"

if [[ -n "${INITIAL_FORWARD}" ]]; then
  send_goal "${INITIAL_FORWARD}" "${INITIAL_LEFT}" || true
fi

while true; do
  printf '\n目标 forward left > '
  if ! IFS= read -r line; then
    break
  fi
  line="${line#"${line%%[![:space:]]*}"}"
  line="${line%"${line##*[![:space:]]}"}"
  [[ -z "${line}" ]] && continue

  case "${line}" in
    q|quit|exit|退出)
      break
      ;;
    h|help|帮助)
      usage
      continue
      ;;
    status|状态)
      rosnode list | grep -E 'qnx2ros|livox_lidar_publisher2|scan_planner_node|closed_loop_controller' || true
      continue
      ;;
  esac

  read -r forward left extra <<<"${line}"
  if [[ -n "${extra:-}" || -z "${forward:-}" || -z "${left:-}" ]]; then
    echo "[输入错误] 请输入两个数字，例如：1.0 -0.5"
    continue
  fi
  send_goal "${forward}" "${left}" || true
done

echo "[退出] 导航组件将安全关闭。"
