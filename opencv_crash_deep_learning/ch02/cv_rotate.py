# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-11-17

import imutils
import cv2

image = cv2.imread("jp.png")
rotated = imutils.rotate(image, 90)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)