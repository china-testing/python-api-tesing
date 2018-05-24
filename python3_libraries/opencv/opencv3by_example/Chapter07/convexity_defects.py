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
    img = cv2.imread(sys.argv[1]) 
 
    # Iterate over the extracted contours 
    for contour in get_all_contours(img): 
        # Extract convex hull from the contour 
        hull = cv2.convexHull(contour, returnPoints=False) 
 
        # Extract convexity defects from the above hull 
        defects = cv2.convexityDefects(contour, hull) 
 
        if defects is None: 
            continue 
 
        # Draw lines and circles to show the defects 
        for i in range(defects.shape[0]): 
            start_defect, end_defect, far_defect, _ = defects[i,0] 
            start = tuple(contour[start_defect][0]) 
            end = tuple(contour[end_defect][0]) 
            far = tuple(contour[far_defect][0]) 
            cv2.circle(img, far, 5, [128,0,0], -1) 
            cv2.drawContours(img, [contour], -1, color=(0,0,0), thickness=3) 
 
    cv2.imshow('Convexity defects',img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 