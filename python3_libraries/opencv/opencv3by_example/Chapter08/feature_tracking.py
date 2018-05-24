import cv2 
import numpy as np 
 
# Extract area of interest based on the tracking_paths
# In case there is none, entire frame is used
def calculate_region_of_interest(frame, tracking_paths):
    mask = np.zeros_like(frame) 
    mask[:] = 255 
    for x, y in [np.int32(tp[-1]) for tp in tracking_paths]: 
        cv2.circle(mask, (x, y), 6, 0, -1) 
    return mask

def add_tracking_paths(frame, tracking_paths):
    mask = calculate_region_of_interest(frame, tracking_paths)
 
    # Extract good features to track. You can learn more 
    # about the parameters here: http://goo.gl/BI2Kml 
    feature_points = cv2.goodFeaturesToTrack(frame, mask = mask, maxCorners = 500, \
        qualityLevel = 0.3, minDistance = 7, blockSize = 7) 

    if feature_points is not None: 
        for x, y in np.float32(feature_points).reshape(-1, 2): 
            tracking_paths.append([(x, y)])

def compute_feature_points(tracking_paths, prev_img, current_img):
    feature_points = [tp[-1] for tp in tracking_paths]
    # Vector of 2D points for which the flow needs to be found
    feature_points_0 = np.float32(feature_points).reshape(-1, 1, 2) 

    feature_points_1, status_1, err_1 = cv2.calcOpticalFlowPyrLK(prev_img, current_img, \
        feature_points_0, None, **tracking_params) 
    feature_points_0_rev, status_2, err_2 = cv2.calcOpticalFlowPyrLK(current_img, prev_img, \
        feature_points_1, None, **tracking_params)

    # Compute the difference of the feature points 
    diff_feature_points = abs(feature_points_0-feature_points_0_rev).reshape(-1, 2).max(-1) 

    # threshold and keep only the good points 
    good_points = diff_feature_points < 1
    return feature_points_1.reshape(-1, 2), good_points

def start_tracking(cap, scaling_factor, num_frames_to_track, num_frames_jump, tracking_params): 
    tracking_paths = [] 
    frame_index = 0 
 
    # Iterate until the user presses the ESC key 
    while True: 
        # read the input frame 
        ret, frame = cap.read() 
 
        # downsample the input frame 
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA) 
 
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        output_img = frame.copy() 
 
        if len(tracking_paths) > 0: 
            prev_img, current_img = prev_gray, frame_gray
            # Compute feature points using optical flow. You can 
            # refer to the documentation to learn more about the 
            # parameters here: http://goo.gl/t6P4SE
            feature_points, good_points = compute_feature_points(tracking_paths, prev_img, current_img)
 
            new_tracking_paths = []
            for tp, (x, y), good_points_flag in \
                zip(tracking_paths, feature_points, good_points): 
                if not good_points_flag: continue 
 
                tp.append((x, y)) 
 
                # Using the queue structure i.e. first in, first out 
                if len(tp) > num_frames_to_track: del tp[0] 
 
                new_tracking_paths.append(tp) 
 
                # draw green circles on top of the output image 
                cv2.circle(output_img, (x, y), 3, (0, 255, 0), -1) 
 
            tracking_paths = new_tracking_paths 
 
            # draw green lines on top of the output image 
            point_paths = [np.int32(tp) for tp in tracking_paths]
            cv2.polylines(output_img, point_paths, False, (0, 150, 0)) 
 
        # 'if' condition to skip every 'n'th frame 
        if not frame_index % num_frames_jump: 
            add_tracking_paths(frame_gray, tracking_paths)

        frame_index += 1 
        prev_gray = frame_gray 
 
        cv2.imshow('Optical Flow', output_img) 
 
        # Check if the user pressed the ESC key 
        c = cv2.waitKey(1) 
        if c == 27: 
            break 
 
if __name__ == '__main__': 
    # Capture the input frame 
    cap = cv2.VideoCapture(1) 
 
    # Downsampling factor for the image 
    scaling_factor = 0.5 
 
    # Number of frames to keep in the buffer when you 
    # are tracking. If you increase this number, 
    # feature points will have more "inertia" 
    num_frames_to_track = 5 
 
    # Skip every 'n' frames. This is just to increase the speed. 
    num_frames_jump = 2 

    # 'winSize' refers to the size of each patch. These patches 
    # are the smallest blocks on which we operate and track 
    # the feature points. You can read more about the parameters 
    # here: http://goo.gl/ulwqLk 
    tracking_params = dict(winSize  = (11, 11), maxLevel = 2, \
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 
 
    start_tracking(cap, scaling_factor, num_frames_to_track, \
        num_frames_jump, tracking_params) 
    cv2.destroyAllWindows() 