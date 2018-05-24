import cv2 
import numpy as np 
 
# Capture the input frame 
def get_frame(cap, scaling_factor=0.5): 
    ret, frame = cap.read() 
 
    # Resize the frame 
    frame = cv2.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv2.INTER_AREA) 
 
    return frame 
 
if __name__=='__main__': 
    # Initialize the video capture object 
    cap = cv2.VideoCapture(1) 
 
    # Create the background subtractor object 
    bgSubtractor= cv2.bgsegm.createBackgroundSubtractorGMG()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(3,3))

    # Iterate until the user presses the ESC key 
    while True: 
        frame = get_frame(cap, 0.5) 
 
        # Apply the background subtraction model to the input frame
        mask = bgSubtractor.apply(frame)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
 
        cv2.imshow('Input frame', frame)
        cv2.imshow('Moving Objects', mask)
 
        # Check if the user pressed the ESC key 
        c = cv2.waitKey(delay=30) 
        if c == 27: 
            break 
 
    cap.release() 
    cv2.destroyAllWindows() 