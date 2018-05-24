#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-06

import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("test1.jpg")
locations = face_recognition.face_locations(image)
print(locations)
pos = locations[0]

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image, 'RGBA')
d.rectangle((pos[3], pos[0], pos[1], pos[2]))
pil_image.show()
pil_image.save("quick4.jpg")