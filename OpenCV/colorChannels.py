import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\Photos\Picture7.jpg')

# enlarged size
enlarged = cv.resize(img, (img.shape[1]*2, img.shape[0]*2), cv.INTER_CUBIC)
cv.imshow('enlarged', enlarged)

# blank image
blank = np.zeros(enlarged.shape[:2], dtype = 'uint8')

# split img by color
b, g, r = cv.split(enlarged)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge b, g and r
merged = cv.merge([b, g, r])
cv.imshow('merged image', merged)

# color saturation of splited color
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)