import cv2
import numpy as np

img = cv2.imread('Resources/1.jpeg')
kernel = np.ones((5,5), np.uint8)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 200, 150) # display the border of the image (borders are controlled by the parameter ex.(200,150))
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilatation Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)

