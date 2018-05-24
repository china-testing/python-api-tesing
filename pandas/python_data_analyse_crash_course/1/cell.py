#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# cell.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

# 列操作
country_df = df['country']
print(country_df.head())
print(country_df.tail())
country_df_dot = df.country
print(country_df_dot.head())
subset = df[['country', 'continent', 'year']]
print(subset.head())
subset = df[[1]]
print(subset.head())
subset = df[[0, -1]]
print(subset.head())
small_range = list(range(5))
subset = df[small_range]
print(subset.head())
small_range = list(range(3, 6))
subset = df[small_range]
print(subset.head())
small_range = list(range(0, 6, 2))
subset = df[small_range]
print(subset.head())
