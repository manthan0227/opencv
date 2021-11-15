# Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)

# img[:] = 255, 0, 255  # change the color of the screen
# img[0:300, 100: 300] = 255, 0, 0

cv2.line(img, (0,0), (img.shape[1], img.shape[0]),(0,255,0), 3) # Line with thickness 3
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2) # Rectangle with thickness 2
# cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), cv2.FILLED) # Rectangle with Filled color
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.putText(img, 'OPENCV', (300, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 250, 0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)

