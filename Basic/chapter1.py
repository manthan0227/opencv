import cv2

''' for image'''
# img = cv2.imread('Resources/manthan1.jpg')
# cv2.imshow('output', img)
# cv2.waitKey(0)

''' for video'''
# cap = cv2.VideoCapture('Resources/vid1.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

''' for webcam'''
cap = cv2.VideoCapture(0) # 0 = camera, 1 = webcam
cap.set(3, 640)
cap.set(4, 489)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break