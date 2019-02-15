import cv2
from imutils.video import VideoStream
import imutils


capture = VideoStream(src=0)
# capture = VideoStream(src='vid.mp4')

capture.start()

while True:
    img = capture.read()
    cv2.imshow('VideosStream', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()