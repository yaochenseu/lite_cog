#!/usr/bin/env python3

import argparse
import base64
import ctypes
import ctypes.util
import hashlib
import hmac
import json
import os
import shutil
import subprocess
import sys
import wave
from datetime import datetime
from email.utils import formatdate
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parent
DEFAULT_AUDIO_DIR = ROOT / "audio"
DEFAULT_CONFIG = ROOT / "iflytek.env"
PYTHON_PACKAGES = ROOT / "third_party" / "python"
XFYUN_TTS_URL = "wss://tts-api.xfyun.cn/v2/tts"
XFYUN_TTS_HOST = "tts-api.xfyun.cn"
XFYUN_TTS_PATH = "/v2/tts"

sys.path.insert(0, str(PYTHON_PACKAGES))

ESPEAK_AUDIO_OUTPUT_RETRIEVAL = 1
ESPEAK_CHARS_UTF8 = 1
ESPEAK_RATE = 1
ESPEAK_VOLUME = 2
ESPEAK_PITCH = 3


class TtsError(RuntimeError):
    pass


def load_config(path):
    values = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip("\"'")

    keys = ("XFYUN_APP_ID", "XFYUN_API_KEY", "XFYUN_API_SECRET", "XFYUN_API_PASSWORD")
    return {key: os.environ.get(key) or values.get(key, "") for key in keys}


def create_xfyun_auth_url(api_key, api_secret):
    date = formatdate(timeval=None, localtime=False, usegmt=True)
    signature_origin = (
        f"host: {XFYUN_TTS_HOST}\n"
        f"date: {date}\n"
        f"GET {XFYUN_TTS_PATH} HTTP/1.1"
    )
    signature = base64.b64encode(
        hmac.new(api_secret.encode("utf-8"), signature_origin.encode("utf-8"), hashlib.sha256).digest()
    ).decode("ascii")
    authorization_origin = (
        f'api_key="{api_key}",algorithm="hmac-sha256",'
        f'headers="host date request-line",signature="{signature}"'
    )
    authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode("ascii")
    return f"{XFYUN_TTS_URL}?{urlencode({'authorization': authorization, 'date': date, 'host': XFYUN_TTS_HOST})}"


class XfyunOnline:
    sample_rate = 16000

    def __init__(self, config_path, voice="x4_yezi", speed=50, volume=50, pitch=50, timeout=30):
        config = load_config(config_path)
        self.app_id = config["XFYUN_APP_ID"]
        self.api_key = config["XFYUN_API_KEY"]
        self.api_secret = config["XFYUN_API_SECRET"]
        self.api_password = config["XFYUN_API_PASSWORD"]
        self.voice = voice
        self.speed = speed
        self.volume = volume
        self.pitch = pitch
        self.timeout = timeout

        if not self.app_id:
            raise TtsError(f"配置文件缺少 XFYUN_APP_ID: {config_path}")
        if not self.api_password and (not self.api_key or not self.api_secret):
            raise TtsError(f"配置文件缺少讯飞在线合成凭据: {config_path}")

    def synthesize(self, text):
        if len(text.encode("utf-8")) >= 8000:
            raise TtsError("讯飞在线合成的单次文本必须小于 8000 字节")
        try:
            import websocket
        except ImportError as error:
            raise TtsError("缺少 websocket-client，请安装 requirements.txt 中的依赖") from error

        if self.api_password:
            url = XFYUN_TTS_URL
            headers = [f"x-api-key: {self.api_password}"]
        else:
            url = create_xfyun_auth_url(self.api_key, self.api_secret)
            headers = []

        payload = {
            "common": {"app_id": self.app_id},
            "business": {
                "aue": "raw",
                "auf": "audio/L16;rate=16000",
                "vcn": self.voice,
                "tte": "utf8",
                "speed": self.speed,
                "volume": self.volume,
                "pitch": self.pitch,
            },
            "data": {
                "status": 2,
                "text": base64.b64encode(text.encode("utf-8")).decode("ascii"),
            },
        }

        connection = None
        chunks = []
        try:
            connection = websocket.create_connection(url, timeout=self.timeout, header=headers)
            connection.send(json.dumps(payload, ensure_ascii=False))
            while True:
                response = connection.recv()
                if isinstance(response, bytes):
                    chunks.append(response)
                    continue
                message = json.loads(response)
                code = int(message.get("code", -1))
                if code != 0:
                    description = message.get("message") or message.get("msg") or "未知错误"
                    raise TtsError(f"讯飞在线合成失败，错误码 {code}: {description}")
                data = message.get("data") or {}
                audio = data.get("audio")
                if audio:
                    chunks.append(base64.b64decode(audio))
                if data.get("status") == 2:
                    break
        except TtsError:
            raise
        except Exception as error:
            raise TtsError(f"无法连接讯飞在线合成服务: {type(error).__name__}") from error
        finally:
            if connection is not None:
                connection.close()

        audio = b"".join(chunks)
        if not audio:
            raise TtsError("讯飞在线合成未返回音频")
        return audio


