import cv2 as cv

image = cv.imread('TestPic.jpg')

dst = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('GrayScale', dst)

cv.waitKey(0)
cv.destroyAllWindows()
