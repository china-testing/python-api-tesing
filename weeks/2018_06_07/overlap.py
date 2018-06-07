#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-07


def get_area(pos):
    left, top, right, buttom = pos
    left = max(0, left)
    top = max(0, top)
    width = right - left
    height = buttom - top
    return (width*height, left, top, right, buttom)


def overlap(pos1, pos2):
    area1, left1, top1, right1, buttom1 = get_area(pos1)
    area2, left2, top2, right2, buttom2 = get_area(pos2)
    
    left = max(left1, left2)
    top = max(top1, top2)
    left = max(0, left)
    top = max(0, top)    
    right = min(right1, right2) 
    buttom = min(buttom1, buttom2)
    
    if right <= left or buttom <= top:
        area = 0
    else:
        area = (right - left)*(buttom - top)
        
    return (area, area1, area2, float(area)/area1, float(area)/area2)    

print(overlap((60, 188, 260, 387), (106, 291, 340, 530)))


