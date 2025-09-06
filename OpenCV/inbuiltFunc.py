import cv2 as cv

img = cv.imread('OpenCV\Photos\Picture1.jpg')
cv.imshow('img', img)

# resizing
large_img = cv.resize(img, (564, 804), interpolation = cv.INTER_CUBIC)
cv.imshow('enlarged', large_img)

# grayscale
gray = cv.cvtColor(large_img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

# blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
edge = cv.Canny(large_img, 130, 170)
cv.imshow('edge', edge)

# image dilation
dilate = cv.dilate(edge, (3,3), iterations=3)
cv.imshow('dilated', dilate)

# image eroded
eroded = cv.erode(dilate, (3,3), iterations=3)
cv.imshow('eroded', eroded)

# cropping
crop = large_img[0:100, 100:300]
cv.imshow('cropped', crop)

cv.waitKey(0)