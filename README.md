Real-time 3-Wheeler ADAS system using YOLO11-seg and MiDaS depth estimation for collision warning on unstructured Indian roads with edge-deployable pipeline.
Repository Structure:

main.py → prototype inference pipeline
requirements.txt → dependencies
models/ → placeholder for YOLO11-seg and MiDaS weights
ppt.pdf → proposal presentation

Future Work:

Integration of real-time YOLO11-seg inference
MiDaS depth estimation deployment
ROI-based collision detection logic
Edge deployment using OpenVINO / ONNX runtime

Current Implementation Status

This repository currently includes a working YOLO-based real-time object detection pipeline as a prototype perception module.

Upcoming integration modules:

• Drivable area segmentation (YOLO11-seg)
• Monocular depth estimation using MiDaS
• ROI-based collision warning logic
• Edge deployment optimization using OpenVINO / ONNX
## Sample Output

Example object detection output from prototype ADAS perception pipeline:

outputs/sample_detection.png
