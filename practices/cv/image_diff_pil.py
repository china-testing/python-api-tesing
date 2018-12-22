#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 项目实战讨论QQ群630011153 144081101
# https://github.com/china-testing/python-api-tesing/blob/master/practices/cv/image_diff_pil.py
# CreateDate: 2018-12-21
from PIL import Image
from PIL import ImageChops 

def compare_images(path1, path2, diff_save_location):
    
    image1 = Image.open(path1)
    image2 = Image.open(path2)
    diff = ImageChops.difference(image1, image2)
 
    if diff.getbbox():
        diff.save(diff_save_location)
 
if __name__ == '__main__':
    compare_images('images/original_01.png', 'images/modified_01.png',
                  'images/out.png')

