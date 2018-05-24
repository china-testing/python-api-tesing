import argparse
import _pickle as pickle 

import cv2 
import numpy as np 
from sklearn.cluster import KMeans 
 
class DenseDetector(): 
    def __init__(self, step_size=20, feature_scale=20, img_bound=20): 
        # Create a dense feature detector 
        self.initXyStep = step_size
        self.initFeatureScale = feature_scale
        self.initImgBound = img_bound
 
    def detect(self, img):
        keypoints = []
        rows, cols = img.shape[:2]
        for x in range(self.initImgBound, rows, self.initFeatureScale):
            for y in range(self.initImgBound, cols, self.initFeatureScale):
                keypoints.append(cv2.KeyPoint(float(x), float(y), self.initXyStep))
        return keypoints 

class SIFTExtractor():
    def __init__(self):
        self.extractor = cv2.xfeatures2d.SIFT_create()

    def compute(self, image, kps): 
        if image is None: 
            print("Not a valid image")
            raise TypeError 
 
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kps, des = self.extractor.detectAndCompute(gray_image, None)
        return kps, des


    def get_description(self, gray_image):
        extractor = cv2.xfeatures2d.SIFT_create()
        kps, des = extractor.detectAndCompute(gray_image, None)
        return kps, des


# Vector quantization 
class Quantizer(object): 
    def __init__(self, num_clusters=32):
        self.extractor = SIFTExtractor()
        self.num_clusters = num_clusters 
        self.num_retries = 10 
 
    def quantize(self, datapoints): 
        # Create KMeans object 
        kmeans = KMeans(self.num_clusters, 
                        n_init=max(self.num_retries, 1), 
                        max_iter=10, tol=1.0) 
 
        # Run KMeans on the datapoints 
        res = kmeans.fit(datapoints) 
 
        # Extract the centroids of those clusters 
        centroids = res.cluster_centers_
 
        return kmeans, centroids 
 
    def normalize(self, input_data): 
        sum_input = np.sum(input_data)
        return input_data / sum_input if sum_input > 0 else input_data
 
    # Extract feature vector from the image 
    def get_feature_vector(self, img, kmeans, centroids): 
        kps = DenseDetector().detect(img) 
        kps, fvs = self.extractor.compute(img, kps) 
        labels = kmeans.predict(fvs) 
        fv = np.zeros(self.num_clusters) 
 
        for i, item in enumerate(fvs): 
            fv[labels[i]] += 1 
 
        fv_image = np.reshape(fv, ((1, fv.shape[0]))) 
        return self.normalize(fv_image)


class FeatureExtractor(object):
    def __init__(self, image_path, optimal_size=150):
        img = cv2.imread(image_path)
        self.image = self.get_optimized_image(img, optimal_size)

    def get_feature_vector(self, num_clusters = 32):
        kmeans, centroids = self.get_centroids(self.image)
        return Quantizer(num_clusters).get_feature_vector(self.image, kmeans, centroids)

            # Extract the centroids from the feature points
    def get_centroids(self, image):
        kps_all = []
        # Dense feature detector
        kps = DenseDetector().detect(image)
        # SIFT feature extractor
        kps, fvs = SIFTExtractor().compute(image, kps)
        kps_all.extend(fvs)

        kmeans, centroids = Quantizer().quantize(kps_all)
        return kmeans, centroids

    def get_optimized_image(self, img, new_size=150):
        h, w = img.shape[0], img.shape[1]
        ds_factor = new_size / float(h)
        if w < h: ds_factor = new_size / float(w)
        new_size = (int(w * ds_factor), int(h * ds_factor))
        return cv2.resize(img, new_size)


def build_arg_parser():
    parser = argparse.ArgumentParser(description='Creates features for given image')
    parser.add_argument("--image", dest="image", required=True,
                        help="Path of image to extract features from")
    parser.add_argument("--class", dest="cls", required=True,
                        help="Class to append to image")
    parser.add_argument("--feature-map-file", dest='feature_map_file', required=True,
                        help="Base file name to store the feature map")

    return parser

if __name__=='__main__':
    args = build_arg_parser().parse_args()

    featureExtractor = FeatureExtractor(args.image)
    image_feature_vector = featureExtractor.get_feature_vector()

    # Input data and labels
    if 'feature_map_file' in args:
        print("===== Building feature map =====")
        if args.feature_map_file:
            with open(args.feature_map_file, 'wb') as f:
                pickle.dump({
                    'label': args.cls,
                    'feature_vector': image_feature_vector
                }, f)
                print('Saved in %s' % args.feature_map_file)