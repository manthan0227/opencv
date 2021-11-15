import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # // line(src, start, end, color, thickness)
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 10)
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 10)
    # // rectangle(src, topleft, bottomright, color, thickness)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # // circle(src, center, radius, color, thickness)
    img = cv2.circle(img, (300, 300), 50, (0, 255, 0), 5)
    font = cv2.FONT_HERSHEY_PLAIN
    # // putText(src, text, start, font, scale, color, thickness)
    img = cv2.putText(img, "Manthan Nagpurkar", (10, height-1), font, 4, (0, 0, 0), 10, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()