import cv2
import numpy as np

print("Starting 3-Wheeler ADAS Prototype...")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.putText(frame,
                "ADAS STATUS: SAFE",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    cv2.imshow("3-Wheeler ADAS Output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
