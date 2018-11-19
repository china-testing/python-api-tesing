# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-11-17

from PIL import Image

im = Image.open("jp.png")
im2 = im.rotate(90, expand=True)
im2.show()