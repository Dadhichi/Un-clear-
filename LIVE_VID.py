import cv2 as cv

cap = cv.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video  file")

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        cv.imshow('Frame', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv.destroyAllWindows()
