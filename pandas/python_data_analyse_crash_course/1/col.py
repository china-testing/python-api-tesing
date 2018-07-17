#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# col.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

# 列操作
country_df = df['country'] # 列名选取单列

print("\n\n列首5行")
print(country_df.head())

print("\n\n列尾5行")
print(country_df.tail())

country_df_dot = df.country # 点号的方式选取列
print("\n\n点号的方式选取列")
print(country_df_dot.head())

subset = df[['country', 'continent', 'year']] # 选取多列
print("\n\n选取多列")
print(subset.head())