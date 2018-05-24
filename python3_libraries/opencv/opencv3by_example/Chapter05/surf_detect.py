import cv2 
import numpy as np 
 
input_image = cv2.imread('images/fishing_house.jpg') 
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
 
# For version opencv < 3.0.0, use cv2.SURF()
surf = cv2.xfeatures2d.SURF_create()
# This threshold controls the number of keypoints 
surf.setHessianThreshold(15000) 

keypoints, descriptors = surf.detectAndCompute(gray_image, None) 

cv2.drawKeypoints(input_image, keypoints, input_image, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
 
cv2.imshow('SURF features', input_image) 
cv2.waitKey() 