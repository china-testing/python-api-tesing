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
    bgSubtractor = cv2.createBackgroundSubtractorMOG2()
 
    # This factor controls the learning rate of the algorithm. 
    # The learning rate refers to the rate at which your model 
    # will learn about the background. Higher value for 
    # 'history' indicates a slower learning rate. You 
    # can play with this parameter to see how it affects 
    # the output. 
    history = 100 
 
    # Iterate until the user presses the ESC key 
    while True: 
        frame = get_frame(cap, 0.5) 
 
        # Apply the background subtraction model to the input frame        
        mask = bgSubtractor.apply(frame, learningRate=1.0/history)
 
        # Convert from grayscale to 3-channel RGB 
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
 
        cv2.imshow('Input frame', frame)
        cv2.imshow('Moving Objects MOG', mask & frame)
 
        # Check if the user pressed the ESC key 
        c = cv2.waitKey(delay=30) 
        if c == 27: 
            break 
 
    cap.release() 
    cv2.destroyAllWindows() 