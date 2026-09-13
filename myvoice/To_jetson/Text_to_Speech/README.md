# 语音合成与播报

先在部署包根目录执行 `bash install.sh`，再进入本目录运行：

```bash
./tts "你好，我是讯飞小露。"
./tts "你好" --no-play --output audio/hello.wav
./tts "你好" --engine espeak
./tts "你好" --voice x4_yezi --speed 50 --volume 50 --pitch 50
./tts "你好" --no-play --json
```

默认在线发音人为讯飞小露 `x4_yezi`。先生成 WAV，再通过默认扬声器播放；输出保存到 `audio/`。

本目录的 `iflytek.env` 已包含讯飞认证信息，语音识别模块也复用此文件。

查看或指定播放设备：

```bash
./tts --list-devices
./tts "你好" --device plughw:CARD=设备名,DEV=0
```
