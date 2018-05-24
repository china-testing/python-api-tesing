import math 
 
import cv2 

eye_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_eye.xml')
if eye_cascade.empty():
  raise IOError('Unable to load the eye cascade classifier xml file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5
ret, frame = cap.read()
contours = []

while True: 
  ret, frame = cap.read() 
  frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1)
  for (x_eye, y_eye, w_eye, h_eye) in eyes:
    pupil_frame = gray[y_eye:y_eye + h_eye, x_eye:x_eye + w_eye]
    ret, thresh = cv2.threshold(pupil_frame, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("threshold", thresh)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)

    for contour in contours:
      area = cv2.contourArea(contour)
      rect = cv2.boundingRect(contour)
      x, y, w, h = rect
      radius = 0.15 * (w + h)

      area_condition = (100 <= area <= 200)
      symmetry_condition = (abs(1 - float(w)/float(h)) <= 0.2)
      fill_condition = (abs(1 - (area / (math.pi * math.pow(radius, 2.0)))) <= 0.4)
      cv2.circle(frame, (int(x_eye + x + radius), int(y_eye + y + radius)), int(1.3 * radius), (0, 180, 0), -1)

  cv2.imshow('Pupil Detector', frame)
  c = cv2.waitKey(1) 
  if c == 27: 
    break
  
cap.release() 
cv2.destroyAllWindows()