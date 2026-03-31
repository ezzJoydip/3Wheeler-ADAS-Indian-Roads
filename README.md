# 3Wheeler-ADAS-Indian-Roads
Real-time 3-Wheeler ADAS system for unstructured Indian road conditions using YOLO11-seg, drivable area segmentation, and monocular depth estimation for collision warning on edge devices.
Pipeline:
Camera → CLAHE preprocessing → YOLO11-seg detection →
MiDaS depth estimation → ROI collision logic → HUD alert output
