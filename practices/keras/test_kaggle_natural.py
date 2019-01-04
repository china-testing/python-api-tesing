#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 项目实战讨论QQ群630011153 144081101
# https://github.com/china-testing/python-api-tesing/blob/master/practices/keras/test_kaggle_natural.py
# 数据集：https://itbooks.pipipan.com/fs/18113597-329046186
# CreateDate: 2019-01-04
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model


train_path = 'images/train/'
test_path = 'images/test/'
batch_size = 16
image_size = 224
num_class = 8


model = load_model('fine_tune.h5')

train_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(
    directory=train_path, target_size=(image_size,image_size),
    batch_size=batch_size, class_mode='categorical',
    color_mode='rgb', shuffle=True)


test_datagen = ImageDataGenerator()

test_generator = test_datagen.flow_from_directory(
    directory=test_path, target_size=(image_size, image_size),
    color_mode='rgb', shuffle=False, class_mode='categorical', batch_size=1)

filenames = test_generator.filenames
nb_samples = len(filenames)

fig=plt.figure()
columns = 4
rows = 4
for i in range(1, columns*rows -1):
    x_batch, y_batch = test_generator.next()

    name = model.predict(x_batch)
    name = np.argmax(name, axis=-1)
    true_name = y_batch
    true_name = np.argmax(true_name, axis=-1)

    label_map = (test_generator.class_indices)
    label_map = dict((v,k) for k,v in label_map.items()) #flip k,v
    predictions = [label_map[k] for k in name]
    true_value = [label_map[k] for k in true_name]

    image = x_batch[0].astype(np.int)
    fig.add_subplot(rows, columns, i)
    plt.title(str(predictions[0]) + ':' + str(true_value[0]))
    plt.imshow(image)
plt.show()