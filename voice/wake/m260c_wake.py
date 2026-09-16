#!/usr/bin/env python3
"""Standalone wake-up event monitor for WHEELTEC M260C microphones."""

from __future__ import annotations

import argparse
import json
import os
import select
import struct
import sys
import termios
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


FRAME_HEADER = 0xA5
USER_ID = 0x01
HANDSHAKE_MESSAGE = 0x01
DEVICE_MESSAGE = 0x04
CONTROL_MESSAGE = 0x05
HANDSHAKE_ACK = 0xFF
HEADER_SIZE = 7
MAX_PAYLOAD_SIZE = 10232
HANDSHAKE_PAYLOAD = bytes((0xA5, 0x00, 0x00, 0x00))


def calculate_checksum(data: bytes) -> int:
    """Return the protocol's two's-complement checksum."""
    return (-sum(data)) & 0xFF


def encode_frame(msg_type: int, message_id: int, payload: bytes) -> bytes:
    """Build one M260C protocol frame."""
    header = struct.pack(
        "<BBBHH", FRAME_HEADER, USER_ID, msg_type, len(payload), message_id
    )
    body = header + payload
    return body + bytes((calculate_checksum(body),))


@dataclass(frozen=True)
class Frame:
    msg_type: int
    message_id: int
    payload: bytes


class FrameParser:
    """Incrementally split and validate frames from a serial byte stream."""

    def __init__(self, max_payload_size: int = MAX_PAYLOAD_SIZE) -> None:
        self._buffer = bytearray()
        self._max_payload_size = max_payload_size

    def feed(self, data: bytes) -> List[Frame]:
        self._buffer.extend(data)
        frames: List[Frame] = []
        marker = bytes((FRAME_HEADER, USER_ID))

        while True:
            start = self._buffer.find(marker)
            if start < 0:
                if self._buffer.endswith(bytes((FRAME_HEADER,))):
                    self._buffer[:] = bytes((FRAME_HEADER,))
                else:
                    self._buffer.clear()
                break

            if start:
                del self._buffer[:start]

            if len(self._buffer) < HEADER_SIZE:
                break

            payload_size = int.from_bytes(self._buffer[3:5], "little")
            if payload_size > self._max_payload_size:
                del self._buffer[0]
                continue

            frame_size = HEADER_SIZE + payload_size + 1
            if len(self._buffer) < frame_size:
                break

            raw_frame = bytes(self._buffer[:frame_size])
            if calculate_checksum(raw_frame[:-1]) != raw_frame[-1]:
                del self._buffer[0]
                continue

            frames.append(
                Frame(
                    msg_type=raw_frame[2],
                    message_id=int.from_bytes(raw_frame[5:7], "little"),
                    payload=raw_frame[7:-1],
                )
            )
            del self._buffer[:frame_size]

        return frames


@dataclass(frozen=True)
class WakeEvent:
    message_id: int
    timestamp: float
    keyword: Optional[str] = None
    angle_deg: Optional[float] = None
    beam: Optional[int] = None
    confidence: Optional[float] = None

    def as_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "event": "wake",
            "timestamp": self.timestamp,
            "message_id": self.message_id,
        }
        if self.keyword is not None:
            result["keyword"] = self.keyword
        if self.angle_deg is not None:
            result["angle_deg"] = self.angle_deg
        if self.beam is not None:
            result["beam"] = self.beam
        if self.confidence is not None:
            result["confidence"] = self.confidence
        return result


def _as_object(value: Any) -> Dict[str, Any]:
    current = value
    for _ in range(2):
        if isinstance(current, dict):
            return current
        if not isinstance(current, str):
            return {}
        try:
            current = json.loads(current)
        except json.JSONDecodeError:
            return {}
    return current if isinstance(current, dict) else {}


def _first_value(objects: List[Dict[str, Any]], names: List[str]) -> Any:
    for obj in objects:
        for name in names:
            if name in obj and obj[name] is not None:
                return obj[name]
    return None


