## https://www.youtube.com/watch?v=UOIKXp82iEw

## lib for web-cam
## pip install opencv-python

## C:/Users/rgupta/AppData/Local/Programs/Python/Python310/python.exe d:/python-workspace/securitycamra.py

import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Papa', frame)

