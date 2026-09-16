#!/usr/bin/env python3

import argparse
import json
import os
import re
import select
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path

from xfyun_iat import XfyunIatRecognizer
from xfyun_slm import FRAME_BYTES, MAX_AUDIO_BYTES, XfyunSlmRecognizer, default_config_path


ROOT = Path(__file__).resolve().parent
PYTHON_PACKAGES = ROOT / "third_party" / "python"
DEFAULT_MODEL = ROOT / "models" / "vosk-model-small-cn-0.22"
DEFAULT_DEVICE = "plughw:CARD=XFMDPV0018,DEV=0"
SAMPLE_RATE = 16000
CHUNK_BYTES = 8000

sys.path.insert(0, str(PYTHON_PACKAGES))


def parse_args():
    parser = argparse.ArgumentParser(description="M260C 语音转文字")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--record", action="store_true", help="从 M260C 实时录音")
    source.add_argument("--file", type=Path, help="识别 PCM 或 WAV 文件")
    source.add_argument("--list-devices", action="store_true", help="列出 ALSA 录音设备")
    parser.add_argument("--device", default=DEFAULT_DEVICE, help="ALSA 录音设备")
    parser.add_argument(
        "--engine",
        choices=("iat", "slm", "offline"),
        default="iat",
        help="识别引擎，默认 iat 语音听写",
    )
    parser.add_argument("--offline", action="store_true", help="使用 Vosk 离线识别")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL, help="Vosk 离线模型目录")
    parser.add_argument("--config", type=Path, default=default_config_path(), help="讯飞凭据配置文件")
    parser.add_argument("--timeout", type=float, help="设置单次录音最长秒数")
    parser.add_argument("--continuous", action="store_true", help="持续监听，与默认录音模式相同")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--verbose", action="store_true", help="显示识别过程")
    args = parser.parse_args()
    if args.timeout is not None and args.timeout <= 0:
        parser.error("--timeout 必须大于 0")
    if args.continuous and not args.record:
        parser.error("--continuous 只能与 --record 一起使用")
    if args.continuous and args.timeout is not None:
        parser.error("--continuous 不能与 --timeout 同时使用")
    if args.offline:
        args.engine = "offline"
    return args


def load_vosk(model_path, verbose):
    try:
        from vosk import KaldiRecognizer, Model, SetLogLevel
    except ImportError as error:
        raise RuntimeError("缺少本地 Vosk 依赖，请先执行 README 中的安装命令") from error

    if not model_path.is_dir():
        raise RuntimeError(f"找不到离线模型: {model_path}")
    SetLogLevel(0 if verbose else -1)
    return Model(str(model_path)), KaldiRecognizer


def normalize_text(text):
    text = text.strip()
    return re.sub(r"(?<=[\u3400-\u9fff])\s+(?=[\u3400-\u9fff])", "", text)


def collect_result(payload, texts, confidences, verbose=False):
    result = json.loads(payload)
    text = normalize_text(result.get("text", ""))
    if text:
        texts.append(text)
    for word in result.get("result", []):
        if "conf" in word:
            confidences.append(float(word["conf"]))
    if verbose and (text or result.get("partial")):
        print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
    return text


def create_recognizer(model, recognizer_class):
    recognizer = recognizer_class(model, SAMPLE_RATE)
    recognizer.SetWords(True)
    return recognizer


def recognize_pcm_stream(stream, recognizer, verbose=False, stop_after_utterance=False, deadline=None):
    texts = []
    confidences = []

    while True:
        if deadline is not None and time.monotonic() >= deadline:
            break
        chunk = stream.read(CHUNK_BYTES)
        if not chunk:
            break
        if recognizer.AcceptWaveform(chunk):
            text = collect_result(recognizer.Result(), texts, confidences, verbose)
            if stop_after_utterance and text:
                break

    collect_result(recognizer.FinalResult(), texts, confidences, verbose)
    confidence = sum(confidences) / len(confidences) if confidences else 0.0
    return normalize_text(" ".join(texts)), confidence


