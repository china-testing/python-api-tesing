import sys 
import cv2 
import numpy as np 
 
# Extract all the contours from the image 
def get_all_contours(img): 
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0) 
    # Find all the contours in the thresholded image. The values 
    # for the second and third parameters are restricted to a 
    # certain number of possible values. You can learn more 'findContours' function here: 
    # http://docs.opencv.org/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html#findcontours
    im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )
    return contours

# Extract reference contour from the image 
def get_ref_contour(img): 
    contours = get_all_contours(img)

    # Extract the relevant contour based on area ratio. We use the 
    # area ratio because the main image boundary contour is 
    # extracted as well and we don't want that. This area ratio 
    # threshold will ensure that we only take the contour inside the image. 
    for contour in contours: 
        area = cv2.contourArea(contour) 
        img_area = img.shape[0] * img.shape[1] 
        if 0.05 < area/float(img_area) < 0.8: 
            return contour 
 
if __name__=='__main__': 
    # Boomerang reference image 
    img1 = cv2.imread(sys.argv[1]) 
 
    # Input image containing all the different shapes 
    img2 = cv2.imread(sys.argv[2]) 
 
    # Extract the reference contour 
    ref_contour = get_ref_contour(img1)
 
    # Extract all the contours from the input image 
    input_contours = get_all_contours(img2) 
 
    closest_contour = None
    min_dist = None
    contour_img = img2.copy()
    cv2.drawContours(contour_img, input_contours, -1, color=(0,0,0), thickness=3) 
    cv2.imshow('Contours', contour_img)
    # Finding the closest contour 
    for i, contour in enumerate(input_contours): 
        # Matching the shapes and taking the closest one using 
        # Comparison method CV_CONTOURS_MATCH_I3 (second argument)
        ret = cv2.matchShapes(ref_contour, contour, 3, 0.0)
        print("Contour %d matchs in %f" % (i, ret))
        if min_dist is None or ret < min_dist:
            min_dist = ret 
            closest_contour = contour
 
    cv2.drawContours(img2, [closest_contour], 0 , color=(0,0,0), thickness=3) 
    cv2.imshow('Best Matching', img2)
    cv2.waitKey() 