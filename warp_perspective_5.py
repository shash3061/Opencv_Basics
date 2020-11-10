import cv2
import numpy as np

img = cv2.imread('resources/cards2.jpg')
#img = cv2.resize(img, (600, 712))

width, height = 250, 350
pts1 = np.float32([[406, 23], [472, 167], [198, 109], [267, 261]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)