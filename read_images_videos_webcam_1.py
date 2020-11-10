import cv2
import numpy as np
print('Package imported')

img1 = cv2.imread('resources/shash.png')
cv2.imshow('Output', img1)
cv2.waitKey(0)

# Video
# cap = cv2.VideoCapture('resources/sample_video.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