class EspeakNg:
    def __init__(self, voice="cmn", speed=175, volume=100, pitch=50):
        library = ctypes.util.find_library("espeak-ng") or "libespeak-ng.so.1"
        try:
            self.lib = ctypes.CDLL(library)
        except OSError as error:
            raise TtsError("找不到 eSpeak NG 合成库") from error

        self._configure_api()
        self._chunks = []
        self._closed = False
        self._callback_type = ctypes.CFUNCTYPE(
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_short),
            ctypes.c_int,
            ctypes.c_void_p,
        )
        self._callback = self._callback_type(self._on_audio)

        self.sample_rate = self.lib.espeak_Initialize(
            ESPEAK_AUDIO_OUTPUT_RETRIEVAL, 0, None, 0
        )
        if self.sample_rate <= 0:
            raise TtsError("eSpeak NG 初始化失败")

        self.lib.espeak_SetSynthCallback(self._callback)
        if self.lib.espeak_SetVoiceByName(voice.encode("utf-8")) != 0:
            self.close()
            raise TtsError(f"找不到语音: {voice}")

        self._set_parameter(ESPEAK_RATE, speed, "语速")
        self._set_parameter(ESPEAK_VOLUME, volume, "音量")
        self._set_parameter(ESPEAK_PITCH, pitch, "音调")

    def _configure_api(self):
        self.lib.espeak_Initialize.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
        ]
        self.lib.espeak_Initialize.restype = ctypes.c_int
        self.lib.espeak_SetSynthCallback.argtypes = [ctypes.c_void_p]
        self.lib.espeak_SetSynthCallback.restype = None
        self.lib.espeak_SetVoiceByName.argtypes = [ctypes.c_char_p]
        self.lib.espeak_SetVoiceByName.restype = ctypes.c_int
        self.lib.espeak_SetParameter.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.lib.espeak_SetParameter.restype = ctypes.c_int
        self.lib.espeak_Synth.argtypes = [
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.c_uint,
            ctypes.c_int,
            ctypes.c_uint,
            ctypes.c_uint,
            ctypes.POINTER(ctypes.c_uint),
            ctypes.c_void_p,
        ]
        self.lib.espeak_Synth.restype = ctypes.c_int
        self.lib.espeak_Synchronize.argtypes = []
        self.lib.espeak_Synchronize.restype = ctypes.c_int
        self.lib.espeak_Terminate.argtypes = []
        self.lib.espeak_Terminate.restype = ctypes.c_int

    def _on_audio(self, samples, sample_count, _events):
        if samples and sample_count > 0:
            self._chunks.append(ctypes.string_at(samples, sample_count * 2))
        return 0

    def _set_parameter(self, parameter, value, name):
        if self.lib.espeak_SetParameter(parameter, value, 0) != 0:
            self.close()
            raise TtsError(f"无法设置{name}")

    def synthesize(self, text):
        self._chunks.clear()
        encoded = text.encode("utf-8") + b"\0"
        text_buffer = ctypes.create_string_buffer(encoded)
        utterance_id = ctypes.c_uint(0)
        result = self.lib.espeak_Synth(
            ctypes.cast(text_buffer, ctypes.c_void_p),
            len(encoded),
            0,
            0,
            0,
            ESPEAK_CHARS_UTF8,
            ctypes.byref(utterance_id),
            None,
        )
        if result != 0:
            raise TtsError(f"语音合成失败，错误码: {result}")
        result = self.lib.espeak_Synchronize()
        if result != 0:
            raise TtsError(f"等待语音合成失败，错误码: {result}")
        audio = b"".join(self._chunks)
        if not audio:
            raise TtsError("语音合成未产生音频")
        return audio

    def close(self):
        if not self._closed:
            self.lib.espeak_Terminate()
            self._closed = True


def validate_range(parser, name, value, minimum, maximum):
    if not minimum <= value <= maximum:
        parser.error(f"{name} 必须在 {minimum} 到 {maximum} 之间")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="讯飞在线语音合成与播报")
    parser.add_argument("text", nargs="?", help="需要合成和播报的文字")
    parser.add_argument("-o", "--output", type=Path, help="WAV 输出路径")
    parser.add_argument("--no-play", action="store_true", help="只生成 WAV，不播放")
    parser.add_argument("--device", help="指定 ALSA 播放设备")
    parser.add_argument("--engine", choices=("online", "espeak"), default="online", help="合成引擎")
    parser.add_argument("--voice", help="发音人，在线默认讯飞小露，离线默认 cmn")
    parser.add_argument("--speed", type=int, help="语速")
    parser.add_argument("--volume", type=int, help="音量")
    parser.add_argument("--pitch", type=int, help="音调")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="讯飞凭据配置文件")
    parser.add_argument("--timeout", type=float, default=30, help="在线请求超时秒数")
    parser.add_argument("--list-devices", action="store_true", help="列出播放设备")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args(argv)

    if args.timeout <= 0:
        parser.error("--timeout 必须大于 0")
    if args.engine == "online":
        args.voice = args.voice or "x4_yezi"
        args.speed = 50 if args.speed is None else args.speed
        args.volume = 50 if args.volume is None else args.volume
        args.pitch = 50 if args.pitch is None else args.pitch
        validate_range(parser, "--speed", args.speed, 0, 100)
        validate_range(parser, "--volume", args.volume, 0, 100)
        validate_range(parser, "--pitch", args.pitch, 0, 100)
    else:
        args.voice = args.voice or "cmn"
        args.speed = 175 if args.speed is None else args.speed
        args.volume = 100 if args.volume is None else args.volume
        args.pitch = 50 if args.pitch is None else args.pitch
        validate_range(parser, "--speed", args.speed, 80, 450)
        validate_range(parser, "--volume", args.volume, 0, 200)
        validate_range(parser, "--pitch", args.pitch, 0, 99)
    if args.device and args.no_play:
        parser.error("--device 不能与 --no-play 同时使用")
    return args


