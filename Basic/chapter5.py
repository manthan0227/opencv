# Wrap perspective

import cv2
import numpy as np

img = cv2.imread('Resources/k.jpg')

width, height = 250, 350

print(img.shape)
# cv2.rectangle(img, (140, 0), (280, 200), (255, 0, 0), 2)
# for finding the (x,y) points of the spade knight
pts1 = np.float32([[140,0], [280, 0], [140, 200], [280,200]]) #we have to find pts1 from the image
pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
spadeKnight = cv2.warpPerspective(img, matrix, (width, height))

#for club knight
pts1 = np.float32([[424,0], [563, 200], [563, 0], [424, 200]])
pts2 = np.float32([[0,0], [width, height], [width, 0], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
clubKnight = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Spade Knight', spadeKnight)
cv2.imshow('Club Knight', clubKnight)

cv2.waitKey(0)

