# M260C 语音合成与播报

输入文字后生成 WAV 并通过 Ubuntu 扬声器播报。默认使用讯飞在线合成，发音人为讯飞小露 `x4_yezi`。

## 直接播报

```bash
cd /media/yzc/F/DOGcode/my/voice/myvoice/Text_to_Speech
./tts "你好，我是小微"
```

默认音频保存在 `audio` 目录。

指定输出文件或只生成音频：

```bash
./tts "你好，我是小露" --output audio/hello.wav
./tts "你好，我是小露" --no-play
```

## 切换引擎和发音人

```bash
./tts "你好" --engine online --voice x4_yezi
./tts "你好，我是离线语音" --engine espeak
```

## 讯飞配置

凭据从本地 `iflytek.env` 读取：

```text
XFYUN_APP_ID=你的APPID
XFYUN_API_KEY=你的APIKey
XFYUN_API_SECRET=你的APISecret
```

## 调整声音

```bash
./tts "正在进行语音播报" --speed 50 --volume 50 --pitch 50
```

## 指定播放设备

```bash
./tts --list-devices
./tts "你好" --device plughw:CARD=设备名,DEV=0
```

正常使用时不需要指定设备，程序会通过 Ubuntu 默认音频输出播报。声卡被 PulseAudio 占用时也应省略 `--device`。

## JSON 输出

```bash
./tts "你好" --no-play --json
```

输出包含合成引擎、音频路径、采样率、时长和播放结果。

## 测试

```bash
python3 -m unittest discover -s tests -v
```
