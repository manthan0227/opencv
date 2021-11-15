import numpy as np
import cv2

# //open webcam or camera
cap = cv2.VideoCapture('sample.mov')

while True:
    ret, frame = cap.read()
    # //width and height of the window
    width = int(cap.get(3))
    height = int(cap.get(4))
    # //for Blank window
    image = np.zeros(frame.shape, np.uint8)
    # //
    # //four image frame display on window
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)
    # //when you click 'q' on the keyboard frame window will be shutdown
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
