import cv2

gray_img = cv2.imread('images/input.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', gray_img)
cv2.imwrite('images/output.jpg', gray_img)
cv2.waitKey()