#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://china-testing.github.io/pil1.html
# https://github.com/china-testing/python-api-tesing/blob/master/practices/pil_merge.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-12-04

import math
from PIL import Image

column = 11
width = 802
height = 286
size = (802, 286)

list_im = [r'd:\code.jpg', r'd:\code.jpg', r'd:\code.jpg', r'd:\code.jpg', 
           r'd:\code.jpg', r'd:\code.jpg', r'd:\code.jpg', r'd:\code.jpg',
           r'd:\code.jpg', r'd:\code.jpg', r'd:\code.jpg']
imgs = [Image.open(i) for i in list_im]

row_num = math.ceil(len(imgs)/column)
target = Image.new('RGB', (width*column, height*row_num))
for i in range(len(list_im)):
    if i % column == 0:
        end = len(list_im) if i + column > len(list_im) else i + column 
        for col, image in enumerate(imgs[i:i+column]):
            target.paste(image, (width*col, height*(i//column), 
                                 width*(col + 1), height*(i//column + 1)))   
target.show()
target.save('d:\code2.jpg')