#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# series.py

import pandas as pd
import numpy as np

scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age'])
print(scientists)

print("\n\n从数据帧(DataFrame)获取的行或者列为Series：")
first_row = scientists.loc['William Gosset']
print(type(first_row))
print(first_row)

print("\n\nindex和keys是一样的：")
print(first_row.index)
print(first_row.keys())

print("\n\nSeries取值：")
print(first_row.values)
print(first_row.index[0])
print(first_row.keys()[0])

print("\n\nPandas.Series和numpy.ndarray很类似：")
ages = scientists['Age']
print(ages)

# 统计，更多参考http://pandas.pydata.org/pandas-docs/stable/basics.html#descriptive-statistics
print("\n\n统计：平均值、最小值、最大值、方差")
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())

scientists = pd.read_csv('../data/scientists.csv')
ages = scientists['Age']
print(ages)
print(ages.mean())
print(ages.describe())
print(ages[ages > ages.mean()])
print(ages > ages.mean())
manual_bool_values = [True, True, False, False, True, True, False, False]
print(ages[manual_bool_values])

print(ages + ages)
print(ages * ages)
print(ages + 100)
print(ages * 2)
print(ages + pd.Series([1, 100]))
# print(ages + np.array([1, 100])) 会报错，不同类型相加，大小一定要一样
print(ages + np.array([1, 100, 1, 100, 1, 100, 1, 100]))

print("\n\n排序： 默认有自动排序")
print(ages)
print("\n\n排序： ages.sort_index(ascending=False) 降序")
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)
print(ages * 2)
print(ages + rev_ages)