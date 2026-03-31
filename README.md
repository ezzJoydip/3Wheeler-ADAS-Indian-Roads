# 3Wheeler-ADAS-Indian-Roads

## Project Overview
This project proposes a real-time Advanced Driver Assistance System (ADAS) designed specifically for 3-wheelers operating in unstructured Indian road environments. The system detects surrounding objects, estimates relative depth using monocular vision, and generates collision warning alerts (Safe / Warning / Stop) for driver assistance using edge-deployable hardware.

## Model Architecture
Pipeline:

Camera Input
→ CLAHE preprocessing
→ YOLO object detection / segmentation
→ MiDaS monocular depth estimation
→ ROI-based collision warning logic
→ HUD alert output

The detection module currently uses YOLOv8 lightweight model for real-time inference.

Future modules include:
- YOLO11-seg drivable area segmentation
- MiDaS depth estimation integration
- OpenVINO edge deployment optimization

## Dataset Used
The system leverages:

- India Driving Dataset (IDD)
- nuScenes dataset
- COCO pretrained weights for transfer learning

These datasets help adapt perception models to Indian road scenarios including pedestrians, animals, and mixed traffic conditions.

## Setup & Installation Instructions

Install dependencies:

pip install -r requirements.txt

## How to Run the Code

Run:

python main.py

This launches the real-time detection pipeline using webcam input.

Press **q** to exit.

## Example Outputs / Results

Example detection outputs are available in:

outputs/sample_output.txt

Future outputs include:
- bounding box detection overlays
- segmentation masks
- collision warning visualization frames
