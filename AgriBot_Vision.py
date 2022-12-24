import numpy as np
import cv2 as cv
import argparse

Lower_Limit = np.array([110, 50, 50])
Upper_Limit = np.array([130, 255, 255])

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'

parser = argparse.ArgumentParser()
parser.add_argument('--camera', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)

cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)

while True:

    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    frame_threshold = cv.inRange(frame_HSV, Lower_Limit, Upper_Limit)

    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

# Enter you code here (tf)

cv.destroyAllWindows()
