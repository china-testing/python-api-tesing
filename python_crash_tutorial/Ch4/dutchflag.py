#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-12
# dutchflag.py

from PIL import Image

def dutchflag(width, height):
    """Return new image of Dutch flag."""
    img = Image.new("RGB", (width, height))
    for j in range(height):
        for i in range(width):
            if j < height/3:
                img.putpixel((i, j), (255, 0, 0))
            elif j < 2*height/3:
                img.putpixel((i, j), (0, 255, 0))
            else:
                img.putpixel((i, j), (0, 0, 255))
    return img

def main():
    img = dutchflag(600, 400)
    img.save("dutchflag.jpg")
    
main()
