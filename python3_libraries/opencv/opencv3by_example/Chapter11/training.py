import argparse
import random
import cv2
import numpy as np
import pickle
import math
from sklearn import preprocessing
from collections import OrderedDict

class ClassifierANN(object):
    def __init__(self, feature_vector_size, label_words):
        self.ann = cv2.ml.ANN_MLP_create()
        # Number of centroids used to build the feature vectors
        input_size = feature_vector_size
        # Number of models to recongnize
        output_size = len(label_words)
        # Applying Heaton rules
        hidden_size = (input_size * (2 / 3)) + output_size
        nn_config = np.array([input_size, hidden_size, output_size], dtype=np.uint8)
        self.label_words = label_words
        self.ann.setLayerSizes(np.array(nn_config))
        # Symmetrical Sigmoid as activation function
        self.ann.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)
        # Map models as tuples of probabilities
        self.le = preprocessing.LabelBinarizer()
        self.le.fit(label_words)  # Label words are ['dress', 'footwear', 'backpack']

    def train(self, training_set):
        label_words = [item['label'] for item in training_set]
        dim_size = training_set[0]['feature_vector'].shape[1]
        train_samples = np.asarray(
            [np.reshape(x['feature_vector'], (dim_size,)) for x in training_set]
        )
        # Convert item labels into encoded binary tuples
        train_response = np.array(self.le.transform(label_words), dtype=np.float32)
        self.ann.train(np.array(train_samples,
                                dtype=np.float32), cv2.ml.ROW_SAMPLE,
                       np.array(train_response, dtype=np.float32)
                       )

    def get_confusion_matrix(self, testing_set):
        feature_vectors, expected_labels = self._get_network_io(testing_set)
        confusion_matrix = self._init_confusion_matrix(self.label_words)
        retval, test_outputs = self.ann.predict(feature_vectors)
        for expected_output, test_output in zip(expected_labels, test_outputs):
            expected_model = self.classify(expected_output)
            predicted_model = self.classify(test_output)
            confusion_matrix[expected_model][predicted_model] += 1
        return confusion_matrix

    def classify(self, encoded_word, threshold = 0.5):
        models = self.le.inverse_transform(np.asarray([encoded_word]), threshold)
        return models[0]

    def _get_network_io(self, features_map):
        label_words = [ item['label'] for item in features_map]
        dim_size = features_map[0]['feature_vector'].shape[1]
        inputs = np.asarray([np.reshape(x['feature_vector'], (dim_size,)) for x in features_map])
        outputs = np.array(self.le.transform(label_words), dtype=np.float32)
        return inputs, outputs

    def _init_confusion_matrix(self, label_words):
        confusion_matrix =  OrderedDict()
        for label in label_words:
            confusion_matrix[label] = OrderedDict()
            for label2 in label_words: confusion_matrix[label][label2] = 0
        return confusion_matrix

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Creates features for given images')
    parser.add_argument("--feature-map-file", dest="feature_map_file", required=True,
        help="Input pickle file containing the feature map")
    parser.add_argument("--training-set", dest="training_set", required=True,
        help="Percentage taken for training. ie 0.75")
    parser.add_argument("--ann-file", dest="ann_file", required=False,
        help="Output file where ANN will be stored")
    parser.add_argument("--le-file", dest="le_file", required=False,
                        help="Output file where LabelEncoder class will be stored")
    return parser

def print_confusion_matrix(confusion_matrix):
    expected_model = confusion_matrix.keys()
    print ('\t\t', '\t'.join([expected_type.ljust(15) for expected_type in expected_model]))

    for expected_type in expected_model:
        values = []
        for predicted_values in confusion_matrix.values():
            for predicted_model, value in predicted_values.items():
                if predicted_model == expected_type: values.append(str(value).ljust(10))
        print('%s\t\t%s' % (expected_type.ljust(15), '\t'.join(values)))


def print_accuracy(confusion_matrix):
    acc_models = OrderedDict()
    for model in confusion_matrix.keys():
        acc_models[model] = {'TP':0, 'TN':0, 'FP':0, 'FN': 0}
    for expected_model, predicted_models in confusion_matrix.items():
        for predicted_model, value in predicted_models.items():
            if predicted_model == expected_model:
                acc_models[expected_model]['TP'] += value
                acc_models[predicted_model]['TN'] += value
            else:
                acc_models[expected_model]['FN'] += value
                acc_models[predicted_model]['FP'] += value


    for model, rep in acc_models.items():
        acc = (rep['TP']+rep['TN'])/(rep['TP']+rep['TN']+rep['FN']+rep['FP'])
        print('%s \t %f' % (model,acc))


def split_feature_map(feature_map, training_set_per):
    feature_map_dict = dict()
    for item in feature_map:
        label = item['label']
        if label not in feature_map_dict: feature_map_dict[label] = list()
        feature_map_dict[label].append(item)

    training_feature_map = []
    testing_feature_map = []
    for label, feature_map_list in feature_map_dict.items():
        slice = math.trunc(len(feature_map_list) * training_set_per)
        random.shuffle(feature_map_list)
        training_feature_map += feature_map_list[:slice]
        testing_feature_map += feature_map_list[slice:]
    return training_feature_map, testing_feature_map

if __name__ == '__main__':
    args = build_arg_parser().parse_args()

    # Load the Feature Map
    with open(args.feature_map_file, 'rb') as f:
        feature_map = pickle.load(f)

    training_set, testing_set = split_feature_map(feature_map, float(args.training_set))
    label_words = np.unique([item['label'] for item in training_set])
    cnn = ClassifierANN(len(feature_map[0]['feature_vector'][0]), label_words)
    cnn.train(training_set)
    print("===== Confusion Matrix =====")
    confusion_matrix = cnn.get_confusion_matrix(testing_set)
    print_confusion_matrix(confusion_matrix)
    print("===== ANN Accuracy =====")
    print_accuracy(confusion_matrix)

    if 'ann_file' in args and 'le_file' in args:
        print("===== Saving ANN =====")
        with open(args.ann_file, 'wb') as f:
            cnn.ann.save(args.ann_file)
        with open(args.le_file, 'wb') as f:
            pickle.dump(cnn.le, f)
        print('Saved in: ', args.ann_file)