from ultralytics import YOLO
import cv2

# Load YOLO pretrained segmentation model
model = YOLO("yolov8n.pt")  # lightweight detection model

# Start webcam
cap = cv2.VideoCapture(0)

print("Starting 3-Wheeler ADAS Detection Pipeline...")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run object detection
    results = model(frame)

    # Plot detections on frame
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("ADAS Object Detection Output", annotated_frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
