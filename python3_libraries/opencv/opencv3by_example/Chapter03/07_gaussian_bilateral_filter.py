import cv2 
import numpy as np 
 
img = cv2.imread('images/input.jpg') 
 
img_gaussian = cv2.GaussianBlur(img, (13,13), 0) 
img_bilateral = cv2.bilateralFilter(img, 13, 70, 50) 
 
cv2.imshow('Input', img) 
cv2.imshow('Gaussian filter', img_gaussian) 
cv2.imshow('Bilateral filter', img_bilateral) 
cv2.waitKey() 