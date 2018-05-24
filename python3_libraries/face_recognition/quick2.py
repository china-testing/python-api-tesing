#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-06

import face_recognition
from PIL import Image

image = face_recognition.load_image_file("test0.jpg")
face_locations = face_recognition.face_locations(image,model="cnn")
top, right, bottom, left = face_locations[0]
print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
face_image = image[top:bottom, left:right]
pil_image = Image.fromarray(face_image)
pil_image.show()
pil_image.save("quick2.jpg")
