#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 钉钉或微信pythontesting 钉钉群21734177 技术支持qq群：630011153 144081101
# 鸣谢 https://github.com/yuangu/sxtwl_cpp/tree/master/python
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import  sxtwl
import argparse
import collections
import pprint
from bidict import bidict

from datas import *
from sizi import summarys

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


# 计算五行分数 http://www.131.com.tw/word/b3_2_14.htm

scores = {"金":0, "木":0, "水":0, "火":0, "土":0}
gan_scores = {"甲":0, "乙":0, "丙":0, "丁":0, "戊":0, "己":0, "庚":0, "辛":0,
              "壬":0, "癸":0}   

for item in gans:  
    scores[gan5[item]] += 5
    gan_scores[item] += 5


for item in list(zhis) + [zhis.month]:  
    for gan in zhi5[item]:
        scores[gan5[gan]] += zhi5[item][gan]
        gan_scores[gan] += zhi5[item][gan]
        

# 计算八字强弱


me_attrs_ = ten_deities[me].inverse
strong = gan_scores[me_attrs_['比肩']] + gan_scores[me_attrs_['劫']] \
    + gan_scores[me_attrs_['偏印']] + gan_scores[me_attrs_['印']]

if not options.b:
    print("\n日期:")
    print("======================================")  
    print("公历:", end='')
    print("\t{}年{}月{}日".format(day.y, day.m, day.d))

    Lleap = "闰" if day.Lleap else ""
    print("农历:", end='')
    print("\t{}年{}{}月{}日".format(day.Lyear0 + 1984, Lleap, ymc[day.Lmc], rmc[day.Ldi]))

print("\n八字:   同义词：七杀|偏官 偏印|枭神  流岁取天干 解读：钉钉或微信pythontesting 以下未包含拱合、三合")
print("="*140)    
print("{:^28s}{:^28s}{:^28s}{:^28s}".format('年【父-根】', "月【兄弟僚友-苗】", "日【自己配偶-花】", "时【子孙-实】"))
print("-"*140)
print("{:^30s}{:^30s}{:^30s}{:^30s}".format(
    '{}{}{}5 [{}]'.format(
        gans.year, yinyang(gans.year), gan5[gans.year], ten_deities[me][gans.year]),
    '{}{}{}5 [{}]'.format(
        gans.month, yinyang(gans.month), gan5[gans.month], ten_deities[me][gans.month]),
    '{}{}{}5 [{}]'.format(me, yinyang(me),gan5[me], '自己 天元'), 
    '{}{}{}5 [{}]'.format(gans.time, yinyang(gans.time), gan5[gans.time], ten_deities[me][gans.time]),
))

empty = empties[zhus[0]]
print("{:^30s}{:^30s}{:^30s}{:^30s}".format(
    "{}{}{} [{}]".format(zhis.year, yinyang(zhis.year), 
                         ten_deities[me][zhis.year], ten_deities[gans.year][zhis.year]),
    "{}{}{} [{}]【命】地元".format(zhis.month, yinyang(zhis.month), 
                         ten_deities[me][zhis.month], ten_deities[gans.month][zhis.month]),  
    "{}{}{} 地元".format(zhis.day, yinyang(zhis.day), ten_deities[me][zhis.day]),   
    "{}{}{} [{}]".format(zhis.time, yinyang(zhis.time), 
                         ten_deities[me][zhis.time], ten_deities[gans.time][zhis.time]),       
))


for seq, item in enumerate(zhis):
    out = ''
    multi = 2 if item == zhis.month and seq == 1 else 1
        
    for gan in zhi5[item]:
        out = out + "{}{}{}{} ".format(gan, gan5[gan], zhi5[item][gan]*multi,  
                                       ten_deities[me][gan])
    print("{:^26s}".format(out), end=' ')

