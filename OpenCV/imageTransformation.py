import cv2 as cv
import numpy as np

img = cv.imread('OpenCV\Photos\Picture1.jpg')
cv.imshow('image', img)

def translate(img, x, y) :
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dim)

def rotate(img, angle, rotPoint=None) :
    (h, w) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (w//2, h//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dim = (w,h)
    return cv.warpAffine(img, rotMat, dim)

#flipping
flip = cv.flip(img, 0)
cv.imshow('flipped img', flip)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

rotated = rotate(img, 180, (100,100))
cv.imshow('rotated', rotated)

cv.waitKey(0)