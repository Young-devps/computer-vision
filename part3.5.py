import numpy as np
import cv2

im1 = cv2.imread('Figure_1.png')
im2 = cv2.imread('Figure_one.png')
im3 = cv2.imread('python.png')



ligne, col, couche = im3.shape
roi = im1[0:ligne, 0:col]


im32gray = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)


#appliquer un depanner
ret, mask = cv2.threshold(im32gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

im1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
im3_fg = cv2.bitwise_and(im3, im3, mask=mask)

dst = cv2.add(im1_bg, im3_fg)
im1[0:ligne, 0:col] = dst



cv2.imshow('res', im1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('im1_bg', im1_bg)
cv2.imshow('im3_fg', im3_fg)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
