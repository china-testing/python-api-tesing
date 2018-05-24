#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# group.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

print(df.loc[42, 'country'])
print(df.iloc[42, 0])
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])