def _as_float(value: Any) -> Optional[float]:
    if isinstance(value, bool) or value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _as_int(value: Any) -> Optional[int]:
    number = _as_float(value)
    return int(number) if number is not None else None


def parse_wake_event(frame: Frame, timestamp: Optional[float] = None) -> Optional[WakeEvent]:
    """Convert an M260C device frame into a normalized wake-up event."""
    if frame.msg_type != DEVICE_MESSAGE:
        return None

    try:
        message = json.loads(frame.payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None

    if not isinstance(message, dict) or message.get("type") != "aiui_event":
        return None

    content = _as_object(message.get("content"))
    event_type = content.get("eventType")
    if event_type is not None and str(event_type) != "4":
        return None

    info = _as_object(content.get("info"))
    info_ivw = _as_object(info.get("ivw"))
    result = _as_object(content.get("result"))
    result_ivw = _as_object(result.get("ivw"))
    sources = [content, info, info_ivw, result, result_ivw]

    keyword = _first_value(sources, ["keyword", "wakeup_keyword", "word"])
    angle = _as_float(_first_value(sources, ["angle", "angle_deg"]))
    beam = _as_int(_first_value(sources, ["beam", "arg1"]))
    confidence = _as_float(_first_value(sources, ["confidence", "score"]))

    return WakeEvent(
        message_id=frame.message_id,
        timestamp=time.time() if timestamp is None else timestamp,
        keyword=str(keyword) if keyword is not None else None,
        angle_deg=angle,
        beam=beam,
        confidence=confidence,
    )


class LinuxSerialPort:
    """Small Linux 8N1 serial transport implemented with the standard library."""

    _BAUD_RATES = {
        9600: termios.B9600,
        19200: termios.B19200,
        38400: termios.B38400,
        57600: termios.B57600,
        115200: termios.B115200,
    }

    def __init__(self, path: str, baudrate: int) -> None:
        self.path = path
        self.baudrate = baudrate
        self.fd: Optional[int] = None

    def __enter__(self) -> "LinuxSerialPort":
        speed = self._BAUD_RATES.get(self.baudrate)
        if speed is None:
            raise ValueError(f"不支持的波特率: {self.baudrate}")

        self.fd = os.open(self.path, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attributes = termios.tcgetattr(self.fd)
        attributes[0] = 0
        attributes[1] = 0
        attributes[2] = termios.CLOCAL | termios.CREAD | termios.CS8
        attributes[3] = 0
        attributes[4] = speed
        attributes[5] = speed
        attributes[6][termios.VMIN] = 0
        attributes[6][termios.VTIME] = 0
        termios.tcsetattr(self.fd, termios.TCSANOW, attributes)
        termios.tcflush(self.fd, termios.TCIOFLUSH)
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def read(self, timeout: float = 0.2) -> bytes:
        if self.fd is None:
            raise RuntimeError("串口未打开")
        readable, _, _ = select.select([self.fd], [], [], timeout)
        if not readable:
            return b""
        data = os.read(self.fd, 4096)
        if not data:
            raise ConnectionResetError("串口设备已断开")
        return data

    def write(self, data: bytes, timeout: float = 1.0) -> None:
        if self.fd is None:
            raise RuntimeError("串口未打开")

        pending = memoryview(data)
        deadline = time.monotonic() + timeout
        while pending:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("串口写入超时")
            _, writable, _ = select.select([], [self.fd], [], remaining)
            if not writable:
                raise TimeoutError("串口写入超时")
            written = os.write(self.fd, pending)
            pending = pending[written:]


def format_event(event: WakeEvent, json_output: bool) -> str:
    if json_output:
        return json.dumps(event.as_dict(), ensure_ascii=False, separators=(",", ":"))

    fields = ["WAKE"]
    if event.keyword is not None:
        fields.append(f"keyword={event.keyword}")
    if event.angle_deg is not None:
        fields.append(f"angle={event.angle_deg:g}°")
    if event.beam is not None:
        fields.append(f"beam={event.beam}")
    if event.confidence is not None:
        fields.append(f"confidence={event.confidence:g}")
    return " ".join(fields)


def _payload_text(payload: bytes) -> str:
    try:
        return payload.decode("utf-8")
    except UnicodeDecodeError:
        return payload.hex()


def make_wake_word_payload(keyword: str, threshold: int) -> bytes:
    keyword = keyword.strip()
    if not keyword:
        raise ValueError("唤醒词不能为空")
    if not 500 <= threshold <= 1500:
        raise ValueError("唤醒阈值必须在 500 到 1500 之间")

    message = {
        "type": "wakeup_keywords",
        "content": {"keyword": keyword, "threshold": str(threshold)},
    }
    return json.dumps(message, ensure_ascii=False, separators=(",", ":")).encode(
        "utf-8"
    )


def set_wake_word(
    port: str,
    baudrate: int,
    keyword: str,
    threshold: int,
    timeout: float,
    verbose: bool,
) -> int:
    """Set one wake word and wait for the device acknowledgement."""
    parser = FrameParser()
    request_id = 1
    request = encode_frame(
        CONTROL_MESSAGE,
        request_id,
        make_wake_word_payload(keyword, threshold),
    )
    started = time.monotonic()
    request_sent = False

    with LinuxSerialPort(port, baudrate) as serial_port:
        while time.monotonic() - started < timeout:
            try:
                data = serial_port.read()
            except ConnectionResetError:
                if request_sent:
                    print("设备已重启，唤醒词设置完成")
                    return 0
                raise

            for frame in parser.feed(data):
                if verbose:
                    print(
                        f"收到帧 type=0x{frame.msg_type:02X} "
                        f"id={frame.message_id} payload={_payload_text(frame.payload)}"
                    )
                if frame.msg_type == HANDSHAKE_MESSAGE:
                    serial_port.write(
                        encode_frame(HANDSHAKE_ACK, frame.message_id, HANDSHAKE_PAYLOAD)
                    )
                    if not request_sent:
                        serial_port.write(request)
                        request_sent = True
                        print(f"已发送唤醒词设置: {keyword}，阈值: {threshold}")
                    continue

                if frame.message_id != request_id:
                    continue

                if frame.msg_type == HANDSHAKE_ACK:
                    print("设置指令已被设备接收，请等待设备重启后测试新唤醒词")
                    return 0

                response = _as_object(_payload_text(frame.payload))
                if response.get("code") == 0:
                    print("唤醒词设置成功，请等待设备重启后测试")
                    return 0

                print(f"设备返回: {_payload_text(frame.payload)}", file=sys.stderr)
                return 1

            if not request_sent and time.monotonic() - started >= 0.5:
                serial_port.write(request)
                request_sent = True
                print(f"已发送唤醒词设置: {keyword}，阈值: {threshold}")

    print("未收到设备确认", file=sys.stderr)
    return 2


def check_serial(port: str, baudrate: int, timeout: float) -> int:
    """Send a version request and report valid frames received from the device."""
    parser = FrameParser()
    started = time.monotonic()
    request_id = int(time.time() * 1000) & 0xFFFF
    request = encode_frame(CONTROL_MESSAGE, request_id, b'{"type":"version"}')
    received_handshake = False
    received_ack = False
    request_sent = False

    with LinuxSerialPort(port, baudrate) as serial_port:
        while time.monotonic() - started < timeout:
            for frame in parser.feed(serial_port.read()):
                if frame.msg_type == HANDSHAKE_MESSAGE:
                    first_handshake = not received_handshake
                    received_handshake = True
                    serial_port.write(
                        encode_frame(HANDSHAKE_ACK, frame.message_id, HANDSHAKE_PAYLOAD)
                    )
                    if first_handshake:
                        print(f"串口正常: 收到握手帧 id={frame.message_id}，已回复")
                    if not request_sent:
                        serial_port.write(request)
                        request_sent = True
                        print(f"已发送版本查询: {port}")
                    continue

                if frame.msg_type == HANDSHAKE_ACK and frame.message_id == request_id:
                    received_ack = True
                    print(f"串口正常: 设备已确认版本查询 id={frame.message_id}")
                    continue

                print(
                    "串口正常: "
                    f"收到设备帧 type=0x{frame.msg_type:02X} "
                    f"id={frame.message_id} payload={_payload_text(frame.payload)}"
                )
                return 0

            if not request_sent and time.monotonic() - started >= 0.5:
                serial_port.write(request)
                request_sent = True
                print(f"已发送版本查询: {port}")

        if received_handshake or received_ack:
            print(
                "串口已连通，但未收到版本信息，语音业务尚未就绪",
                file=sys.stderr,
            )
            return 3
        print("未收到 M260C 数据", file=sys.stderr)
        return 2


def monitor(
    port: str,
    baudrate: int,
    once: bool,
    timeout: float,
    json_output: bool,
    verbose: bool,
) -> int:
    parser = FrameParser()
    started = time.monotonic()

    with LinuxSerialPort(port, baudrate) as serial_port:
        print(f"监听 M260C 唤醒事件: {port}", file=sys.stderr)
        while True:
            if timeout > 0 and time.monotonic() - started >= timeout:
                return 2

            for frame in parser.feed(serial_port.read()):
                if verbose:
                    print(
                        f"收到帧 type=0x{frame.msg_type:02X} "
                        f"id={frame.message_id} length={len(frame.payload)}",
                        file=sys.stderr,
                    )
                if frame.msg_type == HANDSHAKE_MESSAGE:
                    serial_port.write(
                        encode_frame(HANDSHAKE_ACK, frame.message_id, HANDSHAKE_PAYLOAD)
                    )
                    if verbose:
                        print("已回复握手", file=sys.stderr)
                    continue

                event = parse_wake_event(frame)
                if event is None:
                    continue

                print(format_event(event, json_output), flush=True)
                if once:
                    return 0


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="M260C 独立语音唤醒监听程序")
    parser.add_argument(
        "-p", "--port", default="/dev/wheeltec_mic", help="M260C 控制串口"
    )
    parser.add_argument("-b", "--baudrate", type=int, default=115200, help="串口波特率")
    parser.add_argument("--once", action="store_true", help="收到一次唤醒事件后退出")
    parser.add_argument(
        "--timeout", type=float, default=0.0, help="等待秒数，0 表示持续监听"
    )
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出事件")
    parser.add_argument("--verbose", action="store_true", help="显示收到的协议帧")
    parser.add_argument(
        "--check-serial", action="store_true", help="查询设备版本并检查串口收发"
    )
    parser.add_argument(
        "--set-wake-word", metavar="WORD", help="设置唤醒词；旧版 M2 使用带声调数字的拼音"
    )
    parser.add_argument("--threshold", type=int, default=900, help="唤醒阈值")
    return parser


def main() -> int:
    args = build_argument_parser().parse_args()
    try:
        if args.set_wake_word is not None:
            timeout = args.timeout if args.timeout > 0 else 10.0
            return set_wake_word(
                args.port,
                args.baudrate,
                args.set_wake_word,
                args.threshold,
                timeout,
                args.verbose,
            )
        if args.check_serial:
            timeout = args.timeout if args.timeout > 0 else 5.0
            return check_serial(args.port, args.baudrate, timeout)
        return monitor(
            args.port,
            args.baudrate,
            args.once,
            args.timeout,
            args.json,
            args.verbose,
        )
    except KeyboardInterrupt:
        return 130
    except (OSError, ValueError, RuntimeError, TimeoutError) as error:
        print(f"错误: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
