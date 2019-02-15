import cv2
from imutils.video import VideoStream
import imutils

img = cv2.imread('rrr.jpg')
cv2.imshow('window_name', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 