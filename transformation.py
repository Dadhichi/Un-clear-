import cv2 as cv
import numpy as np
import random

image = cv.imread('testimg2.png')

rows, columns, channel = image.shape

for i in range(4):
    tx, ty = random.randint(-25, 25), random.randint(-25, 25)
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    dst = cv.warpAffine(image, M, (columns, rows))

    cv.imshow('Translation '+str(i), dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

for i in range(4):
    theta = random.randint(-90, 90)
    M = cv.getRotationMatrix2D(((columns-1) / 2.0, (rows-1) / 2.0), theta, 1)
    dst = cv.warpAffine(image, M, (columns, rows))
    cv.imshow('Rotation '+str(i), dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

dst = cv.GaussianBlur(image, (5, 5), 0)
cv.imshow('Blur 1', dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.blur(image, (5, 5))
cv.imshow('Blur 2', dst)
cv.waitKey(0)
cv.destroyAllWindows()
