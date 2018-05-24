import sys 
import cv2 
import numpy as np 
 
# Extract all the contours from the image 
def get_all_contours(img): 
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )
    return contours
 
if __name__=='__main__': 
    # Input image containing all the different shapes 
    img1 = cv2.imread(sys.argv[1]) 
    # Extract all the contours from the input image 
    input_contours = get_all_contours(img1) 
 
    contour_img = img1.copy()
    smoothen_contours = []
    factor = 0.01

    # Finding the closest contour 
    for contour in input_contours: 
        epsilon = factor * cv2.arcLength(contour, True) 
        smoothen_contours.append(cv2.approxPolyDP(contour, epsilon, True)) 
 
    cv2.drawContours(contour_img, smoothen_contours, -1, color=(0,0,0), thickness=3) 
    cv2.imshow('Contours', contour_img)
    cv2.waitKey() 