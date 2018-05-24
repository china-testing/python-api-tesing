#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-02-06

import face_recognition


image = face_recognition.load_image_file("test0.jpg")
face_locations = face_recognition.face_locations(image,model="cnn")
print(face_locations)
