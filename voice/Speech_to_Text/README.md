# 语音转文字

先在部署包根目录执行 `bash install.sh`，再进入本目录运行：

```bash
./stt --record                       # 默认在线 IAT，持续监听
./stt --record --verbose             # 显示实时中间结果
./stt --record --engine slm          # 中文识别大模型
./stt --record --offline              # Vosk 离线识别
./stt --record --timeout 10           # 单次识别，最长监听 10 秒
./stt --record --json                # 输出 JSON
```

按 `Ctrl+C` 停止监听。在线识别默认静音约 2 秒后结束当前句，再开始下一次识别。

```bash
./stt --list-devices
./stt --record --device plughw:CARD=XFMDPV0018,DEV=0
./stt --file example.wav
./stt --file example.pcm --offline
```

文件使用 16 kHz、单声道、16 位 PCM。当前代码的在线文件上限为 59 秒。

配置默认读取部署包内 `../Text_to_Speech/iflytek.env`，已填写。`--config` 可指定其他配置文件。

在线 JSON 的 `confidence` 为 `null`；离线模式返回模型置信度。