def recognize_file(path, model, recognizer_class, verbose=False):
    recognizer = create_recognizer(model, recognizer_class)
    if path.suffix.lower() != ".wav":
        with path.open("rb") as stream:
            return recognize_pcm_stream(stream, recognizer, verbose)

    with wave.open(str(path), "rb") as stream:
        if (stream.getnchannels(), stream.getsampwidth(), stream.getframerate(), stream.getcomptype()) != (
            1,
            2,
            SAMPLE_RATE,
            "NONE",
        ):
            raise RuntimeError("WAV 必须是 16kHz、单声道、16位 PCM")

        class WavePcmStream:
            def read(self, byte_count):
                return stream.readframes(byte_count // 2)

        return recognize_pcm_stream(WavePcmStream(), recognizer, verbose)


def iter_file_pcm(path):
    if path.suffix.lower() != ".wav":
        with path.open("rb") as stream:
            while True:
                chunk = stream.read(FRAME_BYTES)
                if not chunk:
                    return
                yield chunk
        return

    with wave.open(str(path), "rb") as stream:
        if (stream.getnchannels(), stream.getsampwidth(), stream.getframerate(), stream.getcomptype()) != (
            1,
            2,
            SAMPLE_RATE,
            "NONE",
        ):
            raise RuntimeError("WAV 必须是 16kHz、单声道、16位 PCM")
        while True:
            chunk = stream.readframes(FRAME_BYTES // 2)
            if not chunk:
                return
            yield chunk


def stop_process(process):
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def start_microphone(device):
    if not shutil.which("arecord"):
        raise RuntimeError("找不到 arecord，请安装 alsa-utils")
    command = [
        "arecord",
        "-q",
        "-D",
        device,
        "-t",
        "raw",
        "-f",
        "S16_LE",
        "-c",
        "1",
        "-r",
        str(SAMPLE_RATE),
    ]
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def iter_microphone_pcm(process, deadline=None):
    while deadline is None or time.monotonic() < deadline:
        if process.poll() is not None:
            error = process.stderr.read().decode("utf-8", errors="replace").strip()
            raise RuntimeError(error or "录音进程意外退出")
        readable, _, _ = select.select([process.stdout], [], [], 0.1)
        if not readable:
            continue
        chunk = os.read(process.stdout.fileno(), FRAME_BYTES)
        if not chunk:
            return
        yield chunk


def recognize_online_file(path, engine, verbose=False):
    if path.suffix.lower() == ".wav":
        with wave.open(str(path), "rb") as stream:
            pcm_bytes = stream.getnframes() * stream.getsampwidth() * stream.getnchannels()
    else:
        pcm_bytes = path.stat().st_size
    if pcm_bytes > MAX_AUDIO_BYTES:
        raise RuntimeError("讯飞在线识别的单个音频不能超过 60 秒")
    return engine.recognize_chunks(iter_file_pcm(path), pace=True, verbose=verbose)


def recognize_online_microphone(device, timeout, engine, verbose=False):
    process = start_microphone(device)
    deadline = time.monotonic() + timeout if timeout is not None else None
    try:
        return engine.recognize_chunks(
            iter_microphone_pcm(process, deadline),
            pace=False,
            verbose=verbose,
        )
    finally:
        stop_process(process)


def recognize_online_microphone_continuous(device, engine, as_json=False, verbose=False):
    process = start_microphone(device)
    if not as_json:
        print(f"{engine.service_name}持续监听中，按 Ctrl+C 停止……", file=sys.stderr)
    try:
        while True:
            text, confidence = engine.recognize_chunks(
                iter_microphone_pcm(process),
                pace=False,
                verbose=verbose,
            )
            if text:
                print_result(text, confidence, as_json)
    finally:
        stop_process(process)


def recognize_microphone(device, timeout, model, recognizer_class, verbose=False):
    if not shutil.which("arecord"):
        raise RuntimeError("找不到 arecord，请安装 alsa-utils")

    command = [
        "arecord",
        "-q",
        "-D",
        device,
        "-t",
        "raw",
        "-f",
        "S16_LE",
        "-c",
        "1",
        "-r",
        str(SAMPLE_RATE),
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    recognizer = create_recognizer(model, recognizer_class)
    texts = []
    confidences = []
    deadline = time.monotonic() + timeout

    if not verbose:
        print("正在监听，请讲话……", file=sys.stderr)
    try:
        while time.monotonic() < deadline:
            if process.poll() is not None:
                error = process.stderr.read().decode("utf-8", errors="replace").strip()
                raise RuntimeError(error or "录音进程意外退出")
            readable, _, _ = select.select([process.stdout], [], [], 0.1)
            if not readable:
                continue
            chunk = os.read(process.stdout.fileno(), CHUNK_BYTES)
            if not chunk:
                break
            if recognizer.AcceptWaveform(chunk):
                text = collect_result(recognizer.Result(), texts, confidences, verbose)
                if text:
                    break
            elif verbose:
                partial = json.loads(recognizer.PartialResult()).get("partial", "")
                if partial:
                    print(f"临时结果: {normalize_text(partial)}", file=sys.stderr)
    finally:
        stop_process(process)

    if not texts:
        collect_result(recognizer.FinalResult(), texts, confidences, verbose)
    confidence = sum(confidences) / len(confidences) if confidences else 0.0
    return normalize_text(" ".join(texts)), confidence


def recognize_microphone_continuous(device, model, recognizer_class, as_json=False, verbose=False):
    if not shutil.which("arecord"):
        raise RuntimeError("找不到 arecord，请安装 alsa-utils")

    command = [
        "arecord",
        "-q",
        "-D",
        device,
        "-t",
        "raw",
        "-f",
        "S16_LE",
        "-c",
        "1",
        "-r",
        str(SAMPLE_RATE),
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    recognizer = create_recognizer(model, recognizer_class)
    if not as_json:
        print("持续监听中，按 Ctrl+C 停止……", file=sys.stderr)

    try:
        while True:
            if process.poll() is not None:
                error = process.stderr.read().decode("utf-8", errors="replace").strip()
                raise RuntimeError(error or "录音进程意外退出")
            readable, _, _ = select.select([process.stdout], [], [], 0.1)
            if not readable:
                continue
            chunk = os.read(process.stdout.fileno(), CHUNK_BYTES)
            if not chunk:
                break
            if recognizer.AcceptWaveform(chunk):
                texts = []
                confidences = []
                text = collect_result(recognizer.Result(), texts, confidences, verbose)
                if text:
                    confidence = sum(confidences) / len(confidences) if confidences else 0.0
                    print_result(text, confidence, as_json)
            elif verbose:
                partial = json.loads(recognizer.PartialResult()).get("partial", "")
                if partial:
                    print(f"临时结果: {normalize_text(partial)}", file=sys.stderr)
    finally:
        stop_process(process)
    return 0


def list_devices():
    result = subprocess.run(["arecord", "-L"], check=False, text=True)
    return result.returncode


def print_result(text, confidence, as_json):
    status = "ok" if text else "no_match"
    if as_json:
        print(
            json.dumps(
                {
                    "status": status,
                    "text": text,
                    "confidence": round(confidence, 3) if confidence is not None else None,
                },
                ensure_ascii=False,
            ),
            flush=True,
        )
    elif text:
        print(f"识别结果: {text}")
        if confidence is not None:
            print(f"置信度: {confidence:.3f}", flush=True)
    else:
        print("未识别到有效语音", flush=True)
    return 0 if text else 2


def main():
    args = parse_args()
    if args.list_devices:
        return list_devices()

    if args.file and not args.file.is_file():
        raise RuntimeError(f"找不到音频文件: {args.file}")

    if args.engine == "offline":
        model, recognizer_class = load_vosk(args.model.resolve(), args.verbose)
        if args.record and args.timeout is None:
            return recognize_microphone_continuous(
                args.device, model, recognizer_class, args.json, args.verbose
            )
        if args.record:
            text, confidence = recognize_microphone(
                args.device, args.timeout, model, recognizer_class, args.verbose
            )
        else:
            text, confidence = recognize_file(args.file, model, recognizer_class, args.verbose)
    else:
        engine_class = XfyunIatRecognizer if args.engine == "iat" else XfyunSlmRecognizer
        engine = engine_class(args.config)
        if args.record and args.timeout is None:
            return recognize_online_microphone_continuous(
                args.device, engine, args.json, args.verbose
            )
        if args.record:
            text, confidence = recognize_online_microphone(
                args.device, args.timeout, engine, args.verbose
            )
        else:
            text, confidence = recognize_online_file(args.file, engine, args.verbose)
    return print_result(text, confidence, args.json)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("已停止", file=sys.stderr)
        raise SystemExit(130)
    except (OSError, RuntimeError, wave.Error) as error:
        print(f"错误: {error}", file=sys.stderr)
        raise SystemExit(1)
