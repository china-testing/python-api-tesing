#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-12 
# bowtie.py
# Draw a bowtie

from turtle import *

pensize(7)
penup()
goto(-200, -100)
pendown()
fillcolor("red")
begin_fill()
goto(-200, 100)
goto(200, -100)
goto(200, 100)
goto(-200, -100)
end_fill()

exitonclick()
