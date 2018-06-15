#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-12
# grayscale.py

from PIL import Image

def grayscale(img):
    """Return copy of img in grayscale."""
    width, height = img.size
    newimg = Image.new("RGB", (width, height))
    for j in range(height):
        for i in range(width):
            r, g, b = img.getpixel((i, j))
            avg = (r + g + b) // 3
            newimg.putpixel((i, j), (avg, avg, avg))
    return newimg
    
def main():
    img = Image.open("lake.jpg")
    newimg = grayscale(img)
    newimg.save("lake_gray.jpg")
    
main()
