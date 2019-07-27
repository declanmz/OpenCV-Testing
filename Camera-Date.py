import cv2
import datetime

cap = cv2.VideoCapture(0)

capWidth = cap.get(3)
capHeight = cap.get(4)

# cap.set(3, capWidth*1)
# cap.set(4, capHeight*1)

print(cap.get(3))
print(cap.get(4))

font = cv2.FONT_HERSHEY_SIMPLEX

ret = True
while cap.isOpened() and ret:
    ret, frame = cap.read()

    dtText = str(datetime.datetime.now())

    cv2.putText(frame, dtText, (10, 30), font, 1, (0, 0, 0), 2)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == 27:
        break