print()
for seq, item in enumerate(zhis):
  
    output = ''
    others = zhis[:seq] + zhis[seq+1:] 
    for type_ in zhi_atts[item]:
        flag = False
        for zhi in zhi_atts[item][type_]:
            if zhi in others:
                if not flag:
                    output = output + " " + type_ + ":"
                    flag = True
                output += zhi
    print("{:^30s}".format(output), end=' ')         
        
print()
for item in zhus:
    print("{:^30s}".format(nayins[item]), end=' ')    

print()

for item in empty:
    if item in zhis:
        print("空亡", item)
        break
    
print("-"*140)    

print(kus)
for item in gan_scores:  
    print("{}[{}]-{} ".format(
        item, ten_deities[me][item], gan_scores[item]),  end='  ')    
print("\n")
print("五行分数", scores, '\t\t八字强弱：', strong, "通常大于29分为强，还需要参考月份、坐支等")
print(zhi_3hes)

# 出身分析
cai = ten_deities[me].inverse['财']
guan = ten_deities[me].inverse['官']
births = tuple(gans[:2])
if cai in births and guan in births:
    birth = '不错'
#elif cai in births or guan in births:
    #birth = '较好'
else:
    birth = '一般'
    
print("出身:", birth)    

gan_shens = []
for item in gans:
    gan_shens.append(ten_deities[me][item])
print(gan_shens)

zhi_shens = []
for item in zhis:
    d = zhi5[item]
    zhi_shens.append(ten_deities[me][max(d, key=d.get)])
print(zhi_shens)

if "伤" in gan_shens + zhi_shens:
    print("伤官: 合神(三合、六合、双鸳合等等)重，男子犯之，耽迷酒色；女人逢之，不媒自嫁。")

# 子女分析
boy = ten_deities[me].inverse['食'] if options.n else ten_deities[me].inverse['杀']
girl = ten_deities[me].inverse['伤'] if options.n else ten_deities[me].inverse['官']
children = ['食','伤'] if options.n else ['官','杀'] 
boy_state = "子：{} -- {} {} {} [{}]".format(
    boy, ten_deities[boy][zhis[0]], ten_deities[boy][zhis[1]], 
    ten_deities[boy][zhis[2]], ten_deities[boy][zhis[3]] )
girl_state = "女：{} -- {} {} {} [{}]".format(
    girl, ten_deities[girl][zhis[0]], ten_deities[girl][zhis[1]], 
    ten_deities[girl][zhis[2]], ten_deities[girl][zhis[3]] )


# 对象状态
mate = ten_deities[me].inverse['官'] if options.n else ten_deities[me].inverse['财']
lover = ten_deities[me].inverse['杀'] if options.n else ten_deities[me].inverse['偏财'] 
mate_state = "对象：{} -- {} [{}] {} {}".format(
    mate, ten_deities[mate][zhis[0]], ten_deities[mate][zhis[1]], 
    ten_deities[mate][zhis[2]], ten_deities[mate][zhis[3]] )
lover_state = "情人：{} -- {} [{}] {} {}".format(
    lover, ten_deities[lover][zhis[0]], ten_deities[lover][zhis[1]], 
    ten_deities[lover][zhis[2]], ten_deities[lover][zhis[3]] )
print("{:<25s}  {:<25s}  {:<25}  {:<25s}".format(
    boy_state, girl_state, mate_state, lover_state))

# 父母状态
father = ten_deities[me].inverse['偏财'] 
mother = ten_deities[me].inverse['印'] 
father_state = "父：{} -- {} [{}] {} {}".format(
    father, ten_deities[father][zhis[0]], ten_deities[father][zhis[1]], 
    ten_deities[father][zhis[2]], ten_deities[father][zhis[3]] )
mother_state = "母：{} -- {} [{}] {} {}".format(
    mother, ten_deities[mother][zhis[0]], ten_deities[mother][zhis[1]], 
    ten_deities[mother][zhis[2]], ten_deities[mother][zhis[3]] )

