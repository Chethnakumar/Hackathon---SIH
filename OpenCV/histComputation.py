import cv2 as cv
import numpy as np
import matplotlib.pyplot as pp

img = cv.imread('OpenCV\Photos\Picture3.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# histogram for grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('masked', masked)

hist = cv.calcHist([gray], [0], masked, [256], [0,256])

pp.figure()
pp.title('Grayscale histogram')
pp.xlabel('bins')
pp.ylabel('no of pixels')

pp.plot(hist)
pp.xlim([0,256])
pp.show()

# histogram for color
# colors = ['b', 'g', 'r']
# for i, col in enumerate(colors):
#     hist = cv.calcHist([img], [i], mask, [256], [0,256])
#     pp.plot(hist, color = col)
#     pp.xlim([0,256])
# pp.show()

cv.waitKey(0)