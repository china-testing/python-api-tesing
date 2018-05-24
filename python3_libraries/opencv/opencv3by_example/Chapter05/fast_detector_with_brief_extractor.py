import cv2 
import numpy as np 
 
input_image = cv2.imread('images/house.jpg') 
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
 
# Initiate FAST detector 
fast = cv2.FastFeatureDetector_create() 
 
# Initiate BRIEF extractor, before opencv 3.0.0 use cv2.DescriptorExtractor_create("BRIEF")
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create() 
 
# find the keypoints with STAR 
keypoints = fast.detect(gray_image, None) 

# compute the descriptors with BRIEF 
keypoints, descriptors = brief.compute(gray_image, keypoints) 
 
cv2.drawKeypoints(input_image, keypoints, input_image, color=(0,255,0)) 
cv2.imshow('BRIEF keypoints', input_image) 
cv2.waitKey()