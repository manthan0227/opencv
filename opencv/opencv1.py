import cv2

img = cv2.imread('assets/assasian.png', 1)

# // resize the image
# img = cv2.resize(img, (600, 600))
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()