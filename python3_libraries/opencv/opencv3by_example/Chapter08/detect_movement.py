import cv2 
 
# Compute the frame difference 
def frame_diff(prev_frame, cur_frame, next_frame): 
    # Absolute difference between current frame and next frame 
    diff_frames1 = cv2.absdiff(next_frame, cur_frame) 
 
    # Absolute difference between current frame and 
     # previous frame 
    diff_frames2 = cv2.absdiff(cur_frame, prev_frame) 
 
    # Return the result of bitwise 'AND' between the 
     # above two resultant images 
    return cv2.bitwise_and(diff_frames1, diff_frames2) 
 
# Capture the frame from webcam 
def get_frame(cap, scaling_factor): 
    # Capture the frame 
    ret, frame = cap.read() 
 
    # Resize the image 
    frame = cv2.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv2.INTER_AREA) 
 
    return frame
 
if __name__=='__main__': 
    cap = cv2.VideoCapture(0)   
    scaling_factor = 0.5
 
    cur_frame, prev_frame, next_frame = None, None, None
    while True:
        frame = get_frame(cap, scaling_factor)
        prev_frame = cur_frame 
        cur_frame = next_frame
        # Convert frame to grayscale image 
        next_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        if prev_frame is not None:
            cv2.imshow("Object Movement", frame_diff(prev_frame, cur_frame, next_frame)) 

        key = cv2.waitKey(delay=10) 
        if key == 27: 
            break 
 
    cv2.destroyAllWindows() 