#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：6089740
# CreateDate: 2018-3-27
# pillow_rotate.py
import glob
import os 
from PIL import Image

def rotate(files, dst, value=90):
    for file_ in files:
        img = Image.open(file_)
        img = img.rotate(value)
        name = "{}{}{}".format(dst, os.sep, os.path.basename(file_))
        img.save(name)

src = r'/home/andrew/code/tmp_photos'
dst = r'/home/andrew/code/tmp_photos2'

common = glob.glob('{}{}*.*'.format(src, os.sep))  
rotate(common, dst)