# 兄弟姐妹状态
brother = ten_deities[me].inverse['劫'] if options.n else ten_deities[me].inverse['比肩']
sister = ten_deities[me].inverse['比肩'] if options.n else ten_deities[me].inverse['劫'] 
brother_state = "兄弟：{} -- {} [{}] {} {}".format(
    brother, ten_deities[brother][zhis[0]], ten_deities[brother][zhis[1]], 
    ten_deities[brother][zhis[2]], ten_deities[brother][zhis[3]] )
sister_state = "姐妹：{} -- {} [{}] {} {}".format(
    sister, ten_deities[sister][zhis[0]], ten_deities[sister][zhis[1]], 
    ten_deities[sister][zhis[2]], ten_deities[sister][zhis[3]] )
print("{:<25s}  {:<25s}  {:<25}  {:<25s}".format(
    father_state, mother_state, brother_state, sister_state))

print("-"*140)    
sum_index = ''.join([me, '日', *zhus[3]])
if sum_index in summarys:
    print("\n\n命")    
    print("=========================")      
    print(summarys[sum_index])

gan_ = tuple(gans)
for item in Gan:
    if gan_.count(item) == 3:
        print("三字干：", item, "--", gan3[item])
        break
    
gan_ = tuple(gans)
for item in Gan:
    if gan_.count(item) == 4:
        print("四字干：", item, "--", gan4[item])
        break    
        
zhi_ = tuple(zhis)
for item in Zhi:
    if zhi_.count(item) > 2:
        print("三字支：", item, "--", zhi3[item])
        break

print("="*140)  
print("你属:", me, "特点：--", gan_desc[me],"\n")
print("年份:", zhis[0], "特点：--", zhi_desc[zhis[0]],"\n")

def check_subset(gans, db, desc):
    flag = False # 是否找到
    for item in db:
        if set(item).issubset(gans):
            if not flag:
                print("\n\n{}:".format(desc))
                print("="*60)   
                flag = True
            print(item, db[item])  
    return flag

check_subset(gans, gan_hes, '十干合 https://www.jianshu.com/p/3d770f21c677')
check_subset(gans, gan_chongs, '十干冲 https://www.jianshu.com/p/ac958d44835f')
check_subset(zhis, zhi_6hes, '地支六合: 男子忌合绝，女人忌合贵。')		
if not check_subset(zhis, zhi_3hes, '地支三合'):	 # 如果三合，没必要检查半合
    check_subset(zhis, zhi_half_3hes, '地支半合')	
check_subset(zhis, zhi_huis, '地支三会')	
check_subset(zhis, zhi_chongs, '地支相冲 https://www.jianshu.com/p/ac958d44835f')	
check_subset(zhis, zhi_poes, '地支相破(破煞): 少年灾滞，财产耗散，兼有折伤之灾。')	
check_subset(zhis, zhi_haies, '地支相害 六亲损害 再见羊刃、劫煞、官府，为灾尤甚。日时、女命尤忌')	
check_subset(zhis, zhi_xings, '地支相刑')



# 羊刃分析
key = '帝旺' if Gan.index(me)%2 == 0 else '冠带'

if ten_deities[me].inverse[key] in zhis:
    print("\n羊刃:", me, ten_deities[me].inverse[key])  
    print("======================参考：https://www.jianshu.com/p/c503f7b3ed04")  
    if ten_deities[me].inverse['冠带']:
        print("羊刃重重又见禄，富贵饶金玉。 官、印相助福相资。")  
    else:
        print("劳累命！")



# 三奇
flag = False
if ['乙','丙', '丁'] == list(gans[:3]) or ['乙','丙', '丁'] == list(gans[1:]):
    flag = True   
if ['甲','戊', '庚'] == list(gans[:3]) or ['甲','戊', '庚'] == list(gans[1:]):
    flag = True   
if ['辛','壬', '癸'] == list(zhis[:3]) or ['辛','壬', '癸'] == list(zhis[1:]):
    flag = True         


if flag:
    print("\n\n三奇：参见https://www.jianshu.com/p/d014a054c38e")     

