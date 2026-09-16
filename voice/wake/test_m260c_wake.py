#!/usr/bin/env python3

import json
import os
import pty
import select
import unittest

from wake.m260c_wake import (
    DEVICE_MESSAGE,
    HANDSHAKE_ACK,
    HANDSHAKE_PAYLOAD,
    Frame,
    FrameParser,
    LinuxSerialPort,
    encode_frame,
    make_wake_word_payload,
    parse_wake_event,
)


class FrameParserTest(unittest.TestCase):
    def test_fragmented_frame(self) -> None:
        raw = encode_frame(DEVICE_MESSAGE, 42, b'{}')
        parser = FrameParser()

        self.assertEqual(parser.feed(raw[:3]), [])
        self.assertEqual(parser.feed(raw[3:8]), [])
        frames = parser.feed(raw[8:])

        self.assertEqual(frames, [Frame(DEVICE_MESSAGE, 42, b'{}')])

    def test_noise_and_multiple_frames(self) -> None:
        first = encode_frame(DEVICE_MESSAGE, 1, b'one')
        second = encode_frame(DEVICE_MESSAGE, 2, b'two')
        frames = FrameParser().feed(b'noise' + first + second)

        self.assertEqual([frame.message_id for frame in frames], [1, 2])

    def test_bad_checksum_is_rejected_and_next_frame_is_read(self) -> None:
        broken = bytearray(encode_frame(DEVICE_MESSAGE, 1, b'bad'))
        broken[-1] ^= 0xFF
        valid = encode_frame(DEVICE_MESSAGE, 2, b'good')

        frames = FrameParser().feed(bytes(broken) + valid)

        self.assertEqual(frames, [Frame(DEVICE_MESSAGE, 2, b'good')])

    def test_handshake_ack_keeps_message_id(self) -> None:
        raw = encode_frame(HANDSHAKE_ACK, 513, HANDSHAKE_PAYLOAD)
        frame = FrameParser().feed(raw)[0]

        self.assertEqual(frame.msg_type, HANDSHAKE_ACK)
        self.assertEqual(frame.message_id, 513)
        self.assertEqual(frame.payload, HANDSHAKE_PAYLOAD)


class WakeEventTest(unittest.TestCase):
    def make_frame(self, message: dict, message_id: int = 7) -> Frame:
        payload = json.dumps(message, ensure_ascii=False).encode('utf-8')
        return Frame(DEVICE_MESSAGE, message_id, payload)

    def test_flat_wake_event(self) -> None:
        frame = self.make_frame(
            {
                'type': 'aiui_event',
                'content': {'beam': 0, 'angle': 45, 'confidence': 950},
            }
        )

        event = parse_wake_event(frame, timestamp=10.0)

        self.assertIsNotNone(event)
        self.assertEqual(event.angle_deg, 45)
        self.assertEqual(event.beam, 0)
        self.assertEqual(event.confidence, 950)

    def test_nested_wake_event(self) -> None:
        info = json.dumps(
            {'ivw': {'angle': 123, 'keyword': 'xiao3 wei1', 'score': 900}}
        )
        frame = self.make_frame(
            {
                'type': 'aiui_event',
                'content': {'eventType': '4', 'arg1': 2, 'info': info},
            }
        )

        event = parse_wake_event(frame, timestamp=10.0)

        self.assertIsNotNone(event)
        self.assertEqual(event.keyword, 'xiao3 wei1')
        self.assertEqual(event.angle_deg, 123)
        self.assertEqual(event.beam, 2)
        self.assertEqual(event.confidence, 900)

    def test_other_aiui_event_is_ignored(self) -> None:
        frame = self.make_frame(
            {'type': 'aiui_event', 'content': {'eventType': 1, 'angle': 20}}
        )

        self.assertIsNone(parse_wake_event(frame))

    def test_non_json_payload_is_ignored(self) -> None:
        frame = Frame(DEVICE_MESSAGE, 1, b'not json')

        self.assertIsNone(parse_wake_event(frame))


class LinuxSerialPortTest(unittest.TestCase):
    def test_serial_round_trip(self) -> None:
        master_fd, slave_fd = pty.openpty()
        slave_path = os.ttyname(slave_fd)
        incoming = encode_frame(DEVICE_MESSAGE, 9, b'{}')
        outgoing = encode_frame(HANDSHAKE_ACK, 10, HANDSHAKE_PAYLOAD)

        try:
            with LinuxSerialPort(slave_path, 115200) as serial_port:
                os.write(master_fd, incoming)
                self.assertEqual(serial_port.read(timeout=0.2), incoming)

                serial_port.write(outgoing)
                readable, _, _ = select.select([master_fd], [], [], 0.2)
                self.assertTrue(readable)
                self.assertEqual(os.read(master_fd, 4096), outgoing)
        finally:
            os.close(slave_fd)
            os.close(master_fd)


class WakeWordCommandTest(unittest.TestCase):
    def test_make_wake_word_payload(self) -> None:
        payload = make_wake_word_payload('ni3 hao3', 900)

        self.assertEqual(
            json.loads(payload),
            {
                'type': 'wakeup_keywords',
                'content': {'keyword': 'ni3 hao3', 'threshold': '900'},
            },
        )

    def test_invalid_threshold_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            make_wake_word_payload('ni3 hao3', 499)


if __name__ == '__main__':
    unittest.main()
