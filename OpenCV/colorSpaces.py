import cv2 as cv
import matplotlib.pyplot as pp

img = cv.imread('OpenCV\Photos\Picture2.jpg')
# cv.imshow('img', img)

# enlarged size
enlarged = cv.resize(img, (img.shape[1]*2, img.shape[0]*2), cv.INTER_CUBIC)
cv.imshow('enlarged', enlarged)

# BGR 2 GRAY
gray = cv.cvtColor(enlarged, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR 2 HSV
hsv = cv.cvtColor(enlarged, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR 2 LAB
lab = cv.cvtColor(enlarged, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR 2 RGB
rgb = cv.cvtColor(enlarged, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# matplot lib
pp.imshow(rgb)
pp.show()

# INVERSE CONVERSION

rvs = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('gray to rgb', rvs)

# gray to rgb conversion is not working?

cv.waitKey(0)