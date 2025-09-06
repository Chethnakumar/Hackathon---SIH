import cv2 as cv
# print(cv.__version__)
img = cv.imread('Photos/Picture8.jpg')

cv.imshow('Fairy Tail', img)

cv.waitKey(0)
# this is a test.
# vid = cv.VideoCapture('Videos\[Fairy Tail] NaLu Moment Lucy Hugs Natsu Clip [English Subbed].mp4')

# while True:
#     isTrue, frame = vid.read() # to read

#     cv.imshow('Natsu x Lucy', frame) # to display

#     if cv.waitKey(50) & 0XFF==ord('d'):
#         break

# vid.release()

# cv.destroyAllWindows()