def default_output_path():
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    return DEFAULT_AUDIO_DIR / f"tts_{stamp}.wav"


def synthesize_to_wav(text, output, voice="cmn", speed=175, volume=100, pitch=50):
    if not text.strip():
        raise TtsError("合成文字不能为空")

    engine = EspeakNg(voice=voice, speed=speed, volume=volume, pitch=pitch)
    try:
        audio = engine.synthesize(text)
        sample_rate = engine.sample_rate
    finally:
        engine.close()

    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(sample_rate)
        stream.writeframes(audio)

    duration = len(audio) / 2 / sample_rate
    return output, sample_rate, duration


def synthesize_online_to_wav(
    text,
    output,
    config_path=DEFAULT_CONFIG,
    voice="x4_yezi",
    speed=50,
    volume=50,
    pitch=50,
    timeout=30,
):
    if not text.strip():
        raise TtsError("合成文字不能为空")

    engine = XfyunOnline(
        config_path=config_path,
        voice=voice,
        speed=speed,
        volume=volume,
        pitch=pitch,
        timeout=timeout,
    )
    audio = engine.synthesize(text)
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(engine.sample_rate)
        stream.writeframes(audio)

    duration = len(audio) / 2 / engine.sample_rate
    return output, engine.sample_rate, duration


def play_wav(path, device=None):
    if device:
        if not shutil.which("aplay"):
            raise TtsError("找不到 aplay，无法使用指定设备播放")
        commands = [("aplay", ["aplay", "-q", "-D", device, str(path)])]
    else:
        commands = [
            ("aplay", ["aplay", "-q", str(path)]),
            ("paplay", ["paplay", str(path)]),
            ("pw-play", ["pw-play", str(path)]),
        ]

    failures = []
    for player, command in commands:
        if not shutil.which(player):
            continue
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return player
        message = result.stderr.strip() or result.stdout.strip()
        if message:
            failures.append(f"{player}: {message.splitlines()[-1]}")

    detail = "; ".join(failures)
    if detail:
        if device:
            raise TtsError(f"无法使用播放设备 {device}（{detail}）")
        raise TtsError(f"播放失败，未找到可用的音频输出设备（{detail}）")
    raise TtsError("播放失败，找不到 aplay、paplay 或 pw-play")


def list_devices():
    if not shutil.which("aplay"):
        raise TtsError("找不到 aplay")
    return subprocess.run(["aplay", "-l"], check=False).returncode


def read_text(args):
    if args.text is not None:
        return args.text
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    raise TtsError("请提供需要合成的文字")


def emit_error(error, as_json):
    if as_json:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False), file=sys.stderr)
    else:
        print(f"错误: {error}", file=sys.stderr)


def main(argv=None):
    args = parse_args(argv)
    try:
        if args.list_devices:
            return list_devices()

        text = read_text(args)
        if args.engine == "online":
            output, sample_rate, duration = synthesize_online_to_wav(
                text,
                args.output or default_output_path(),
                config_path=args.config,
                voice=args.voice,
                speed=args.speed,
                volume=args.volume,
                pitch=args.pitch,
                timeout=args.timeout,
            )
        else:
            output, sample_rate, duration = synthesize_to_wav(
                text,
                args.output or default_output_path(),
                voice=args.voice,
                speed=args.speed,
                volume=args.volume,
                pitch=args.pitch,
            )

        player = None
        if not args.no_play:
            try:
                player = play_wav(output, args.device)
            except TtsError as error:
                raise TtsError(f"WAV 已生成: {output}；{error}") from error

        if args.json:
            print(
                json.dumps(
                    {
                        "status": "ok",
                        "engine": args.engine,
                        "text": text,
                        "output": str(output),
                        "sample_rate": sample_rate,
                        "duration": round(duration, 3),
                        "played": player is not None,
                        "player": player,
                    },
                    ensure_ascii=False,
                )
            )
        else:
            print(f"音频文件: {output}")
            if player:
                print(f"播报完成: {player}")
        return 0
    except (OSError, TtsError) as error:
        emit_error(error, args.json)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
