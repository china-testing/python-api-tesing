import sys 
from collections import namedtuple 
 
import cv2 
import numpy as np

class PoseEstimator(object): 
    def __init__(self): 
        # Use locality sensitive hashing algorithm 
        flann_params = dict(algorithm = 6, table_number = 6, key_size = 12, multi_probe_level = 1) 
 
        self.min_matches = 10 
        self.cur_target = namedtuple('Current', 'image, rect, keypoints, descriptors, data')
        self.tracked_target = namedtuple('Tracked', 'target, points_prev, points_cur, H, quad') 
 
        self.feature_detector = cv2.ORB_create()
        self.feature_detector.setMaxFeatures(1000)
        self.feature_matcher = cv2.FlannBasedMatcher(flann_params, {}) 
        self.tracking_targets = [] 
 
    # Function to add a new target for tracking 
    def add_target(self, image, rect, data=None): 
        x_start, y_start, x_end, y_end = rect 
        keypoints, descriptors = [], [] 
        for keypoint, descriptor in zip(*self.detect_features(image)): 
            x, y = keypoint.pt 
            if x_start <= x <= x_end and y_start <= y <= y_end: 
                keypoints.append(keypoint) 
                descriptors.append(descriptor) 
 
        descriptors = np.array(descriptors, dtype='uint8') 
        self.feature_matcher.add([descriptors]) 
        target = self.cur_target(image=image, rect=rect, keypoints=keypoints, descriptors=descriptors, data=None) 
        self.tracking_targets.append(target) 
 
    # To get a list of detected objects 
    def track_target(self, frame): 
        self.cur_keypoints, self.cur_descriptors = self.detect_features(frame) 

        if len(self.cur_keypoints) < self.min_matches: return []
        try: matches = self.feature_matcher.knnMatch(self.cur_descriptors, k=2)
        except Exception as e:
            print('Invalid target, please select another with features to extract')
            return []
        matches = [match[0] for match in matches if len(match) == 2 and match[0].distance < match[1].distance * 0.75] 
        if len(matches) < self.min_matches: return [] 
 
        matches_using_index = [[] for _ in range(len(self.tracking_targets))] 
        for match in matches: 
            matches_using_index[match.imgIdx].append(match) 
 
        tracked = [] 
        for image_index, matches in enumerate(matches_using_index): 
            if len(matches) < self.min_matches: continue 
 
            target = self.tracking_targets[image_index] 
            points_prev = [target.keypoints[m.trainIdx].pt for m in matches]
            points_cur = [self.cur_keypoints[m.queryIdx].pt for m in matches]
            points_prev, points_cur = np.float32((points_prev, points_cur))
            H, status = cv2.findHomography(points_prev, points_cur, cv2.RANSAC, 3.0) 
            status = status.ravel() != 0

            if status.sum() < self.min_matches: continue 
 
            points_prev, points_cur = points_prev[status], points_cur[status] 
 
            x_start, y_start, x_end, y_end = target.rect 
            quad = np.float32([[x_start, y_start], [x_end, y_start], [x_end, y_end], [x_start, y_end]])
            quad = cv2.perspectiveTransform(quad.reshape(1, -1, 2), H).reshape(-1, 2)
            track = self.tracked_target(target=target, points_prev=points_prev, points_cur=points_cur, H=H, quad=quad) 
            tracked.append(track) 
 
        tracked.sort(key = lambda x: len(x.points_prev), reverse=True) 
        return tracked 
 
    # Detect features in the selected ROIs and return the keypoints and descriptors 
    def detect_features(self, frame): 
        keypoints, descriptors = self.feature_detector.detectAndCompute(frame, None) 
        if descriptors is None: descriptors = [] 
        return keypoints, descriptors 
 
    # Function to clear all the existing targets 
    def clear_targets(self): 
        self.feature_matcher.clear() 
        self.tracking_targets = []  
 
class ROISelector(object): 
    def __init__(self, win_name, init_frame, callback_func): 
        self.callback_func = callback_func 
        self.selected_rect = None 
        self.drag_start = None 
        self.tracking_state = 0
        event_params = {"frame": init_frame}
        cv2.namedWindow(win_name)
        cv2.setMouseCallback(win_name, self.mouse_event, event_params)
 
    def mouse_event(self, event, x, y, flags, param):
        x, y = np.int16([x, y]) 
 
        # Detecting the mouse button down event 
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.drag_start = (x, y) 
            self.tracking_state = 0 
 
        if self.drag_start:
            if event == cv2.EVENT_MOUSEMOVE:
                h, w = param["frame"].shape[:2] 
                xo, yo = self.drag_start 
                x0, y0 = np.maximum(0, np.minimum([xo, yo], [x, y]))               
                x1, y1 = np.minimum([w, h], np.maximum([xo, yo], [x, y])) 
                self.selected_rect = None 
 
                if x1-x0 > 0 and y1-y0 > 0:
                    self.selected_rect = (x0, y0, x1, y1) 
 
            elif event == cv2.EVENT_LBUTTONUP:
                self.drag_start = None 
                if self.selected_rect is not None: 
                    self.callback_func(self.selected_rect)
                    self.selected_rect = None
                    self.tracking_state = 1

    def draw_rect(self, img, rect): 
        if not rect: return False 
        x_start, y_start, x_end, y_end = rect
        cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2) 
        return True 
 
class VideoHandler(object): 
    def __init__(self, capId, scaling_factor, win_name): 
        self.cap = cv2.VideoCapture(capId)
        self.pose_tracker = PoseEstimator() 
        self.win_name = win_name
        self.scaling_factor = scaling_factor

        ret, frame = self.cap.read()
        self.rect = None
        self.frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        self.roi_selector = ROISelector(win_name, self.frame, self.set_rect) 

    def set_rect(self, rect): 
        self.rect = rect
        self.pose_tracker.add_target(self.frame, rect) 

    def start(self):
        paused = False
        while True:
            if not paused or self.frame is None: 
                ret, frame = self.cap.read()
                scaling_factor = self.scaling_factor
                frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA) 
                if not ret: break 
                self.frame = frame.copy() 
 
            img = self.frame.copy() 
            if not paused and self.rect is not None: 
                tracked = self.pose_tracker.track_target(self.frame) 
                for item in tracked: 
                    cv2.polylines(img, [np.int32(item.quad)], True, (255, 255, 255), 2) 
                    for (x, y) in np.int32(item.points_cur): 
                        cv2.circle(img, (x, y), 2, (255, 255, 255)) 
 
            self.roi_selector.draw_rect(img, self.rect) 
            cv2.imshow(self.win_name, img) 
            ch = cv2.waitKey(1) 
            if ch == ord(' '): paused = not paused 
            if ch == ord('c'): self.pose_tracker.clear_targets() 
            if ch == 27: break

if __name__ == '__main__': 
    VideoHandler(0, 0.8, 'Tracker').start()