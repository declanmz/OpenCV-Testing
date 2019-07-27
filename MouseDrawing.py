import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):

    font = cv2.FONT_HERSHEY_SIMPLEX

    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 255, 255), 5)

        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:

        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        color_image = np.zeros((200, 200, 3), np.uint8)

        color_image[:] = [blue, green, red]

        cv2.imshow('Color', color_image)


points =[]

# img = np.zeros([512, 512, 3], np.uint8)

img = cv2.imread('lena.jpg', 1)

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()