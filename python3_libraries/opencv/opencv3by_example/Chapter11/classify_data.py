import argparse
import _pickle as pickle 
 
import cv2 
import numpy as np 

import create_features as cf
 
# Classifying an image 
class ImageClassifier(object): 
    def __init__(self, ann_file, le_file, codebook_file):
        with open(ann_file, 'rb') as f:
            self.ann = cv2.ml.ANN_MLP_load(ann_file)
        with open(le_file, 'rb') as f:
            self.le = pickle.load(f)

        # Load the codebook 
        with open(codebook_file, 'rb') as f: 
            self.kmeans, self.centroids = pickle.load(f)

    def classify(self, encoded_word, threshold=None):
        models = self.le.inverse_transform(np.asarray(encoded_word), threshold)
        return models[0]

    # Method to get the output image tag 
    def getImageTag(self, img): 
        # Resize the input image 
        img = cf.resize_to_size(img) 
        # Extract the feature vector
        feature_vector = cf.FeatureExtractor().get_feature_vector(img, self.kmeans, self.centroids) 
        # Classify the feature vector and get the output tag
        retval, image_tag = self.ann.predict(feature_vector)
        return self.classify(image_tag)


def build_arg_parser(): 
    parser = argparse.ArgumentParser(description='Extracts features from each line and classifies the data') 
    parser.add_argument("--input-image", dest="input_image", required=True,
        help="Input image to be classified")
    parser.add_argument("--codebook-file", dest="codebook_file", required=True,
        help="File containing the codebook")
    parser.add_argument("--ann-file", dest="ann_file", required=True,
        help="File containing trained ANN")
    parser.add_argument("--le-file", dest="le_file", required=True,
        help="File containing LabelEncoder class")
    return parser 
 
if __name__=='__main__': 
    args = build_arg_parser().parse_args() 
    codebook_file = args.codebook_file
    input_image = cv2.imread(args.input_image) 
 
    tag = ImageClassifier(args.ann_file, args.le_file, codebook_file).getImageTag(input_image)
    print("Output class:", tag)