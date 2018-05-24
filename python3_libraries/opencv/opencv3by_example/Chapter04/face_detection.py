import cv2 
import numpy as np 
 
face_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_alt.xml') 
 
cap = cv2.VideoCapture(1) 
scaling_factor = 0.5 
 
while True: 
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx=scaling_factor, 
 fy=scaling_factor, interpolation=cv2.INTER_AREA)
 
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3) 
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3) 
 
    cv2.imshow('Face Detector', frame) 
 
    c = cv2.waitKey(1) 
    if c == 27: 
        break 
 
cap.release() 
cv2.destroyAllWindows() 