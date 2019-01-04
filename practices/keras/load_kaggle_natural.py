#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 项目实战讨论QQ群630011153 144081101
# https://github.com/china-testing/python-api-tesing/blob/master/practices/keras/load_kaggle_natural.py
# 数据集：https://itbooks.pipipan.com/fs/18113597-329046186
# CreateDate: 2019-01-04
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Model, load_model
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16

train_path = 'images/train/'
test_path = 'images/test/'
batch_size = 16
image_size = 224
num_class = 8


train_datagen = ImageDataGenerator(
    validation_split=0.3, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
    directory=train_path, target_size=(image_size,image_size),
    batch_size=batch_size, class_mode='categorical',
    color_mode='rgb', shuffle=True)


x_batch, y_batch = train_generator.next()

fig=plt.figure()
columns = 4
rows = 4
for i in range(1, columns*rows):
    num = np.random.randint(batch_size)
    image = x_batch[num].astype(np.int)
    fig.add_subplot(rows, columns, i)
    plt.imshow(image)
plt.show()

#Load the VGG model
base_model = VGG16(weights='imagenet', include_top=False, 
                   input_shape=(image_size, image_size, 3))

print(base_model.summary())

    # Freeze the layers 
for layer in base_model.layers:
    layer.trainable = False
 
# # Create the model
model = keras.models.Sequential()

# # Add the vgg convolutional base model
model.add(base_model)
 
# # Add new layers
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(num_class, activation='softmax'))
 
# # Show a summary of the model. Check the number of trainable parameters    
print(model.summary())