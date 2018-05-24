#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq group:630011153
# CreateDate: 2018-3-13
# create.py

import pandas as pd

s = pd.Series(['banana', 42])
print(s)

s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# 注意：列名未必为执行的顺序，通常为按字母排序
scientists = pd.DataFrame({
    ' Name': ['Rosaline Franklin', 'William Gosset'],
    ' Occupation': ['Chemist', 'Statistician'],
    ' Born': ['1920-07-25', '1876-06-13'],
    ' Died': ['1958-04-16', '1937-10-16'],
    ' Age': [37, 61]})
print(scientists)

# 指定顺序
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age'])
print(scientists)