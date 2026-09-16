import base64
import json
import subprocess
import sys
import tempfile
import types
import unittest
import wave
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import tts


class TextToSpeechTests(unittest.TestCase):
    def test_chinese_text_creates_pcm_wav(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "test.wav"
            path, sample_rate, duration = tts.synthesize_to_wav("你好，这是测试。", output)

            self.assertEqual(path, output.resolve())
            self.assertGreater(duration, 0)
            with wave.open(str(path), "rb") as stream:
                self.assertEqual(stream.getnchannels(), 1)
                self.assertEqual(stream.getsampwidth(), 2)
                self.assertEqual(stream.getframerate(), sample_rate)
                self.assertGreater(stream.getnframes(), 0)

    def test_cli_json_without_playback(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "cli.wav"
            result = subprocess.run(
                [
                    str(ROOT / "tts"),
                    "语音播报测试",
                    "--engine",
                    "espeak",
                    "--no-play",
                    "--json",
                    "--output",
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('"status": "ok"', result.stdout)
            self.assertTrue(output.is_file())

    def test_empty_text_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(tts.TtsError):
                tts.synthesize_to_wav("   ", Path(directory) / "empty.wav")

    def test_xfyun_auth_url_does_not_expose_secret(self):
        url = tts.create_xfyun_auth_url("test-key", "test-secret")
        self.assertTrue(url.startswith("wss://tts-api.xfyun.cn/v2/tts?"))
        self.assertNotIn("test-secret", url)

    def test_online_engine_collects_pcm(self):
        class FakeConnection:
            def __init__(self):
                self.request = None

            def send(self, request):
                self.request = json.loads(request)

            def recv(self):
                return json.dumps(
                    {
                        "code": 0,
                        "data": {
                            "audio": base64.b64encode(b"\x01\x02\x03\x04").decode("ascii"),
                            "status": 2,
                        },
                    }
                )

            def close(self):
                pass

        connection = FakeConnection()
        websocket_module = types.SimpleNamespace(create_connection=lambda *_args, **_kwargs: connection)
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "iflytek.env"
            config.write_text(
                "XFYUN_APP_ID=test-app\nXFYUN_API_KEY=test-key\nXFYUN_API_SECRET=test-secret\n",
                encoding="utf-8",
            )
            with mock.patch.dict(sys.modules, {"websocket": websocket_module}):
                engine = tts.XfyunOnline(config)
                audio = engine.synthesize("你好")

        self.assertEqual(audio, b"\x01\x02\x03\x04")
        self.assertEqual(connection.request["business"]["vcn"], "x4_yezi")
        self.assertEqual(connection.request["data"]["status"], 2)


if __name__ == "__main__":
    unittest.main()
