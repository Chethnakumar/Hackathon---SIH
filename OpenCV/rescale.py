import cv2 as cv

def rescaleFrame (frame, scale = 0.75):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    dim = (w, h)

    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)

# image 

img = cv.imread('Photos/Picture8.jpg')
resized = rescaleFrame(img, scale=.3)

cv.imshow('Fairy Tail', img)
cv.imshow('resized', resized)

cv.waitKey(0)

# video

# vid = cv.VideoCapture('Videos\[Fairy Tail] NaLu Moment Lucy Hugs Natsu Clip [English Subbed].mp4')

# while True:
#     isTrue, frame = vid.read() # to read
#     resized_vid = rescaleFrame(frame, scale=.1) #resized video input

#     cv.imshow('Natsu x Lucy', frame) # to display
#     cv.imshow('ressized video', resized_vid) # to display resized vid

#     if cv.waitKey(50) & 0XFF==ord('d'):
#         break

# vid.release()

cv.destroyAllWindows()