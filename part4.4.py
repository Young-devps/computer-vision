#detection de contour

import cv2
import numpy as np



img = cv2.imread('python.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corner = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)
k = cv2.waitKey(0) & 0xFF