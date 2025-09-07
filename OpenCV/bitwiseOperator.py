import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('rectagle', rectangle)

circle = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 200, 255, -1)
cv.imshow('circle', circle)

# bitwise AND
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise and', bit_and)

# bitwise OR
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise or', bit_or)

# bitwise XOR
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise xor', bit_xor)

# bitwise not
bit_not = cv.bitwise_not(rectangle, circle)
cv.imshow('bitwise not', bit_not)

cv.waitKey(0)