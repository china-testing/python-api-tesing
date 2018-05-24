#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# col.py

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

