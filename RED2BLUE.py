import cv2 as cv
import numpy as np
image = cv.imread('TestPic.jpg')
dst = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow('rgb', dst)

# dst = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# lowe_red = np.array([0, 100, 100])
# highe_red = np.array([179, 255, 255])

# mask = cv.inRange(dst, lowe_red, highe_red)

# dst[mask != 0] = [0, 100, 100]

# cv.imshow('mask', dst)

# cv.imshow('original', dst)
# cv.imshow('somethins', dst)

cv.waitKey(0)
cv.destroyAllWindows()
