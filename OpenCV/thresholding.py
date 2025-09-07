import cv2 as cv

img = cv.imread('OpenCV\Photos\Picture2.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray.copy(), 175, 255, cv.THRESH_BINARY)
cv.imshow('thresholded image', thresh)

# inverse thresholding
threshold1, thresh1 = cv.threshold(gray.copy(), 175, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded image1', thresh1)

# adaptive threshold
adp_thresh = cv.adaptiveThreshold(gray.copy(), 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold', adp_thresh)

cv.waitKey(0)