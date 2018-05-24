import cv2 
import numpy as np 
 
face_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_alt.xml') 
 
face_mask = cv2.imread('./images/mask_hannibal.png') 
h_mask, w_mask = face_mask.shape[:2] 
 
if face_cascade.empty(): 
    raise IOError('Unable to load the face cascade classifier xml file') 
 
cap = cv2.VideoCapture(1) 
scaling_factor = 0.5 
 
while True: 
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
 
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3) 
    for (x,y,w,h) in face_rects: 
        if h <= 0 or w <= 0: pass
        # Adjust the height and weight parameters depending on the sizes and the locations. 
        # You need to play around with these to make sure you get it right. 
        h, w = int(1.4*h), int(1.0*w) 
        y -= int(0.1*h)
        x = int(x)
        
        # Extract the region of interest from the image 
        frame_roi = frame[y:y+h, x:x+w] 
        face_mask_small = cv2.resize(face_mask, (w, h), interpolation=cv2.INTER_AREA) 

        # Convert color image to grayscale and threshold it 
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY) 
        ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV) 

        # Create an inverse mask 
        mask_inv = cv2.bitwise_not(mask) 

        try:
            # Use the mask to extract the face mask region of interest 
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask) 
            # Use the inverse mask to get the remaining part of the image 
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv) 
        except cv2.error as e:
            print('Ignoring arithmentic exceptions: '+ str(e))

        # add the two images to get the final output 
        frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
 
    cv2.imshow('Face Detector', frame) 
 
    c = cv2.waitKey(1) 
    if c == 27: 
        break 
 
cap.release() 
cv2.destroyAllWindows() 