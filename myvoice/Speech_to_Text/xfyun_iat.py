#!/usr/bin/env python3

import base64
import json
import sys

from xfyun_slm import XfyunSlmError, XfyunSlmRecognizer, create_xfyun_auth_url


XFYUN_IAT_URL = "wss://iat-api.xfyun.cn/v2/iat"
XFYUN_IAT_HOST = "iat-api.xfyun.cn"
XFYUN_IAT_PATH = "/v2/iat"


class XfyunIatRecognizer(XfyunSlmRecognizer):
    service_name = "讯飞语音听写"

    def auth_url(self):
        return create_xfyun_auth_url(
            self.api_key,
            self.api_secret,
            url=XFYUN_IAT_URL,
            host=XFYUN_IAT_HOST,
            path=XFYUN_IAT_PATH,
        )

    def _frame(self, audio, status, sequence):
        frame = {
            "data": {
                "status": status,
                "format": "audio/L16;rate=16000",
                "encoding": "raw",
                "audio": base64.b64encode(audio).decode("ascii"),
            }
        }
        if status == 0:
            frame["common"] = {"app_id": self.app_id}
            frame["business"] = {
                "language": "zh_cn",
                "domain": "iat",
                "accent": "mandarin",
                "vad_eos": self.eos,
                "dwa": "wpgs",
                "ptt": 1,
            }
        return frame

    def _handle_response(self, raw_message, result, verbose=False):
        if isinstance(raw_message, bytes):
            raw_message = raw_message.decode("utf-8")
        message = json.loads(raw_message)
        code = int(message.get("code", -1))
        if code != 0:
            description = message.get("message") or "未知错误"
            raise XfyunSlmError(f"{self.service_name}失败，错误码 {code}: {description}")

        data = message.get("data") or {}
        response_result = data.get("result")
        if response_result:
            current = result.update(response_result)
            if verbose and current:
                print(f"临时结果: {current}", file=sys.stderr)
        return int(data.get("status", 0)) == 2
