#!/bin/python

import cv2

cam = cv2.VideoCapture("http://10.0.1.2/mjpg/video.mjpg")
print cam

while(True):
  ret, frame = cam.read()
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('feed', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cam.release()
cv2.destroyAllWindows()