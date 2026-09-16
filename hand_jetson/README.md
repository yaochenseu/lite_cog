# HaGRID dynamic gestures for NVIDIA Jetson

This directory is the deployment subset of `hand2/dynamic_gestures`. It contains
the camera demo, two pretrained ONNX models, hand tracking, and the deterministic
action controller. Training files and example GIFs are intentionally excluded.

## Files

- `run_demo.py`: USB camera, video file, or CSI/GStreamer entry point.
- `models/hand_detector.onnx`: hand detector.
- `models/crops_classifier.onnx`: 45-class hand-pose classifier.
- `main_controller.py`: detection, classification, and OCSORT tracking pipeline.
- `utils/action_controller.py`: rules that convert pose/trajectory history into dynamic gestures.
- `ocsort/`: object tracking implementation.

## Jetson environment

Use the Python and OpenCV supplied with the installed JetPack whenever possible.
The pip OpenCV wheel normally loses Jetson's GStreamer/CUDA integration.

```bash
cd /path/to/hand_jetson
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

Install an `onnxruntime` or `onnxruntime-gpu` aarch64 build that matches the
specific JetPack, CUDA, and Python versions. It is intentionally not pinned in
`requirements.txt` because JetPack 5 and JetPack 6 require different builds.

Verify the runtime before opening the camera:

```bash
python3 -c "import cv2, numpy, scipy, onnxruntime as ort; print(cv2.__version__); print(ort.get_available_providers())"
```

The program selects providers in this order when available:

1. `TensorrtExecutionProvider`
2. `CUDAExecutionProvider`
3. `CPUExecutionProvider`

## USB camera

```bash
python3 run_demo.py --source 0 --debug
```

Use another `/dev/videoN` index with `--source N`. Press `q` to exit.

## CSI camera

Pass a GStreamer pipeline as the source:

```bash
python3 run_demo.py --debug --gstreamer --source \
'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM),width=1280,height=720,framerate=30/1,format=NV12 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink drop=1'
```

The CSI command requires an OpenCV build with GStreamer support and an active
desktop display because the demo uses `cv2.imshow`.

## Input options

```text
--source       Camera index, video path, or GStreamer pipeline
--gstreamer    Interpret source as a GStreamer pipeline
--width        Requested USB-camera width (default 1280)
--height       Requested USB-camera height (default 720)
--no-mirror    Disable horizontal mirroring
--debug        Show boxes, hand-pose labels, tracking IDs, and FPS
```

Dynamic actions are also printed to the terminal. The bundled implementation
supports swipe, fast swipe, tap/double tap, drag/drop, and zoom rule groups.

## License and provenance

The runtime was derived from `ai-forever/dynamic_gestures`. Keep
`license/LICENSE-2.0.txt` with redistributed copies. The original dependency
pins are retained in `requirements-upstream.txt` for reference.
