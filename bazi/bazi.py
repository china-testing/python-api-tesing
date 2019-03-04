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

def yinyang(item):
    if item in Gan:
        return '+' if Gan.index(item)%2 == 0 else '-'
    else:
        return '+' if Zhi.index(item)%2 == 0 else '-'

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
parser.add_argument('-n', action="store_true", default=False, help=u'是否为女，默认为男')
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

print("\n八字:   同义词：七杀|偏官 偏印|枭神 解读：钉钉或微信pythontesting")
print("="*140)    
print("{:^28s}{:^28s}{:^28s}{:^28s}".format('年【父-根】', "月【兄弟僚友-苗】", "日【自己配偶-花】", "时【子孙-实】"))
print("-"*140)
print("{:^30s}{:^30s}{:^30s}{:^30s}".format(
    '{}{}{} [{}]'.format(
         gans.year, yinyang(gans.year), gan5[gans.year], ten_deities[me][gans.year]),
    '{}{}{} [{}]'.format(
        gans.month, yinyang(gans.month), gan5[gans.month], ten_deities[me][gans.month]),
    '{}{}{} [{}]'.format(me, yinyang(me),gan5[me], '自己'), 
    '{}{}{} [{}]'.format(gans.time, yinyang(gans.time), gan5[gans.time], ten_deities[me][gans.time]),
))
print("{:^30s}{:^30s}{:^30s}{:^30s}".format(
    "{}{}{} [{}]".format(zhis.year, yinyang(zhis.year), 
        ten_deities[me][zhis.year], ten_deities[gans.year][zhis.year]),
    "{}{}{} [{}]".format(zhis.month, yinyang(zhis.month), 
        ten_deities[me][zhis.month], ten_deities[gans.month][zhis.month]),  
    "{}{}{}".format(zhis.day, yinyang(zhis.day), ten_deities[me][zhis.day]),   
    "{}{}{} [{}]".format(zhis.time, yinyang(zhis.time), 
        ten_deities[me][zhis.time], ten_deities[gans.time][zhis.time]),       
))
for item in zhis:
    out = ''
    for gan in zhi5[item]:
        out = out + "{}{}{}{} ".format(gan, gan5[gan], zhi5[item][gan],  ten_deities[me][gan])
    print("{:^26s}".format(out), end=' ')

print("\n\n")
print("="*140)  
print("你属:", me, "特点：--", gan_desc[me],"\n")
print("年份:", zhis[0], "特点：--", zhi_desc[zhis[0]],"\n")
#print(dict(ten_deities[me]))
#print(ten_deities[me])

# 子女分析
print("\n\n子女状态:", end='')
children = ['食','伤'] if options.n else ['官','杀'] 
for item in children:
	gan = ten_deities[me].inverse[item]
	print(item, ": ", gan, "--", ten_deities[gan][zhis[0]], 
	      ten_deities[gan][zhis[1]], ten_deities[gan][zhis[2]], " [",
	      ten_deities[gan][zhis[3]], ']\t\t',  end='')


# 对象状态
print("\n\n对象状态:", end='')
peer = ['官','杀'] if options.n else ['财','偏财'] 
for item in peer:
	gan = ten_deities[me].inverse[item]
	print(item, ": ", gan, "--", ten_deities[gan][zhis[0]], " [",
	          ten_deities[gan][zhis[1]], "]", ten_deities[gan][zhis[2]], 
	          ten_deities[gan][zhis[3]], '\t\t',  end='')	
	
	
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



# 羊刃分析
key = '帝旺' if Gan.index(me)%2 == 0 else '冠带'

if ten_deities[me].inverse[key] in zhis:
    print("\n羊刃:", me, ten_deities[me].inverse[key])  
    print("=========================")   
    print("羊刃重重又见禄，富贵饶金玉。 官、印相助福相资。")  
    print("专羊刃，主眼露性急，凶暴害物，亲近恶党，生旺稍可，死绝尤甚")
    print("在五行败者逢之，多患瘰疠或瘴疠、金刃之灾，不论贵贱，多冗杂劳迫，少得安逸") 
    print("六甲生人逢乙卯、丁卯，为真羊刃。若重犯，主残疾，官禄失退则散在晚年")
    print("运行羊刃，财物耗散")    
    print("\n有刃头财，如甲人见己卯之类，谓之销 煞 主财帛歇灭，常人以屠沽刀锯等事为业，或因被盗而致命者。")
    print("有刃头鬼，如甲人见辛卯之类，谓之持刃煞，主人不令终，虽入贵格，亦不可测。甲乙人见之，尤紧。多脑疽发背而终。")
    print("有羊刃相蚀，如甲寅虎、兔、甲戊狗兔之类()，见所蚀年月稍可，日时至危。若见两重，更值空亡，设非相蚀，亦犯流配至老，主不善终?")
    print("有揽辔澄清格，谓贵人乘马而前视羊刃，犹马头带剑之义。")    
    print("=========================")      


