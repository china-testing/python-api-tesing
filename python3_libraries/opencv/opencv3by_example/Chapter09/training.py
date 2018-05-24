import os 
import sys 
import argparse 
 
import _pickle as pickle
import numpy as np 
from sklearn.multiclass import OneVsOneClassifier 
from sklearn.svm import LinearSVC 
from sklearn import preprocessing 
 
# To train the classifier 
class ClassifierTrainer(object): 
    def __init__(self, X, label_words): 
        # Encoding the labels (words to numbers) 
        self.le = preprocessing.LabelEncoder() 
 
        # Initialize One vs One Classifier using a linear kernel 
        self.clf = OneVsOneClassifier(LinearSVC(random_state=0)) 
 
        y = self._encodeLabels(label_words) 
        X = np.asarray(X) 
        self.clf.fit(X, y) 
 
    # Predict the output class for the input datapoint 
    def _fit(self, X): 
        X = np.asarray(X) 
        return self.clf.predict(X) 
 
    # Encode the labels (convert words to numbers) 
    def _encodeLabels(self, labels_words): 
        self.le.fit(labels_words) 
        return np.array(self.le.transform(labels_words), 
         dtype=np.float32) 
 
    # Classify the input datapoint 
    def classify(self, X): 
        labels_nums = self._fit(X) 
        labels_words = self.le.inverse_transform([int(x) for x in 
         labels_nums]) 
        return labels_words 
 
def build_arg_parser(): 
    parser = argparse.ArgumentParser(description='Trains the classifier models')
    parser.add_argument("--feature-map-file", dest="feature_map_file", required=True,\
        help="Input pickle file containing the feature map") 
    parser.add_argument("--svm-file", dest="svm_file", required=False,\
        help="Output file where the pickled SVM model will be stored") 
    return parser 
    
if __name__=='__main__': 
    args = build_arg_parser().parse_args() 
    feature_map_file = args.feature_map_file 
    svm_file = args.svm_file 
 
    # Load the feature map 
    with open(feature_map_file, 'rb') as f: 
        feature_map = pickle.load(f) 
 
    # Extract feature vectors and the labels 
    labels_words = [x['label'] for x in feature_map] 
 
    # Here, 0 refers to the first element in the 
    # feature_map, and 1 refers to the second 
    # element in the shape vector of that element 
    # (which gives us the size) 
    dim_size = feature_map[0]['feature_vector'].shape[1] 
 
    X = [np.reshape(x['feature_vector'], (dim_size,)) for x in feature_map] 
 
    # Train the SVM 
    svm = ClassifierTrainer(X, labels_words) 
    if args.svm_file: 
        with open(args.svm_file, 'wb') as f: 
            pickle.dump(svm, f) 