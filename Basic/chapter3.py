import numpy as np
import cv2

img = cv2.imread('Resources/1.jpeg')
print(img.shape)

imgResize = cv2.resize(img, (300, 600)) #x=300, y=600
print(imgResize.shape)

imgCropped = img[0:200, 100:400] # y=0:200, x=100:400

cv2.imshow('Image', img)
cv2.imshow('Image Resize', imgResize)
cv2.imshow('Cropped Image', imgCropped)

cv2.waitKey(0)