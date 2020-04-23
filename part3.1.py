import cv2
import numpy as np
import matplotlib.pyplot as plt
                                
im = cv2.imread('jump.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

plt.imshow(im, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [500, 100], 'c', linewidth=5)
plt.show()


#cv2.imshow('image1', im)
cv2.waitKey(0)
cv2.destroyAllWindows()