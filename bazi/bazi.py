#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import  sxtwl
import argparse
import collections
from bidict import bidict


Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
ten_deities = {
    '甲':bidict({'甲':'比肩', "乙":'劫财', "丙":'食神', "丁":'伤官', "戊":'偏财',
           "己":'正财', "庚":'偏官', "辛":'正官', "壬":'偏印', 
           "癸":'印|印绶'}),
    '乙':bidict({'甲':'劫财', "乙":'比肩', "丙":'伤官', "丁":'食神', "戊":'正财',
           "己":'偏财', "庚":'正官', "辛":'偏官', "壬":'印',
           "癸":'偏印'}),   
    '丙':bidict({'丙':'比肩', "丁":'劫财', "戊":'食神', "己":'伤官', "庚":'偏财',
                  "辛":'正财', "壬":'偏官', "癸":'正官', "甲":'偏印', 
                  "乙":'印'}),
    '丁':bidict({'丙':'劫财', "丁":'比肩', "戊":'伤官', "己":'食神', "庚":'正财',
                  "辛":'偏财', "壬":'正官', "癸":'偏官', "甲":'印',
           "乙":'偏印'}),   
    '戊':bidict({'戊':'比肩', "己":'劫财', "庚":'食神', "辛":'伤官', "壬":'偏财',
                  "癸":'正财', "甲":'偏官', "乙":'正官', "丙":'偏印', 
                  "丁":'印'}),
    '己':bidict({'戊':'劫财', "己":'比肩', "庚":'伤官', "辛":'食神', "壬":'正财',
                  "癸":'偏财', "甲":'正官', "乙":'偏官', "丙":'印',
                  "丁":'偏印'}),      
    '庚':bidict({'庚':'比肩', "辛":'劫财', "壬":'食神', "癸":'伤官', "甲":'偏财',
                  "乙":'正财', "丙":'偏官', "丁":'正官', "戊":'偏印', 
                  "己":'印'}),
    '辛':bidict({'庚':'劫财', "辛":'比肩', "壬":'伤官', "癸":'食神', "甲":'正财',
                  "乙":'偏财', "丙":'正官', "丁":'偏官', "戊":'印',
                  "己":'偏印'}),   
    '壬':bidict({'壬':'比肩', "癸":'劫财', "甲":'食神', "乙":'伤官', "丙":'偏财',
                  "丁":'正财', "戊":'偏官', "己":'正官', "庚":'偏印', 
                  "辛":'印'}),
    '癸':bidict({'壬':'劫财', "癸":'比肩', "甲":'伤官', "乙":'食神', "丙":'正财',
                  "丁":'偏财', "戊":'正官', "己":'偏官', "庚":'印',
                  "辛":'偏印'}),         
    
}
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
zhi5 = {"子":{"壬":56,"癸":184}, 
    "丑":{"辛":40,"癸":56, "己":144}, 
    "寅":{"戊":40,"丙":40, "甲":160},
    "卯":{"甲":56, "乙":184}, 
    "辰":{"癸":40,"乙":56, "戊":144}, 
    "巳":{"庚":40,"戊":56, "丙":144}, 
    "午":{"丙":56, "丁":184},
    "未":{"甲":40,"丁":56, "己":144}, 
    "申":{"戊":40,"壬":40, "庚":160},
    "酉":{ "庚":56, "辛":184}, 
    "戌":{"丙":40,"辛":56, "戊":144}, 
    "亥":{"戊":40,"甲":40, "壬":160}}

#zhi5 = {"子":{"癸":8}, 
        #"丑":{"辛":1,"癸":2, "己":5}, 
        #"寅":{"戊":1,"丙":2, "甲":5},
        #"卯":{"乙":8}, 
        #"辰":{"癸":1,"乙":2, "戊":5}, 
        #"巳":{"庚":1,"戊":2, "丙":5}, 
        #"午":{"己":3, "丁":5},
        #"未":{"乙":1,"丁":2, "己":5}, 
        #"申":{"戊":1,"壬":2, "庚":5},
        #"酉":{"辛":8}, 
        #"戌":{"丁":1,"辛":2, "戊":5}, 
        #"亥":{"甲":3, "壬":5}}

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
me = gans.day

print("\n日期:")
print("======================================")  
print("公历:")
print("\t{}年{}月{}日".format(day.y, day.m, day.d))

Lleap = "闰" if day.Lleap else ""
print("农历:")
print("\t{}年{}{}月{}日".format(day.Lyear0 + 1984, Lleap, ymc[day.Lmc], rmc[day.Ldi]))

print("\n八字:   同义词：七杀|偏官 偏印|枭神")
print("="*150)    
print("{:<30s}{:<30s}{:<30s}{:<30s}".format('年【父-根】', "月【兄弟僚友-苗】", "日【自己配偶-花】", "时【子孙-实】"))
print("-"*150)
print("{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}".format(
    gans.year, '{} [{}]'.format(gan5[gans.year], ten_deities[me][gans.year]),
    gans.month, '{} [{}]'.format(gan5[gans.month], ten_deities[me][gans.month]),
    gans.day, '{} [{}]'.format(gan5[gans.month], '自己'), 
    gans.time, '{} [{}]'.format(gan5[gans.time], ten_deities[me][gans.time]),
))
print("{:^32s}{:^32s}{:^32s}{:^32s}".format(*zhis))
for item in zhis:
    out = item + '='
    for gan in zhi5[item]:
        out = out + "{}{}{} ".format(gan, gan5[gan], zhi5[item][gan]) + ""
    print("{:<30s}".format(out), end=' ')

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
print("身体需要注意：{}".format(gan_health[min(scores, key=scores.get)]))







