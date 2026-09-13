# M260C 语音唤醒

该目录提供独立的 M260C 语音唤醒和声源定位功能，支持串口检查、持续监听和修改唤醒词。

## 快速运行

```bash
cd /media/yzc/F/DOGcode/my/voice/myvoice
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --json
```

已完成实机验证：

| 项目 | 实机信息 |
|---|---|
| 设备 | 旧版 M260C 环形六麦 |
| 稳定串口 | `/dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00` |
| 当前映射 | `/dev/ttyACM0` |
| 固件 | `circle6:v1.0.2` |
| 引擎 | `se_circle.1004` |
| 当前唤醒词 | 小微小微 |

## 串口权限

当前用户需要属于 `dialout` 组：

```bash
sudo usermod -aG dialout "$USER"
```

注销并重新登录后检查：

```bash
groups
ls -l /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00
```

推荐使用 `/dev/serial/by-id/` 路径。它根据设备序列号生成，重新插拔后不会受到 `ttyACM0`、`ttyACM1` 编号变化的影响。

## 检查设备

```bash
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --check-serial \
  --timeout 15
```

设备正常启动后会返回类似信息：

```text
version: circle6:v1.0.2 engine:se_circle.1004
```

## 监听一次

监听一次，成功后退出：

```bash
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --once \
  --json
```

不带 `--once` 时默认持续监听，按 `Ctrl+C` 停止。

## 输出内容

```json
{"event":"wake","timestamp":1788347943.567542,"message_id":1,"keyword":"xiao3 wei1 xiao3 wei1","angle_deg":166.0,"beam":3,"confidence":1332.0}
```

| 字段 | 含义 |
|---|---|
| `keyword` | 识别到的唤醒词 |
| `angle_deg` | 声源方向角度 |
| `beam` | 唤醒波束编号 |
| `confidence` | 唤醒置信度 |

## 修改唤醒词

旧版 M260C 使用带声调数字的拼音。中文唤醒词使用 4～6 个汉字。

设置“小微小微”：

```bash
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --set-wake-word "xiao3 wei1 xiao3 wei1" \
  --threshold 900
```

设置“你好小微”：

```bash
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --set-wake-word "ni3 hao3 xiao3 wei1" \
  --threshold 900
```

设置后等待设备重启，再通过 `--check-serial` 确认版本信息，最后测试新唤醒词。

## 调试

显示收到的协议帧：

```bash
python3 wake/m260c_wake.py \
  --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 \
  --verbose
```

## 测试

```bash
python3 -m unittest wake.test_m260c_wake
```

程序仅使用 Python 标准库。
