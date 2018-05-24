#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-06 qq群： 144081101

import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("sleep.jpg")
locations = face_recognition.face_locations(image)
print(locations)
img = Image.open("sleep.jpg")
img = img.rotate(90,expand=1)
img.save("/tmp/tmp.jpg")
image = face_recognition.load_image_file("/tmp/tmp.jpg")
locations = face_recognition.face_locations(image)
print(locations)

pil_image = Image.fromarray(image)
pil_image.show()




