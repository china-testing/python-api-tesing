#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import  sxtwl
import argparse
import collections
import pprint
from bidict import bidict

from datas import *


description = '''

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year')
parser.add_argument('month', action="store", help=u'month')
parser.add_argument('day', action="store", help=u'day')
parser.add_argument('time', action="store", help=u'time')    
parser.add_argument('-b', action="store_true", default=False, help=u'直接输入八字')
parser.add_argument('-g', action="store_true", default=False, help=u'是否采用公历')
parser.add_argument('-r', action="store_true", default=False, help=u'是否为闰月，仅仅使用于农历')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 02 21')
options = parser.parse_args()

Gans = collections.namedtuple("Gans", "year month day time")
Zhis = collections.namedtuple("Zhis", "year month day time")

if options.b:
    gans = Gans(year=options.year[0], month=options.month[0], 
                day=options.day[0],  time=options.time[0])
    zhis = Gans(year=options.year[1], month=options.month[1], 
                day=options.day[1],  time=options.time[1])
else:

    lunar = sxtwl.Lunar();
    if options.g:
        day = lunar.getDayBySolar(
            int(options.year), int(options.month), int(options.day))
    else:
        day = lunar.getDayByLunar(
            int(options.year), int(options.month), int(options.day), options.r)

    gz = lunar.getShiGz(day.Lday2.tg, int(options.time))

    #　计算甲干相合    
    gans = Gans(year=Gan[day.Lyear2.tg], month=Gan[day.Lmonth2.tg], 
                day=Gan[day.Lday2.tg], time=Gan[gz.tg])
    zhis = Zhis(year=Zhi[day.Lyear2.dz], month=Zhi[day.Lmonth2.dz], 
                day=Zhi[day.Lday2.dz], time=Zhi[gz.dz])
me = gans.day
zhus = [item for item in zip(gans, zhis)]

if not options.b:
    print("\n日期:")
    print("======================================")  
    print("公历:")
    print("\t{}年{}月{}日".format(day.y, day.m, day.d))

    Lleap = "闰" if day.Lleap else ""
    print("农历:")
    print("\t{}年{}{}月{}日".format(day.Lyear0 + 1984, Lleap, ymc[day.Lmc], rmc[day.Ldi]))

print("\n八字:   同义词：七杀|偏官 偏印|枭神 阳刃|帝旺(阳干)|冠带(阴干)")
print("="*140)    
print("{:<30s}{:<30s}{:<30s}{:<30s}".format('年【父-根】', "月【兄弟僚友-苗】", "日【自己配偶-花】", "时【子孙-实】"))
print("-"*140)
print("{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}".format(
    gans.year, '{} [{}]'.format(gan5[gans.year], ten_deities[me][gans.year]),
    gans.month, '{} [{}]'.format(gan5[gans.month], ten_deities[me][gans.month]),
    me, '{} [{}]'.format(gan5[me], '自己'), 
    gans.time, '{} [{}]'.format(gan5[gans.time], ten_deities[me][gans.time]),
))
print("{:>11s}--{:<19s}{:>12s}--{:<19s}{:>12s}--{:<19s}{:>12s}--{:<19s}".format(
    zhis.year, ten_deities[me][zhis.year],
    zhis.month, ten_deities[me][zhis.month],
    zhis.day, ten_deities[me][zhis.day],
    zhis.time, ten_deities[me][zhis.time],
))
for item in zhis:
    out = ''
    for gan in zhi5[item]:
        out = out + "{}{}{}{} ".format(gan, gan5[gan], zhi5[item][gan],  ten_deities[me][gan])
    print("{:<25s}".format(out), end=' ')

print("\n\n")
print("="*140)  
print(dict(ten_deities[me]))
#print(ten_deities[me])

def check_subset(gans, db, desc):
    flag = True
    for item in db:
        if set(item).issubset(gans):
            if flag:
                print("\n\n{}:".format(desc))
                print("="*60)   
                flag = False
            print(item, db[item])    

check_subset(gans, gan_hes, '十干合')
check_subset(gans, gan_chongs, '十干冲')
check_subset(zhis, zhi_6hes, '地支六合')		
check_subset(zhis, zhi_3hes, '地支三合')		
check_subset(zhis, zhi_huis, '地支三会')	
check_subset(zhis, zhi_chongs, '地支相冲')	
check_subset(zhis, zhi_poes, '地支相破')	
check_subset(zhis, zhi_haies, '地支相害')	
check_subset(zhis, zhi_xings, '地支相刑')	


guan_list = []
for item in gans + zhis:
    if item in guans[me]:
        guan_list.append(item)
if guan_list:
    print("\n\n正官:")  
    print("=========================")   
    print("财印两扶,柱中不见伤煞,行运引至官乡,大富大贵命也, 月令最佳")  
    print("大忌刑冲破害、伤官七煞、贪合忘官、劫财分福,为破格")
    print("=========================")      
    print("恭喜，有贵人相助！", guan_list)

    # 检查天福贵人
    if lus[me] in guan_list:
        print("天福贵人:主科名巍峨，官职尊崇，多掌丝纶文翰之美!")

    # 岁德正官
    if gans[0] in guan_list:
        print("大岁德正官!")
    if zhis[0] in guan_list:
        print("小岁德正官!")  
    # 时上正官
    if gans[3] in guan_list:
        print("大时上正官!")
    if zhis[3] in guan_list:
        print("小时上正官!")          


if len(guan_list) == 1:    
    guan_chongs = []
    gui = guan_list[0]
    for item in gans + zhis:
        if item in chongs[gui]:
            guan_chongs.append(item)
    if guan_chongs:
        print("官冲",guan_list)    

    guan_xings = []
    l = list(gans + zhis)
    l.remove(gui)
    for item in l:
        if item in xings[gui]:
            guan_xings.append(item)
    if guan_xings:
        print("官刑",guan_xings) 

if zhus[2] in tianyuans:
    print("\n\n天元坐禄:")  
    print("=========================")   
    print('''
    金若遇火，有重权，防御刺史臣（如庚午、庚寅、庚戌、辛巳、辛未等日）
    水若遇土，入官局，可沾侍郎禄（如壬午、壬戌、癸巳、癸丑、癸未等日）
    木若遇金，主伤衰化煞，为权势若雷（如甲申、甲戌、乙巳、乙酉、乙丑等日）
    火若遇水，主兵权，为将镇三边（如丙申、丙子、丙辰、丁亥、丁丑等日）
    土若遇木，为正禄八座三台福（如戊寅、戊辰、己卯、己未、己亥等日）
    此即白虎持世等格要，日主与官贵相停，偏枯则不成造化，大忌刑冲破害，伤损贵气，不成格矣。
    如庚午日，坐丁官，喜见甲乙财生官，戊己印生身；忌丙煞杂官，癸水伤官，子冲破午。余干例推。
    如果日柱的干支本身已构成官星，就不大忌讳冲破。
    ''')  

    print("=========================")       
    print(zhus[2])

# 计算五行分数 http://www.131.com.tw/word/b3_2_14.htm

scores = {"金":0, "木":0, "水":0, "火":0, "土":0}

for item in gans:  
    scores[gan5[item]] += 150

for item in list(zhis) + [zhis.month]:  
    for gan in zhi5[item]:
        scores[gan5[gan]] += zhi5[item][gan]

print("\n\n五行分数") 
print("="*60)  
print(scores)
short = min(scores, key=scores.get)
print("\n\n五行缺{}的建议".format(short))    
print("=========================")    
print("{}".format(gan_health[short]))