# 将星分析
me_zhi = zhis[2]
other_zhis = zhis[:2] + zhis[3:]
flag = False
tmp_list = []
if me_zhi in ("申", "子", "辰"):
    if "子" in other_zhis:
        flag = True
        tmp_list.append((me_zhi, '子'))
elif me_zhi in ("丑", "巳", "酉"):
    if "酉" in other_zhis:
        flag = True   
        tmp_list.append((me_zhi, '酉'))
elif me_zhi in ("寅", "午", "戌"):
    if "午" in other_zhis:
        flag = True     
        tmp_list.append((me_zhi, '午'))
elif me_zhi in ("亥", "卯", "未"):
    if "卯" in other_zhis:
        flag = True   
        tmp_list.append((me_zhi, '卯'))

if flag:
    print("\n\n将星: 常欲吉星相扶，贵煞加临乃为吉庆。")  
    print("=========================")   
    print('''理愚歌》云：将星若用亡神临，为国栋梁臣。言吉助之为贵，更夹贵库墓纯粹而
    不杂者，出将入相之格也，带华盖、正印而不夹库，两府之格也；只带库墓而带正印，员郎
    以上，既不带墓又不带正印，止有华盖，常调之禄也；带华印而正建驿马，名曰节印，主旌节
    之贵；若岁干库同库为两重福，主大贵。''')
    print(tmp_list)

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
taohuas = []
year_zhi = zhis[0]
if me_zhi in ("申", "子", "辰") or year_zhi in ("申", "子", "辰"):
    if "酉" in zhis:
        flag = True
        taohuas.append("酉")
elif me_zhi in ("丑", "巳", "酉") or year_zhi in ("丑", "巳", "酉"):
    if "午" in other_zhis:
        flag = True   
        taohuas.append("午")
elif me_zhi in ("寅", "午", "戌") or year_zhi in ("寅", "午", "戌"):
    if "卯" in other_zhis:
        flag = True    
        taohuas.append("卯")
elif me_zhi in ("亥", "卯", "未") or year_zhi in ("亥", "卯", "未"):
    if "子" in other_zhis:
        flag = True   
        taohuas.append("子")

if flag:
    print("\n\n咸池(桃花): 墙里桃花，煞在年月；墙外桃花，煞在日时；")  
    print("=========================")   
    print('''一名败神，一名桃花煞，其神之奸邪淫鄙，如生旺则美容仪，耽酒色，疏财好欢，
    破散家业，唯务贪淫；如死绝，落魄不检，言行狡诈，游荡赌博，忘恩失信，私滥奸淫，
    靡所不为；与元辰并，更临生旺者，多得匪人为妻；与贵人建禄并，多因油盐酒货得生，
    或因妇人暗昧之财起家，平生有水厄、痨瘵之疾，累遭遗失暗昧之灾。此人入命，有破无成，
    非为吉兆，妇人尤忌之。
    咸池非吉煞，日时与水命遇之尤凶。''')  
    print(taohuas, zhis)

# 禄分析
flag = False
for item in zhus:
    if item in lu_types[me]:
        if not flag:
            print("\n\n禄分析:")  
            print("=========================")	    
        print(item,lu_types[me][item])


# 文昌贵人
if wenchang[me] in zhis:
    print("\n\n文昌贵人: ")  
    print("=========================")	              
    print(me,  wenchang[me])

# 文星贵人
if wenxing[me] in zhis:
    print("\n\n文星贵人: ")  
    print("=========================")	              
    print(me,  wenxing[me])

# 天印贵人
if tianyin[me] in zhis:
    print("\n\n天印贵人: 此号天印贵，荣达受皇封")  
    print("=========================")	              
    print(me,  tianyin[me])



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
    if ten_deities[me].inverse['建'] in guan_list:
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
        if item in chongs.get(gui, []):
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

print(list(gans).count('癸'))

short = min(scores, key=scores.get)
print("\n\n五行缺{}的建议参见https://www.jianshu.com/p/0ed28f3a7f37".format(short))    

