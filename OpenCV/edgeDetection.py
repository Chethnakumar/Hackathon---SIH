import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\Photos\Picture1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# lapacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lapacian', lap)

# sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('sobel', combined)

# canny
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

cv.waitKey(0)