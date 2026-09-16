#!/usr/bin/env python3

import base64
import hashlib
import hmac
import json
import os
import sys
import time
from email.utils import formatdate
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parent
PYTHON_PACKAGES = ROOT / "third_party" / "python"
LOCAL_CONFIG = ROOT / "iflytek.env"
SHARED_CONFIG = ROOT.parent / "Text_to_Speech" / "iflytek.env"
XFYUN_SLM_URL = "wss://iat.xf-yun.com/v1"
XFYUN_SLM_HOST = "iat.xf-yun.com"
XFYUN_SLM_PATH = "/v1"
SAMPLE_RATE = 16000
FRAME_BYTES = 1280
MAX_AUDIO_BYTES = SAMPLE_RATE * 2 * 59

sys.path.insert(0, str(PYTHON_PACKAGES))


class XfyunSlmError(RuntimeError):
    pass


def default_config_path():
    if LOCAL_CONFIG.is_file():
        return LOCAL_CONFIG
    if SHARED_CONFIG.is_file():
        return SHARED_CONFIG
    return LOCAL_CONFIG


def load_config(path):
    values = {}
    path = Path(path)
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip("\"'")

    keys = ("XFYUN_APP_ID", "XFYUN_API_KEY", "XFYUN_API_SECRET")
    return {key: os.environ.get(key) or values.get(key, "") for key in keys}


def create_xfyun_auth_url(
    api_key,
    api_secret,
    date=None,
    *,
    url=XFYUN_SLM_URL,
    host=XFYUN_SLM_HOST,
    path=XFYUN_SLM_PATH,
):
    date = date or formatdate(timeval=None, localtime=False, usegmt=True)
    signature_origin = (
        f"host: {host}\n"
        f"date: {date}\n"
        f"GET {path} HTTP/1.1"
    )
    signature = base64.b64encode(
        hmac.new(
            api_secret.encode("utf-8"),
            signature_origin.encode("utf-8"),
            hashlib.sha256,
        ).digest()
    ).decode("ascii")
    authorization_origin = (
        f'api_key="{api_key}",algorithm="hmac-sha256",'
        f'headers="host date request-line",signature="{signature}"'
    )
    authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode("ascii")
    return f"{url}?{urlencode({'authorization': authorization, 'date': date, 'host': host})}"


class StreamingResult:
    def __init__(self):
        self.parts = {}

    @property
    def text(self):
        return "".join(self.parts[index] for index in sorted(self.parts))

    def update(self, result):
        words = []
        for segment in result.get("ws", []):
            candidates = segment.get("cw", [])
            if candidates:
                words.append(candidates[0].get("w", ""))
        text = "".join(words)
        sequence = int(result.get("sn", len(self.parts)))

        if result.get("pgs") == "rpl":
            replace_range = result.get("rg", [])
            if len(replace_range) == 2:
                for index in range(int(replace_range[0]), int(replace_range[1]) + 1):
                    self.parts.pop(index, None)
        self.parts[sequence] = text
        return self.text


class XfyunSlmRecognizer:
    service_name = "讯飞中文识别大模型"

    def __init__(self, config_path=None, eos=2000, timeout=20, connector=None):
        config_path = Path(config_path) if config_path else default_config_path()
        config = load_config(config_path)
        self.app_id = config["XFYUN_APP_ID"]
        self.api_key = config["XFYUN_API_KEY"]
        self.api_secret = config["XFYUN_API_SECRET"]
        self.eos = eos
        self.timeout = timeout
        self.connector = connector

        if not self.app_id or not self.api_key or not self.api_secret:
            raise XfyunSlmError(f"配置文件缺少讯飞识别凭据: {config_path}")

    def auth_url(self):
        return create_xfyun_auth_url(self.api_key, self.api_secret)

    def _frame(self, audio, status, sequence):
        frame = {
            "header": {"app_id": self.app_id, "status": status},
            "payload": {
                "audio": {
                    "encoding": "raw",
                    "sample_rate": SAMPLE_RATE,
                    "channels": 1,
                    "bit_depth": 16,
                    "seq": sequence,
                    "status": status,
                    "audio": base64.b64encode(audio).decode("ascii"),
                }
            },
        }
        if status == 0:
            frame["parameter"] = {
                "iat": {
                    "domain": "slm",
                    "language": "zh_cn",
                    "accent": "mandarin",
                    "eos": self.eos,
                    "dwa": "wpgs",
                    "result": {"encoding": "utf8", "compress": "raw", "format": "json"},
                }
            }
        return frame

    def _handle_response(self, raw_message, result, verbose=False):
        if isinstance(raw_message, bytes):
            raw_message = raw_message.decode("utf-8")
        message = json.loads(raw_message)
        header = message.get("header") or {}
        code = int(header.get("code", 0))
        if code != 0:
            description = header.get("message") or "未知错误"
            raise XfyunSlmError(f"{self.service_name}失败，错误码 {code}: {description}")

        encoded_text = ((message.get("payload") or {}).get("result") or {}).get("text")
        if encoded_text:
            decoded = json.loads(base64.b64decode(encoded_text).decode("utf-8"))
            service_code = int(decoded.get("ret", 0))
            if service_code != 0:
                raise XfyunSlmError(f"{self.service_name}失败，服务错误码 {service_code}")
            current = result.update(decoded)
            if verbose and current:
                print(f"临时结果: {current}", file=sys.stderr)
        return int(header.get("status", 0)) == 2

    def _drain(self, connection, result, wait, verbose=False):
        while True:
            try:
                message = connection.recv(timeout=wait)
            except TimeoutError:
                return False
            if self._handle_response(message, result, verbose):
                return True
            wait = 0

    def recognize_chunks(self, chunks, pace=False, verbose=False):
        connector = self.connector
        if connector is None:
            try:
                from websockets.sync.client import connect
            except ImportError as error:
                raise XfyunSlmError("缺少 websockets，请安装 requirements.txt 中的依赖") from error
            connector = connect

        connection = None
        result = StreamingResult()
        sent_bytes = 0
        sequence = 1
        finished = False
        try:
            connection = connector(
                self.auth_url(),
                open_timeout=self.timeout,
                close_timeout=5,
            )
            for chunk in chunks:
                if finished or sent_bytes >= MAX_AUDIO_BYTES:
                    break
                if not chunk:
                    continue
                remaining = MAX_AUDIO_BYTES - sent_bytes
                chunk = chunk[:remaining]
                status = 0 if sequence == 1 else 1
                connection.send(json.dumps(self._frame(chunk, status, sequence), ensure_ascii=False))
                sent_bytes += len(chunk)
                sequence += 1
                finished = self._drain(connection, result, 0.001, verbose)
                if sent_bytes >= MAX_AUDIO_BYTES:
                    break
                if pace and not finished:
                    time.sleep(len(chunk) / (SAMPLE_RATE * 2))

            if sent_bytes == 0:
                raise XfyunSlmError("音频内容为空")
            if not finished:
                connection.send(json.dumps(self._frame(b"", 2, sequence), ensure_ascii=False))
                deadline = time.monotonic() + self.timeout
                while not finished:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise XfyunSlmError(f"等待{self.service_name}结果超时")
                    try:
                        message = connection.recv(timeout=remaining)
                    except TimeoutError as error:
                        raise XfyunSlmError(f"等待{self.service_name}结果超时") from error
                    finished = self._handle_response(message, result, verbose)
        except XfyunSlmError:
            raise
        except Exception as error:
            raise XfyunSlmError(f"无法连接{self.service_name}: {type(error).__name__}") from error
        finally:
            if connection is not None:
                connection.close()
        return result.text, None
