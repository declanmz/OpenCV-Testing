import numpy as np
import cv2

img = cv2.imread('board.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)

chip = img[300:440, 330:510]
img[300:440, 30:210] = chip

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst = cv2.addWeighted(img, .5, img2, .5, 0)

cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()