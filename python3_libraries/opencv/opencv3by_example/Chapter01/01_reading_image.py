import cv2

img = cv2.imread('./images/input.jpg')
print(type(img))
cv2.imshow('Input image', img)

cv2.waitKey()