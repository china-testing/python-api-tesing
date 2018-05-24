import cv2 
import numpy as np 
 
img = cv2.imread('images/input.jpg') 
cv2.imshow('Original', img) 
 
# generating the kernels 
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]]) 
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1], 
                             [-1,2,2,2,-1], 
                             [-1,2,8,2,-1], 
                             [-1,2,2,2,-1], 
                             [-1,-1,-1,-1,-1]]) / 8.0 
 
# applying different kernels to the input image 
output_1 = cv2.filter2D(img, -1, kernel_sharpen_1) 
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2) 
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3) 
 
cv2.imshow('Sharpening', output_1) 
cv2.imshow('Excessive Sharpening', output_2) 
cv2.imshow('Edge Enhancement', output_3) 
cv2.waitKey(0) 