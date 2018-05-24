import cv2 
import numpy as np 
 
img = cv2.imread('images/input.jpg', 0) 
 
kernel = np.ones((5,5), np.uint8) 
 
img_erosion = cv2.erode(img, kernel, iterations=1) 
img_dilation = cv2.dilate(img, kernel, iterations=1) 
 
cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
 
cv2.waitKey(0)