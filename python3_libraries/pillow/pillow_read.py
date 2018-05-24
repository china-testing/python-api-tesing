#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：6089740
# CreateDate: 2018-3-26
# pillow_read.py

from PIL import Image

im = Image.open("demo.jpg")
print(im.format, im.size, im.mode)
im.show()
im.save("demo.png")
