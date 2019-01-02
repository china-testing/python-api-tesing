#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/china-testing/python-api-tesing/blob/master/practices/ts/lr_pd.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-01-02

import pandas as pd
from sklearn import datasets
import tensorflow as tf
import itertools	

def get_input_fn(data_set, num_epochs=None, n_batch = 128, shuffle=True):   
   
    x = pd.DataFrame({k: data_set[k].values for k in FEATURES})
    y = pd.Series(data_set[LABEL].values)
    return tf.estimator.inputs.pandas_input_fn(       
        x=x, y=y,  batch_size=n_batch, num_epochs=num_epochs, shuffle=shuffle)


COLUMNS = ["crim", "zn", "indus", "nox", "rm", "age","dis", "tax", 
           "ptratio", "medv"]
FEATURES = ["crim", "zn", "indus", "nox", "rm",	"age", "dis", "tax", "ptratio"]
LABEL = "medv"

training_set = pd.read_csv("boston_train.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)
test_set = pd.read_csv("boston_test.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)
prediction_set = pd.read_csv("boston_predict.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)

print(training_set.shape, test_set.shape, prediction_set.shape)	


feature_cols = [tf.feature_column.numeric_column(k) for k in FEATURES]

estimator = tf.estimator.LinearRegressor(feature_columns=feature_cols,   
                                         model_dir="train")	

estimator.train(input_fn=get_input_fn(
    training_set, num_epochs=None, n_batch = 128, shuffle=False), steps=1000)		

ev = estimator.evaluate(input_fn=get_input_fn(test_set, num_epochs=1, 
    n_batch = 128, shuffle=False))	

loss_score = ev["loss"]
print("Loss: {0:f}".format(loss_score))
print(training_set['medv'].describe())


y = estimator.predict( input_fn=get_input_fn(prediction_set, num_epochs=1,                          
         n_batch = 128, shuffle=False))

predictions = list(p["predictions"] for p in itertools.islice(y, 6))
print("Predictions: {}".format(str(predictions)))	
