#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong@126.com wechat:pythontesting qq群:144081101
# CreateDate: 2018-04-25
import pytesseract as pt
import requests
from PIL import Image

#img = Image.open("textinimage.png")
print("英文:")
url = "https://xurongzhong.github.io/images/python_lib_ocr_en.png"
img = Image.open(requests.get(url, stream=True).raw)
text = pt.image_to_string(img)
print(text)
#img = Image.open("textinimage.png")
print("中文:")
url = "https://xurongzhong.github.io/images/python_lib_ocr.PNG"
img = Image.open(requests.get(url, stream=True).raw)
text = pt.image_to_string(img,lang='chi_sim')
print(text)
