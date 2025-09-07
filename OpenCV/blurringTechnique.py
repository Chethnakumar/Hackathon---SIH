import cv2 as cv

img = img = cv.imread('OpenCV\Photos\Picture6.jpg')
cv.imshow('img', img)

# averaging smoothing
avg = cv.blur(img, (3,3))
cv.imshow('average smoothing', avg)

# Gaussian Blur
blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', blur)

# Median blur
med = cv.medianBlur(img, 3)
cv.imshow('Median blur', med)

# bilateral Blur
bilat = cv.bilateralFilter(img, 10, 30, 30)
cv.imshow('bilateral blur', bilat)

cv.waitKey(0)