# 将星分析
me_zhi = zhis[2]
other_zhis = zhis[:2] + zhis[3:]
flag = False
if me_zhi in ("申", "子", "辰"):
    if "子" in other_zhis:
        flag = True
elif me_zhi in ("丑", "巳", "酉"):
    if "酉" in other_zhis:
        flag = True   
elif me_zhi in ("寅", "午", "戌"):
    if "午" in other_zhis:
        flag = True     
elif me_zhi in ("亥", "卯", "未"):
    if "卯" in other_zhis:
        flag = True   
        
if flag:
    print("\n\n将星: 常欲吉星相扶，贵煞加临乃为吉庆。")  
    print("=========================")   
    print('''理愚歌》云：将星若用亡神临，为国栋梁臣。言吉助之为贵，更夹贵库墓纯粹而
    不杂者，出将入相之格也，带华盖、正印而不夹库，两府之格也；只带库墓而带正印，员郎
    以上，既不带墓又不带正印，止有华盖，常调之禄也；带华印而正建驿马，名曰节印，主旌节
    之贵；若岁干库同库为两重福，主大贵。''')
    
# 华盖分析
flag = False
if me_zhi in ("申", "子", "辰"):
    if "辰" in other_zhis:
        flag = True
elif me_zhi in ("丑", "巳", "酉"):
    if "丑" in other_zhis:
        flag = True   
elif me_zhi in ("寅", "午", "戌"):
    if "戌" in other_zhis:
        flag = True     
elif me_zhi in ("亥", "卯", "未"):
    if "未" in other_zhis:
        flag = True   
        
if flag:
    print("\n\n华盖: 多主孤寡，总贵亦不免孤独，作僧道艺术论。")  
    print("=========================")   
    print('''《理愚歌》云：华盖虽吉亦有妨，或为孽子或孤孀。填房入赘多阙口，炉钳顶笠拔缁黄。
    又云：华盖星辰兄弟寡，天上孤高之宿也；生来若在时与胎，便是过房庶出者。''')    


# 咸池 桃花
flag = False
year_zhi = zhis[0]
if me_zhi in ("申", "子", "辰") or year_zhi in ("申", "子", "辰"):
    if "酉" in zhis:
        flag = True
elif me_zhi in ("丑", "巳", "酉") or year_zhi in ("丑", "巳", "酉"):
    if "午" in other_zhis:
        flag = True   
elif me_zhi in ("寅", "午", "戌") or year_zhi in ("寅", "午", "戌"):
    if "卯" in other_zhis:
        flag = True     
elif me_zhi in ("亥", "卯", "未") or year_zhi in ("亥", "卯", "未"):
    if "子" in other_zhis:
        flag = True   
        
if flag:
    print("\n\n咸池(桃花): 墙里桃花，煞在年月；墙外桃花，煞在日时；")  
    print("=========================")   
    print('''一名败神，一名桃花煞，其神之奸邪淫鄙，如生旺则美容仪，耽酒色，疏财好欢，
    破散家业，唯务贪淫；如死绝，落魄不检，言行狡诈，游荡赌博，忘恩失信，私滥奸淫，
    靡所不为；与元辰并，更临生旺者，多得匪人为妻；与贵人建禄并，多因油盐酒货得生，
    或因妇人暗昧之财起家，平生有水厄、痨瘵之疾，累遭遗失暗昧之灾。此人入命，有破无成，
    非为吉兆，妇人尤忌之。
    咸池非吉煞，日时与水命遇之尤凶。''')    

# 官分析
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
    l = list(zhis)
    if gui in l:
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
    scores[gan5[item]] += 5

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
