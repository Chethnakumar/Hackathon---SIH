import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\Photos\Picture1.jpg')
# cv.imshow('img', img)

# enlarged image
enlarged_img = cv.resize(img, (img.shape[1]*3, img.shape[0]*3), interpolation=cv.INTER_CUBIC)
cv.imshow('enlarged', enlarged_img)

# blank image
blank = np.zeros(enlarged_img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# grayscale imagae
gray = cv.cvtColor(enlarged_img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray)

# Gaussian Blur
blur = cv.GaussianBlur(enlarged_img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blurred', blur)

# canny image
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny img', canny)

canny1 = cv.Canny(gray, 125, 175)
cv.imshow('canny1 img', canny1)

# threshold image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# count contours
contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contour\'s found!')

# draw contour
cv.drawContours(blank, contour, -1, (255,255,255), 1)
cv.imshow('contour drawing', blank)

cv.waitKey(0)