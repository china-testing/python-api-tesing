import cv2 
import numpy as np 
 
face_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_alt.xml') 
eye_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_eye.xml') 
 
if face_cascade.empty(): 
  raise IOError('Unable to load the face cascade classifier xml file') 
if eye_cascade.empty(): 
  raise IOError('Unable to load the eye cascade classifier xml file') 
 
cap = cv2.VideoCapture(0)
sunglasses_img = cv2.imread('images/sunglasses.png')

while True:
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    vh, vw = frame.shape[:2]
    vh, vw = int(vh), int(vw)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1)
    centers = []

    for (x,y,w,h) in faces: 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        for (x_eye,y_eye,w_eye,h_eye) in eyes: 
            centers.append((x + int(x_eye + 0.5*w_eye), y + int(y_eye + 0.5*h_eye))) 
    
    if len(centers) > 1: # if detects both eyes
        h, w = sunglasses_img.shape[:2]
        # Extract the region of interest from the image 
        eye_distance = abs(centers[1][0] - centers[0][0])
        # Overlay sunglasses; the factor 2.12 is customizable depending on the size of the face 
        sunglasses_width = 2.12 * eye_distance
        scaling_factor = sunglasses_width / w
        print(scaling_factor, eye_distance)
        overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0] 
     
        # customizable X and Y locations; depends on the size of the face 
        x -= int(0.26*overlay_sunglasses.shape[1])
        y += int(0.26*overlay_sunglasses.shape[0])
        
        h, w = overlay_sunglasses.shape[:2]
        h, w = int(h), int(w)
        frame_roi = frame[y:y+h, x:x+w]
        # Convert color image to grayscale and threshold it 
        gray_overlay_sunglassess = cv2.cvtColor(overlay_sunglasses, cv2.COLOR_BGR2GRAY) 
        ret, mask = cv2.threshold(gray_overlay_sunglassess, 180, 255, cv2.THRESH_BINARY_INV) 

        # Create an inverse mask 
        mask_inv = cv2.bitwise_not(mask) 

        try:
            # Use the mask to extract the face mask region of interest 
            masked_face = cv2.bitwise_and(overlay_sunglasses, overlay_sunglasses, mask=mask) 
            # Use the inverse mask to get the remaining part of the image 
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv) 
        except cv2.error as e:
            print('Ignoring arithmentic exceptions: '+ str(e))
            #raise e

        # add the two images to get the final output 
        frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
    else:
        print('Eyes not detected')

    
    cv2.imshow('Eye Detector', frame) 
    c = cv2.waitKey(1) 
    if c == 27: 
        break 

cap.release() 
cv2.destroyAllWindows()