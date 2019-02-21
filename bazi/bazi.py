#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import  sxtwl
import argparse
import collections


Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
gan5 = {"甲":"木", "乙":"木", "丙":"火", "丁":"火", "戊":"土", "己":"土", 
    "庚":"金", "辛":"金", "壬":"水", "癸":"水"}
gan_health = {
    "金":"筋胸、大肠肺",
    "木":"头肩、肝胆",
    "水":"胫足、膀胱肾(比如结石)",    
    "火":"额齿、小肠心脏",
    "土":"鼻面、脾胃",      
}
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
zhi5 = {"子":{"癸":8}, 
        "丑":{"辛":1,"癸":2, "己":5}, 
        "寅":{"戊":1,"丙":2, "甲":5},
        "卯":{"乙":8}, 
        "辰":{"癸":1,"乙":2, "戊":5}, 
        "巳":{"庚":1,"戊":2, "丙":5}, 
        "午":{"己":3, "丁":5},
        "未":{"乙":1,"丁":2, "己":5}, 
        "申":{"戊":1,"壬":2, "庚":5},
        "酉":{"辛":8}, 
        "戌":{"丁":1,"辛":2, "戊":5}, 
        "亥":{"甲":3, "壬":5}}

ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
Week = ["日", "一", "二", "三", "四", "五", "六"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

gan_hes = {
    ("甲", "己"): "中正之合 化土",
    ("乙", "庚"): "仁义之合　化金",
    ("丙", "辛"): "丙义之合　化水",
    ("丁", "壬"): "淫慝之合　化木",    
    ("戊", "癸"): "无情之合　化火",    
}

gan_chongs = {
    ("甲", "庚"): "相冲",
    ("乙", "辛"): "相冲",
    ("丙", "壬"): "相冲",
    ("丁", "癸"): "相冲",       
}

zhi_6hes = {
    ("子", "丑"): "化土",
    ("寅", "亥"): "化木",
    ("卯", "戌"): "化火",
    ("辰", "酉"): "化金",    
    ("巳", "申"): "化水",    
    ("午", "未"): "化土",        
}

zhi_3hes = {
    ("申", "子", "辰"): "化水",
    ("巳", "酉", "丑"): "化金",  
    ("寅", "午", "戌"): "化火",       
    ("亥", "卯", "未"): "化木",
}

zhi_huis = {
    ("亥", "子", "丑"): "化水",
    ("寅", "卯", "辰"): "化木",  
    ("巳", "午", "未"): "化火",       
    ("申", "酉", "戌"): "化金",
}

zhi_chongs = {
    ("子", "午"): "相冲",
    ("丑", "未"): "相冲",
    ("寅", "申"): "相冲",
    ("卯", "酉"): "相冲",
    ("辰", "戌"): "相冲",   
    ("巳", "亥"): "相冲",       
}

zhi_poes = {
    ("子", "酉"): "相破",
    ("午", "卯"): "相破",
    ("巳", "申"): "相破",
    ("寅", "亥"): "相破",
    ("辰", "丑"): "相破",   
    ("戌", "未"): "相破",       
}

zhi_poes = {
    ("子", "酉"): "相破",
    ("午", "卯"): "相破",
    ("巳", "申"): "相破",
    ("寅", "亥"): "相破",
    ("辰", "丑"): "相破",   
    ("戌", "未"): "相破",       
}

zhi_haies = {
    ("子", "未"): "相害",
    ("丑", "午"): "相害",
    ("寅", "巳"): "相害",
    ("卯", "辰"): "相害",
    ("申", "亥"): "相害",   
    ("酉", "戌"): "相害",       
}

zhi_xings = {
    ("寅", "巳"): "寅刑巳 无恩之刑",
    ("巳", "申"): "巳刑申 无恩之刑",
    ("申", "寅"): "申刑寅 无恩之刑",
    ("未", "丑"): "未刑丑 持势之刑",
    ("丑", "戌"): "丑刑戌 持势之刑",   
    ("戌", "未"): "戌刑未 持势之刑",  
    ("子", "卯"): "子刑卯　卯刑子 无礼之刑",       
}

zhi_zixings = ['辰', '午', '酉', '亥']

description = '''

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year', type=int)
parser.add_argument('month', action="store", help=u'month', type=int)
parser.add_argument('day', action="store", help=u'day', type=int)
parser.add_argument('time', action="store", help=u'time', type=float)    
parser.add_argument('-g', action="store_true", default=False, help=u'是否采用公历')
parser.add_argument('-r', action="store_true", default=False, help=u'是否为闰月，仅仅使用于农历')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 02 21')
options = parser.parse_args()


lunar = sxtwl.Lunar();
if options.g:
    day = lunar.getDayBySolar(options.year, options.month, options.day)
else:
    day = lunar.getDayByLunar(options.year, options.month, options.day, options.r)

gz = lunar.getShiGz(day.Lday2.tg, int(options.time))

#　计算甲干相合 
Gans = collections.namedtuple("Gans", "year month day time")
gans = Gans(year=Gan[day.Lyear2.tg], month=Gan[day.Lmonth2.tg], day=Gan[day.Lday2.tg], time=Gan[gz.tg])
Zhis = collections.namedtuple("Zhis", "year month day time")
zhis = Zhis(year=Zhi[day.Lyear2.dz], month=Zhi[day.Lmonth2.dz], day=Zhi[day.Lday2.dz], time=Zhi[gz.dz])

print("\n日期:")
print("======================================")  
print("公历:")
print("\t{}年{}月{}日".format(day.y, day.m, day.d))

Lleap = "闰" if day.Lleap else ""
print("农历:")
print("\t{}年{}{}月{}日".format(day.Lyear0 + 1984, Lleap, ymc[day.Lmc], rmc[day.Ldi]))

print("\n八字:")
print("="*110)    
print("{:30s}{:30s}{:30s}{:30s}".format('年', "月", "日", "时"))
print("-"*110)
print("{:>11s}-{:<11s}{:>11s}-{:<11s}{:>11s}-{:<11s}{:>11s}-{:<11s}".format(
    gans.year, gan5[gans.year], gans.month, gan5[gans.month],
    gans.day, gan5[gans.day], gans.time, gan5[gans.time],
))
print("{:^24s}{:^24s}{:^24s}{:^24s}".format(*zhis))
for item in zhis:
    out = item + '='
    for gan in zhi5[item]:
        out = out + "{}{}{} ".format(gan, gan5[gan], zhi5[item][gan]) + ""
    print("{:<22s}".format(out), end=' ')

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

flag = True
for item in zhi_zixings:
    if zhis.count(item) > 1:
        if flag:
            print("\n{}:".format("地支自刑"))
            print("=========================")    
            flag = False
        print(item)    
        

# 计算五行分数

scores = {"金":0, "木":0, "水":0, "火":0, "土":0}

for item in gans:  
    scores[gan5[item]] += 5
    
for item in list(zhis) + [zhis.month]:  
    for gan in zhi5[item]:
        scores[gan5[gan]] += zhi5[item][gan]

print("\n\n五行分数") 
print("="*60)  
print(scores)
print("身体需要注意：{}".format(gan_health[min(scores, key=scores.get)]))







