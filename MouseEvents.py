import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):

    font = cv2.FONT_HERSHEY_SIMPLEX

    if event == cv2.EVENT_LBUTTONDOWN:
        str_xy = str(x) + ', ' + str(y)
        cv2.putText(img, str_xy, (x, y), font, .5, (255, 255, 0))
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        str_bgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, str_bgr, (x, y), font, .5, (0, 255, 0))
        cv2.imshow('image', img)


# img = np.zeros([512, 512, 3], np.uint8)

img = cv2.imread('lena.jpg', 1)

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()