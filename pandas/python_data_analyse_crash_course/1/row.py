#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# row.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

# 行操作，注意df.loc[-1]是非法的
print("\n\n第一行")
print(df.loc[0])

print("\n\n行数")
number_of_rows = df.shape[0]
print(number_of_rows)

last_row_index = number_of_rows - 1
print("\n\n最后一行")
print(df.loc[last_row_index])

print("\n\ntail的方法输出最后一行")
print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)
print("\n\nloc的类型为序列Series")
print(type(subset_loc))

print("\n\nhead的类型为数据帧DataFrame")
print(type(subset_head))

print("\n\nloc选取三列，类型为数据帧DataFrame")
print(df.loc[[0, 99, 999]])
print(type(df.loc[[0, 99, 999]]))

print("\n\niloc选取第一行")
print(df.iloc[0])

print("\n\niloc选取三行")
print(df.iloc[[0, 99, 999]])
