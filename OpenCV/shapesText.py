import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# Assigning different color
blank[0:250, 250:500] = 255,255,255
cv.imshow('green', blank)

#rectangle
cv.rectangle(blank, (0,0), (250, 500), (255,255,255), 2)
cv.imshow('white', blank)

# circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), 4)
cv.imshow('circle', blank)

# line 
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), 2)
cv.imshow('line', blank)

# text 
cv.putText(blank, 'Hello! This is Chethna', (blank.shape[1]//4, blank.shape[0]//4), cv.FONT_ITALIC, 1, (0,0,255), 4)
cv.imshow('text', blank)

cv.waitKey(0)