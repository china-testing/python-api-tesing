#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 钉钉或微信pythontesting 钉钉群21734177 技术支持qq群：630011153 144081101
# 代码地址 https://github.com/china-testing/python-api-tesing/blob/master/bazi/luohou.py
# 鸣谢 https://github.com/yuangu/sxtwl_cpp/tree/master/python
# CreateDate: 2019-2-21

import argparse
import sxtwl
import time
import datetime
import collections

from ganzhi import Gan, Zhi, ymc, rmc, zhi_time, jis


year_hous = {'子':'癸酉', '丑':'甲戌', '寅':'丁亥', '卯':'甲子', '辰':'乙丑', 
             '巳':'甲寅', '午':'丁卯', '未':'甲辰', '申':'己巳', '酉':'甲午', 
             '戌':'丁未', '亥':'甲申'}

ji_hous = {'春':'乙卯','夏':'丙午','秋':'庚申','冬':'辛酉'}
yue_hous = {'正':'亥', '二':'子', '三':'丑', '四':'寅', '五':'卯', '六':'辰', 
            '七':'巳', '八':'午', '九':'未', '十':'申', '十一':'酉', '十二':'戌'}
shi_hous = {'子':'丑午', '丑':'巳亥', '寅':'寅午', '卯':'辰戌', '辰':'巳丑', 
            '巳':'辰戌', '午':'卯申', '未':'午辰', '申':'戌丑', '酉':'子午', 
            '戌':'卯午', '亥':'辰卯'}

Gans = collections.namedtuple("Gans", "year month day")
Zhis = collections.namedtuple("Zhis", "year month day")


description = '''
# 年罗猴日
$ python luohou.py -d "2019 6 16"

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', action="store", help=u'year',default="")
parser.add_argument('-n', action="store", help=u'year',default=32, type=int)
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 05 05')
options = parser.parse_args()

Gans = collections.namedtuple("Gans", "year month day")
Zhis = collections.namedtuple("Zhis", "year month day")

if options.d:
    year, month, day = options.d.split()
    d = datetime.date(int(year), int(month), int(day))
else:
    d = datetime.datetime.today()
    
def get_hou(d):
    lunar = sxtwl.Lunar();
    cal_day = lunar.getDayBySolar(d.year, d.month, d.day)
    
    
    #　计算甲干相合    
    gans = Gans(year=Gan[cal_day.Lyear2.tg], month=Gan[cal_day.Lmonth2.tg], 
                day=Gan[cal_day.Lday2.tg])
    zhis = Zhis(year=Zhi[cal_day.Lyear2.dz], month=Zhi[cal_day.Lmonth2.dz], 
                day=Zhi[cal_day.Lday2.dz])
    
    
    print("公历:", end='')
    print("{}年{}月{}日".format(cal_day.y, cal_day.m, cal_day.d), end='')
    
    Lleap = "闰" if cal_day.Lleap else ""
    print("\t农历:", end='')
    print("{}年{}{}月{}日  ".format(cal_day.Lyear0 + 1984, Lleap, ymc[cal_day.Lmc], rmc[cal_day.Ldi]), end='')
    print(' \t',end='')
    print('-'.join([''.join(item) for item in zip(gans, zhis)]), end='')
    
    print("\t杀师时:", end='')   
    for item in shi_hous[zhis[2]]:
        print(item + zhi_time[item], end='')
    
    
    day_ganzhi = gans[2] + zhis[2]
    
    if day_ganzhi == year_hous[zhis[0]]:
        print(" \t年猴:{}年{}日".format(zhis[0], day_ganzhi), end=' ')
        
        
    if zhis[2] == yue_hous[ymc[cal_day.Lmc]]:
        print(" \t月罗:{}日".format(zhis[2]), end=' ')
    
    if day_ganzhi in tuple(ji_hous.values()):       
        birthday = d  
        for i in range(30):    
            day_ = sxtwl.Lunar().getDayBySolar(birthday.year, birthday.month, birthday.day)
            if day_.qk != -1:
                ji = jis[(day_.qk + 3)//6]
                break        
            birthday += datetime.timedelta(days=-1)
           
        if day_ganzhi == ji_hous[ji]:
            print(" \t季猴:{}季{}日".format(ji, ji_hous[ji]), end=' ')    
    print()


get_hou(d)      

for i in range(1,options.n):
    d_ = d + datetime.timedelta(days=i)
    get_hou(d_)  