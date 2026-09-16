import argparse
import time
from pathlib import Path

import cv2
import numpy as np

from main_controller import MainController
from utils import Drawer, Event, targets


PERSISTENT_ACTIONS = {Event.DRAG, Event.DRAG2, Event.DRAG3}
BASE_DIR = Path(__file__).resolve().parent


def parse_source(source):
    """Convert a numeric camera source to int and keep paths/pipelines as strings."""
    try:
        return int(source)
    except ValueError:
        return source


def open_capture(args):
    source = parse_source(args.source)
    backend = cv2.CAP_GSTREAMER if args.gstreamer else cv2.CAP_ANY
    cap = cv2.VideoCapture(source, backend)
    if isinstance(source, int):
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        raise RuntimeError(
            f"Cannot open camera/video source {args.source!r}. "
            "For a Jetson CSI pipeline, also pass --gstreamer."
        )
    return cap


def show_static_debug(frame, bboxes, ids, labels):
    if bboxes is None:
        return
    bboxes = bboxes.astype(np.int32)
    for box, track_id, label in zip(bboxes, ids, labels):
        gesture = targets[label] if label is not None else "None"
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 255, 0), 4)
        cv2.putText(
            frame,
            f"ID {int(track_id)}: {gesture}",
            (box[0], max(30, box[1] - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )


def consume_action(track, drawer):
    action = track["hands"].action
    if action is None:
        return
    if drawer.action != action:
        print(f"Dynamic gesture: {action.name}")
    drawer.set_action(action)
    if action not in PERSISTENT_ACTIONS:
        track["hands"].action = None


def process_tracks(frame, controller, drawer):
    thumb_boxes = []
    for track in controller.tracks:
        if track["tracker"].time_since_update >= 1 or not track["hands"]:
            continue

        hand = track["hands"][-1]
        if hand.gesture == 3 and hand.bbox is not None:
            thumb_boxes.append(hand.bbox)

        # Preserve the upstream privacy demo: blur a stable middle-finger crop.
        if len(track["hands"]) > 3 and [item.gesture for item in track["hands"][-3:]] == [23, 23, 23]:
            x1, y1, x2, y2 = map(int, hand.bbox)
            height, width = frame.shape[:2]
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(width, x2), min(height, y2)
            if x2 > x1 and y2 > y1:
                crop = frame[y1:y2, x1:x2]
                frame[y1:y2, x1:x2] = cv2.GaussianBlur(crop, (51, 51), 10)

        consume_action(track, drawer)

    if len(thumb_boxes) == 2:
        drawer.draw_two_hands(frame, thumb_boxes)


def run(args):
    cap = open_capture(args)
    controller = MainController(args.detector, args.classifier)
    drawer = Drawer()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Camera/video stream ended or a frame could not be read.")
                break
            if not args.no_mirror:
                frame = cv2.flip(frame, 1)

            start_time = time.perf_counter()
            bboxes, ids, labels = controller(frame)

            if args.debug:
                show_static_debug(frame, bboxes, ids, labels)
                elapsed = max(time.perf_counter() - start_time, 1e-9)
                cv2.putText(
                    frame,
                    f"FPS {1.0 / elapsed:.2f}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )

            process_tracks(frame, controller, drawer)
            frame = drawer.draw(frame)
            cv2.imshow("HaGRID Dynamic Gestures", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def build_parser():
    parser = argparse.ArgumentParser(description="Run HaGRID dynamic gestures on Jetson")
    parser.add_argument(
        "--detector", default=str(BASE_DIR / "models" / "hand_detector.onnx"), help="Detector ONNX model"
    )
    parser.add_argument(
        "--classifier", default=str(BASE_DIR / "models" / "crops_classifier.onnx"), help="Classifier ONNX model"
    )
    parser.add_argument("--source", default="0", help="Camera index, video path, or GStreamer pipeline")
    parser.add_argument("--gstreamer", action="store_true", help="Open --source with the GStreamer backend")
    parser.add_argument("--width", type=int, default=1280, help="Requested USB camera width")
    parser.add_argument("--height", type=int, default=720, help="Requested USB camera height")
    parser.add_argument("--no-mirror", action="store_true", help="Do not mirror the input image")
    parser.add_argument("--debug", action="store_true", help="Draw hand boxes, static labels, IDs, and FPS")
    return parser


if __name__ == "__main__":
    run(build_parser().parse_args())
