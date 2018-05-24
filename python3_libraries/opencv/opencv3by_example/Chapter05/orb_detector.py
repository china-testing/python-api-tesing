import cv2 
import numpy as np 
 
input_image = cv2.imread('images/fishing_house.jpg') 
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
 
# Initiate ORB object, before opencv 3.0.0 use cv2.ORB()
orb = cv2.ORB_create() 
 
# find the keypoints with ORB 
keypoints = orb.detect(gray_image, None) 
 
# compute the descriptors with ORB 
keypoints, descriptors = orb.compute(gray_image, keypoints) 
 
# draw only the location of the keypoints without size or orientation 
cv2.drawKeypoints(input_image, keypoints, input_image, color=(0,255,0)) 
 
cv2.imshow('ORB keypoints', input_image) 
cv2.waitKey() 