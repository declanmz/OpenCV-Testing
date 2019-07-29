import numpy as np
import cv2

img1 = np.zeros([250, 500, 3], np.uint8)
cv2.rectangle(img1, (250, 0), (500, 250), (255, 255, 255), -1)
img2 = np.zeros([250, 500, 3], np.uint8)
cv2.rectangle(img2, (200, 0), (300, 100), (255, 255, 255), -1)

bitOp = cv2.bitwise_xor(img2, img1)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('bitOp', bitOp)

cv2.waitKey(0)
cv2.destroyAllWindows()