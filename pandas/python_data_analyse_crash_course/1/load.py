#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-12
# load.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 
print(df.head())
print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())