import cv2 as cv
import numpy as np
image = cv.imread('TestPic.jpg')


def pencil(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    inverted_gray = 255 - gray

    blur = cv.GaussianBlur(inverted_gray, (5, 5), 0)

    dodge = cv.divide(gray, 255 - blur, scale=256)

    final = 255 - cv.divide(255 - dodge, 255 - blur, scale=256)
    return final


final = pencil(image)
cv.imshow('F', final)
cv.waitKey(0)
cv.destroyAllWindows()

cap = cv.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video  file")

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        dest = pencil(frame)
        cv.imshow('Pencil', dest)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv.destroyAllWindows()
