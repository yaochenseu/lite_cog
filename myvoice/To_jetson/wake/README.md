# 语音唤醒与方向角度

先在部署包根目录执行 `bash install.sh`。以下命令在根目录运行。

```bash
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --json
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --once --json
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --check-serial --timeout 15
```

默认持续监听，按 `Ctrl+C` 停止。唤醒事件包含 `keyword`、`angle_deg`、`beam`、`confidence`；角度在唤醒时返回。

当前设备唤醒词为“小微小微”。设置唤醒词：

```bash
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --set-wake-word "xiao3 wei1 xiao3 wei1" --threshold 900
```

设置后等待设备重启并检查串口。用 `ls -l /dev/serial/by-id/` 查看实际串口路径，`--verbose` 显示协议帧。
