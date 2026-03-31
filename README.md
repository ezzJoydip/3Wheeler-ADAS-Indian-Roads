# 3Wheeler-ADAS-Indian-Roads

A lightweight real-time Advanced Driver Assistance System (ADAS) designed for auto-rickshaws operating in unstructured Indian road conditions.

The system integrates YOLO11-seg for object detection and drivable area segmentation with MiDaS monocular depth estimation to generate collision warning alerts (Safe / Warning / Stop) on edge devices with low latency.

Pipeline:
Camera Input → CLAHE preprocessing → YOLO11-seg detection → MiDaS depth estimation → ROI-based collision logic → HUD alert output
