import cv2 
import numpy as np 
 
img = cv2.imread('images/geometric.png', cv2.IMREAD_GRAYSCALE) 
rows, cols = img.shape 
 
# It is used depth of cv2.CV_64F.
sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# Kernel size can be: 1,3,5 or 7.
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5) 
 
laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 50, 240)

cv2.imshow('Original', img) 
cv2.imshow('Sobel horizontal', sobel_horizontal) 
cv2.imshow('Sobel vertical', sobel_vertical)

cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)
 
cv2.waitKey(0) 