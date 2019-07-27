import cv2

img = cv2.imread('lena.jpg', 1)

cv2.imshow('image', img)

loopCondition = True

while loopCondition:
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
        loopCondition = False
    elif k == ord('s'):
        cv2.imwrite('lena_copy.png', img)
        cv2.destroyAllWindows()
        loopCondition = False
