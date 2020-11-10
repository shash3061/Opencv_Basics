import cv2
import numpy as np

img = cv2.imread('resources/shash.png')
print(img.shape)

### Resize by ------------ width, height
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

# first- height and then the width
imgCropped = img[0:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('Image Resize', imgResize)
cv2.imshow('Cropped image', imgCropped)
cv2.waitKey(0)