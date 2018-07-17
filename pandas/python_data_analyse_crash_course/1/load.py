#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# load.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

print("\n\n查看前五行")
print(df.head())

print("\n\n查看类型")
print(type(df))

print("\n\n查看大小")
print(df.shape)

print("\n\n查看列名")
print(df.columns)

print("\n\n查看dtypes(基于列)")
print(df.dtypes)

print("\n\n查看统计信息")
print(df.info())