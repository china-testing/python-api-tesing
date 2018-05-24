#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-06

import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("test1.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)

for face_landmarks in face_landmarks_list:
    
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')
    
    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=3)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=3)    
    
    pil_image.show()
    pil_image.save("quick3.jpg")
    