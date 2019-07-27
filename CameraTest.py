import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    print(cap.get(cv2.CAP_PROP_FPS))

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capture', grey)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()