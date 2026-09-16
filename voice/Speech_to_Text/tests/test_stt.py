import base64
import json
import tempfile
import unittest
import wave
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import stt
import xfyun_iat
import xfyun_slm


class FakeRecognizer:
    def __init__(self, model, rate):
        self.bytes_received = 0

    def SetWords(self, enabled):
        pass

    def AcceptWaveform(self, chunk):
        self.bytes_received += len(chunk)
        return False

    def FinalResult(self):
        return json.dumps(
            {"text": "你 好 世 界", "result": [{"conf": 0.8}, {"conf": 1.0}]},
            ensure_ascii=False,
        )


class FakeSlmConnection:
    def __init__(self):
        self.sent = []
        self.partial_returned = False
        self.final_returned = False
        self.closed = False

    def send(self, message):
        self.sent.append(json.loads(message))

    def recv(self, timeout=None):
        if len(self.sent) == 1 and not self.partial_returned:
            self.partial_returned = True
            result = {
                "sn": 0,
                "ls": False,
                "pgs": "apd",
                "ws": [{"cw": [{"w": "你好"}]}],
            }
            return json.dumps(
                {
                    "header": {"code": 0, "status": 1},
                    "payload": {
                        "result": {
                            "text": base64.b64encode(
                                json.dumps(result, ensure_ascii=False).encode("utf-8")
                            ).decode("ascii")
                        }
                    },
                }
            )
        if self.sent[-1]["header"]["status"] == 2 and not self.final_returned:
            self.final_returned = True
            return json.dumps({"header": {"code": 0, "status": 2}})
        raise TimeoutError

    def close(self):
        self.closed = True


class FakeIatConnection(FakeSlmConnection):
    def recv(self, timeout=None):
        if len(self.sent) == 1 and not self.partial_returned:
            self.partial_returned = True
            return json.dumps(
                {
                    "code": 0,
                    "message": "success",
                    "data": {
                        "status": 1,
                        "result": {
                            "sn": 0,
                            "ls": False,
                            "pgs": "apd",
                            "ws": [{"cw": [{"w": "语音听写"}]}],
                        },
                    },
                },
                ensure_ascii=False,
            )
        if self.sent[-1]["data"]["status"] == 2 and not self.final_returned:
            self.final_returned = True
            return json.dumps({"code": 0, "message": "success", "data": {"status": 2}})
        raise TimeoutError


class SpeechToTextTest(unittest.TestCase):
    def test_normalize_chinese_text(self):
        self.assertEqual(stt.normalize_text("你 好 世 界"), "你好世界")

    def test_recognize_pcm(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "voice.pcm"
            path.write_bytes(b"\0\0" * 1600)
            text, confidence = stt.recognize_file(path, object(), FakeRecognizer)
        self.assertEqual(text, "你好世界")
        self.assertAlmostEqual(confidence, 0.9)

    def test_recognize_wav(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "voice.wav"
            with wave.open(str(path), "wb") as output:
                output.setnchannels(1)
                output.setsampwidth(2)
                output.setframerate(16000)
                output.writeframes(b"\0\0" * 1600)
            text, _ = stt.recognize_file(path, object(), FakeRecognizer)
        self.assertEqual(text, "你好世界")

    def test_xfyun_auth_url(self):
        url = xfyun_slm.create_xfyun_auth_url(
            "test-key",
            "test-secret",
            "Tue, 14 May 2024 08:46:48 GMT",
        )
        query = parse_qs(urlparse(url).query)
        authorization = base64.b64decode(query["authorization"][0]).decode("utf-8")
        self.assertEqual(urlparse(url).netloc, "iat.xf-yun.com")
        self.assertIn('api_key="test-key"', authorization)
        self.assertNotIn("test-secret", url)

    def test_xfyun_slm_request_and_result(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "iflytek.env"
            config.write_text(
                "XFYUN_APP_ID=test-app\n"
                "XFYUN_API_KEY=test-key\n"
                "XFYUN_API_SECRET=test-secret\n",
                encoding="utf-8",
            )
            connection = FakeSlmConnection()
            engine = xfyun_slm.XfyunSlmRecognizer(
                config,
                connector=lambda *args, **kwargs: connection,
            )
            text, confidence = engine.recognize_chunks([b"\0\0" * 640])

        first = connection.sent[0]
        self.assertEqual(first["parameter"]["iat"]["domain"], "slm")
        self.assertEqual(first["parameter"]["iat"]["language"], "zh_cn")
        self.assertEqual(first["payload"]["audio"]["status"], 0)
        self.assertEqual(connection.sent[-1]["payload"]["audio"]["status"], 2)
        self.assertEqual(text, "你好")
        self.assertIsNone(confidence)
        self.assertTrue(connection.closed)

    def test_xfyun_iat_request_and_result(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "iflytek.env"
            config.write_text(
                "XFYUN_APP_ID=test-app\n"
                "XFYUN_API_KEY=test-key\n"
                "XFYUN_API_SECRET=test-secret\n",
                encoding="utf-8",
            )
            connection = FakeIatConnection()
            engine = xfyun_iat.XfyunIatRecognizer(
                config,
                connector=lambda *args, **kwargs: connection,
            )
            text, confidence = engine.recognize_chunks([b"\0\0" * 640])

        first = connection.sent[0]
        self.assertEqual(first["business"]["domain"], "iat")
        self.assertEqual(first["business"]["language"], "zh_cn")
        self.assertEqual(first["data"]["status"], 0)
        self.assertEqual(connection.sent[-1]["data"]["status"], 2)
        self.assertEqual(urlparse(engine.auth_url()).netloc, "iat-api.xfyun.cn")
        self.assertEqual(text, "语音听写")
        self.assertIsNone(confidence)
        self.assertTrue(connection.closed)

    def test_streaming_result_replacement(self):
        result = xfyun_slm.StreamingResult()
        result.update({"sn": 0, "pgs": "apd", "ws": [{"cw": [{"w": "你好"}]}]})
        result.update({"sn": 1, "pgs": "apd", "ws": [{"cw": [{"w": "世界"}]}]})
        text = result.update(
            {"sn": 2, "pgs": "rpl", "rg": [1, 1], "ws": [{"cw": [{"w": "小薇"}]}]}
        )
        self.assertEqual(text, "你好小薇")


if __name__ == "__main__":
    unittest.main()
