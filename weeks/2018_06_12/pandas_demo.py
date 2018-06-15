#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-012

import pandas as pd


def test(x):
    if x['A'] in x['B']:
        return True
    else:
        return False

df = pd.DataFrame( {'A':['Ford', 'Toyota', 'Ford','Audi'], 
                    'B':['Ford F-Series pickup', 'Camry', 'Ford Taurus/Taurus X', 'Audi test']} )


print(df)
# 输出列B包含列A内容的记录
print(df[df.apply(test, axis=1)])

# lambda 方式
print(df[df.apply(lambda x: x['A'] in x['B'], axis=1)])

# 输出列A为Ford或Toyota的记录
print(df[df['A'].str.match('Ford|Toyota')])