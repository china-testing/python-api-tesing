#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# row.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

# 行操作，注意df.loc[-1]是非法的
print(df.loc[0])
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])
print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)
print(type(subset_loc))
print(type(subset_head))

print(df.loc[[0, 99, 999]])
print(type(df.loc[[0, 99, 999]]))

print(df.iloc[0])
print(df.iloc[[0, 99, 999]])
