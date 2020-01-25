import numpy as np
import cv2


img = cv2.imread('chaine.png', cv2.IMREAD_COLOR)




# print(img[55, 55])
# img[55, 55] = [255, 255, 255]
# print(img[55, 55])


# print(img[10:20, 30:40])
# img[10:20, 30:40] = [255, 255, 255]
# roi = img[44:66, 52:58]
# print(roi)


mouth_face = img[44:66, 52:58]
img[0:22, 0:6] = mouth_face




cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()