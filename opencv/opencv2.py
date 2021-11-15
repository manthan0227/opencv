import cv2
import random

img = cv2.imread('assets/assasian.png')
img = cv2.resize(img, (500, 400))

# print(type(img))
# print(img.shape)

# // numpy represents the pixels of the image
#
# [rows, columns, channels]
# [
#     [[], [], []],
#     [[], [], []],
#     [[], [], []]
# ]

# [0, 0 ,0] = RGB
# [255, 0, 0] = Blue
# [0, 255, 0] = Green
# [0, 0, 255] = red

# print(img[140][299])
# //EDIT THE IMAGE
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# //crop part of image
tag = img[200:300, 200:400]
# //crop image
# cv2.imwrite('Crop_image.png', tag)
img[100:200, 200:400] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
