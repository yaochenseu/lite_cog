# Jetson 语音部署包

将整个 `To_jetson` 文件夹复制到 Jetson。包内已包含源码、Vosk 中文模型和现有讯飞认证信息。

适用环境：ARM64 Ubuntu、Python 3.8 及以上。首次安装需要联网，依赖在 Jetson 上安装；日常运行无需手动激活 Python 环境。

| 功能 | 运行方式 |
|---|---|
| 语音唤醒、唤醒时方向角度 | M260C 串口，本地运行 |
| 语音听写 IAT | 讯飞在线流式识别，默认 |
| 中文识别大模型 SLM | 讯飞在线识别，可切换 |
| 离线语音识别 | Vosk 中文模型 |
| 合成与播报 | 默认在线“讯飞小露”，可切换离线 eSpeak |

## 安装

在 Jetson 上进入复制后的目录，例如：

```bash
cd ~/To_jetson
bash install.sh
```

脚本安装系统依赖、创建 `.venv`，并加入 `dialout`、`audio` 设备访问组。安装完成后注销并重新登录。

默认使用 `python3`。需要指定已有的 Python 解释器时：

```bash
bash install.sh --python /usr/bin/python3.10
```

## 运行

以下命令均在 `To_jetson` 目录执行，每个模块单独启动。

唤醒及方向角度，当前设备唤醒词为“小微小微”：

```bash
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --json
```

语音听写，默认持续监听，按 `Ctrl+C` 停止：

```bash
./run stt --record
./run stt --record --verbose          # 显示实时中间结果
./run stt --record --timeout 10       # 单次识别，最长监听 10 秒
```

切换识别方式：

```bash
./run stt --record --engine iat       # 语音听写，默认
./run stt --record --engine slm       # 中文识别大模型
./run stt --record --offline          # Vosk 离线识别
```

合成与播报：

```bash
./run tts "你好，我是讯飞小露。"
./run tts "你好" --no-play            # 只生成 WAV
./run tts "你好" --engine espeak      # 离线合成
```

音频保存在 `Text_to_Speech/audio/`。TTS 当前先生成完整 WAV，再播放。

原来的子项目入口也可使用：`./Speech_to_Text/stt`、`./Text_to_Speech/tts`。

## 设备与认证

连接 M260C 后查看串口和声卡：

```bash
ls -l /dev/serial/by-id/
./run stt --list-devices
./run tts --list-devices
```

唤醒命令的 `--port` 使用实际列出的串口路径。录音默认使用 `plughw:CARD=XFMDPV0018,DEV=0`；如名称不同，用 `--device` 指定。播报使用 Jetson 的默认音频输出，也支持 `--device`。

认证文件已放在 `Text_to_Speech/iflytek.env`，三个在线服务自动读取，包含你提供的 APPID、APIKey、APISecret。文件权限为 `600`，无需再次填写。

## 检查与测试

```bash
./run check
bash test.sh
./run wake --port /dev/serial/by-id/usb-WCH.CN_USB_Single_Serial_0004-if00 --check-serial --timeout 15
```

`check` 检查本地依赖、模型及配置，`test.sh` 运行随包测试。两者都不录音、不调用讯飞。

## 文件说明

- `wake/`：串口唤醒和方向角度。
- `Speech_to_Text/`：三种识别引擎及 Vosk 中文模型。
- `Text_to_Speech/`：合成播报和认证文件。
- `install.sh`：Jetson 安装脚本；`run`：统一入口。
- `requirements.txt`：Python 依赖清单。

部署包使用支持 Python 3.8 的 [websockets 13.1](https://pypi.org/project/websockets/13.1/)，并由 pip 安装 [Vosk ARM64 包](https://pypi.org/project/vosk/0.3.45/)。当前电脑的 x86-64 动态库、虚拟环境和旧讯飞 SDK 未复制。
