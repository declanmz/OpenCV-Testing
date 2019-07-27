import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)

img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 255), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 0), (255, 0, 255), 5)

img = cv2.rectangle(img, (100, 100), (300, 500), (255, 0, 255), 3)

img = cv2.circle(img, (300, 300), 40, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 1, (255, 255, 0), 2)

cv2.imshow('Window', img)

cv2.waitKey(0)
cv2.destroyAllWindows()