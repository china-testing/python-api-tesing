#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://china-testing.github.io/pil1.html
# https://github.com/china-testing/python-api-tesing/blob/master/practices/pillow/rotate.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-12-26
from PIL import Image

im = Image.open("qun.jpg")
print(im.size)
im.show()


im2 = im.rotate(45)
print(im2.size)
im2.show()
im2.save("test1.jpg")

im3 = im.rotate(45, expand=True)
print(im3.size)
im3.show()
im3.save("test2.jpg")

im4 = im.rotate(90)
print(im4.size)
im4.show()
im4.save("test3.jpg")

im5 = im.rotate(90, expand=True)
print(im5.size)
im5.show()
im5.save("test4.jpg")

out = im.transpose(Image.ROTATE_90)
out.show()
print(out.size)
im2.save("test5.jpg")
