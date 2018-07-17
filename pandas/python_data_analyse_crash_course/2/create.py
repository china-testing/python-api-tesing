#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# create.py

import pandas as pd

print("\n\n创建序列Series")
s = pd.Series(['banana', 42])
print(s)

print("\n\n指定索引index创建序列Series")
s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# 注意：列名未必为执行的顺序，通常为按字母排序
print("\n\n创建数据帧DataFrame")
scientists = pd.DataFrame({
    ' Name': ['Rosaline Franklin', 'William Gosset'],
    ' Occupation': ['Chemist', 'Statistician'],
    ' Born': ['1920-07-25', '1876-06-13'],
    ' Died': ['1958-04-16', '1937-10-16'],
    ' Age': [37, 61]})
print(scientists)

print("\n\n指定顺序(index和columns)创建数据帧DataFrame")
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age'])
print(scientists)