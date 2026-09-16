#!/usr/bin/env python3
"""Check package dependencies locally without recording or cloud requests."""

import ctypes.util
import platform
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "Speech_to_Text"))
sys.path.insert(0, str(ROOT / "Text_to_Speech"))


def main():
    print("系统架构: " + platform.machine())
    print("Python: " + platform.python_version())
    try:
        import websocket
        import websockets
        from websockets.sync.client import connect
        from vosk import Model, SetLogLevel
        from xfyun_iat import XfyunIatRecognizer
        from xfyun_slm import XfyunSlmRecognizer
        from tts import DEFAULT_CONFIG, XfyunOnline

        print("WebSocket 依赖: websockets " + websockets.__version__
              + " / websocket-client " + websocket.__version__)
        XfyunIatRecognizer()
        XfyunSlmRecognizer()
        XfyunOnline(DEFAULT_CONFIG)
        print("讯飞配置: 已读取（IAT / SLM / TTS）")

        if not ctypes.util.find_library("espeak-ng"):
            raise RuntimeError("未找到 libespeak-ng1")
        for command in ("arecord", "aplay"):
            if not shutil.which(command):
                raise RuntimeError("未找到 " + command)
        print("录音与播报依赖: 正常")

        SetLogLevel(-1)
        model = Model(str(ROOT / "Speech_to_Text/models/vosk-model-small-cn-0.22"))
        print("Vosk 中文模型: 加载成功")
        del model
    except Exception as error:
        print("检查失败: " + str(error), file=sys.stderr)
        return 1
    print("本地环境检查通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
