import cv2

cap = cv2.VideoCapture(0)

capFrameRate = cap.get(cv2.CAP_PROP_FPS)
capWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
capHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, capFrameRate, (capWidth, capHeight))

ret = True

while cap.isOpened() and ret:
    ret, frame = cap.read()

    # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capture', frame)

    out.write(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()