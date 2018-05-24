import sys 
import cv2 
import numpy as np 
 
class ObjectTracker(): 
    def __init__(self): 
        # Initialize the video capture object 
        # 0 -> indicates that frame should be captured 
        # from webcam 
        self.cap = cv2.VideoCapture(0) 
 
        # Capture the frame from the webcam 
        ret, self.frame = self.cap.read() 
 
        # Downsampling factor for the input frame 
        self.scaling_factor = 0.8 
        self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA) 
 
        cv2.namedWindow('Object Tracker') 
        cv2.setMouseCallback('Object Tracker', self.mouse_event) 
 
        self.selection = None 
        self.drag_start = None 
        self.tracking_state = 0 
 
    # Method to track mouse events 
    def mouse_event(self, event, x, y, flags, param): 
        x, y = np.int16([x, y]) 
 
        # Detecting the mouse button down event 
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.drag_start = (x, y) 
            self.tracking_state = 0 
 
        if self.drag_start:
            if event == cv2.EVENT_MOUSEMOVE:
                h, w = self.frame.shape[:2] 
                xo, yo = self.drag_start 
                x0, y0 = np.maximum(0, np.minimum([xo, yo], [x, y]))               
                x1, y1 = np.minimum([w, h], np.maximum([xo, yo], [x, y])) 
                self.selection = None 
 
                if x1-x0 > 0 and y1-y0 > 0:
                    self.selection = (x0, y0, x1, y1) 
 
            elif event == cv2.EVENT_LBUTTONUP:
                self.drag_start = None 
                if self.selection is not None: 
                    self.tracking_state = 1 
 
    # Method to start tracking the object 
    def start_tracking(self): 
        # Iterate until the user presses the Esc key 
        while True: 
            # Capture the frame from webcam 
            ret, self.frame = self.cap.read() 
            # Resize the input frame 
            self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA) 
 
            vis = self.frame.copy() 
 
            # Convert to HSV colorspace 
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV) 
 
            # Create the mask based on predefined thresholds. 
            mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.))) 
 
            if self.selection: 
                x0, y0, x1, y1 = self.selection 
                self.track_window = (x0, y0, x1-x0, y1-y0) 
                hsv_roi = hsv[y0:y1, x0:x1] 
                mask_roi = mask[y0:y1, x0:x1] 
 
                # Compute the histogram 
                hist = cv2.calcHist( [hsv_roi], [0], mask_roi, [16], [0, 180] ) 
 
                # Normalize and reshape the histogram 
                cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX); 
                self.hist = hist.reshape(-1) 
 
                vis_roi = vis[y0:y1, x0:x1] 
                cv2.bitwise_not(vis_roi, vis_roi) 
                vis[mask == 0] = 0 
 
            if self.tracking_state == 1: 
                print('tracking')
                self.selection = None 
 
                # Compute the histogram back projection 
                prob = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1) 
 
                prob &= mask 
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 ) 
 
                # Apply CAMShift on 'prob' 
                track_box, self.track_window = cv2.CamShift(prob, self.track_window, term_crit) 
 
                # Draw an ellipse around the object 
                cv2.ellipse(vis, track_box, (0, 255, 0), 2) 
 
            cv2.imshow('Object Tracker', vis) 
 
            c = cv2.waitKey(delay=5) 
            if c == 27: 
                break 
 
        cv2.destroyAllWindows() 
 
if __name__ == '__main__': 
    ObjectTracker().start_tracking() 