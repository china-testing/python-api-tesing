#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting QQ群:630011153
# CreateDate: 2018-3-9
# read_csv.py

import pandas as pd

df = pd.read_csv("1.csv", header=None) # 不读取列名
print("df:")
print(df)

print("df.head():")
print(df.head()) # head(self, n=5)，默认为5行，类似的有tail
print("df.tail():")
print(df.tail())

df = pd.read_csv("1.csv") # 默认读取列名
print("df:")
print(df)

df = pd.read_csv("1.csv", names=['号码','群号']) # 自定义列名
print("df:")
print(df)

# 自定义列名，去掉第一行
df = pd.read_csv("1.csv", skiprows=[0], names=['号码','群号'])
print("df:")
print(df)



