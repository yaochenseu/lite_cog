# M260C 语音转文字

默认使用响应更快的讯飞流式语音听写，支持 M260C 持续监听和 PCM/WAV 文件识别。中文识别大模型和 Vosk 离线模式同时保留。

## 实时识别

```bash
cd /media/yzc/F/DOGcode/my/voice/myvoice/Speech_to_Text
./stt --record
```

默认持续监听并逐句输出，按 `Ctrl+C` 停止。

显示实时中间结果：

```bash
./stt --record --verbose
```

切换识别引擎：

```bash
./stt --record --engine iat       # 语音听写，默认
./stt --record --engine slm       # 中文识别大模型
./stt --record --engine offline   # Vosk 离线识别
```

需要限时单次识别时指定秒数：

```bash
./stt --record --timeout 10
```

默认录音设备为 `plughw:CARD=XFMDPV0018,DEV=0`。查看或指定设备：

```bash
./stt --list-devices
./stt --record --device plughw:CARD=XFMDPV0018,DEV=0
```

## 文件识别

```bash
./stt --file example.wav
./stt --file example.pcm
```

音频使用 16 kHz、单声道、16 位 PCM 格式。在线文件最长 60 秒；持续监听会自动开始下一次识别。

## 讯飞配置

默认复用 `../Text_to_Speech/iflytek.env`。也可以在本目录创建 `iflytek.env`：

```text
XFYUN_APP_ID=你的APPID
XFYUN_API_KEY=你的APIKey
XFYUN_API_SECRET=你的APISecret
```

指定其他配置文件：

```bash
./stt --record --config /path/to/iflytek.env
```

两个在线服务使用同一组认证信息：

- `iat`：讯飞流式语音听写，默认使用。
- `slm`：讯飞中文识别大模型，识别参数为 `slm/zh_cn/mandarin`。

## 离线识别

```bash
./stt --record --offline
./stt --file audio/vvui_deno.pcm --offline
```

## JSON 输出

```bash
./stt --record --json
```

在线结果示例：

```json
{"status":"ok","text":"识别到的文字","confidence":null}
```

## 主要文件

- `stt.py`：命令入口、录音和离线识别。
- `xfyun_iat.py`：讯飞语音听写客户端。
- `xfyun_slm.py`：讯飞中文识别大模型客户端和共用传输流程。
- `models/vosk-model-small-cn-0.22`：离线中文模型。

## 测试

```bash
python3 -m unittest discover -s tests -v
./stt --file audio/vvui_deno.pcm --offline --json
```
