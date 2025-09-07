import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\Photos\Picture5.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (blank.shape[1]//2 , blank.shape[0]//2), 50, 255, -1)
rectangle = cv.rectangle(blank.copy(), (0,0), (blank.shape[1]//2, blank.shape[0]//2), 255, -1)

mask = cv.bitwise_and(circle, rectangle)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked', masked)

cv.waitKey(0)