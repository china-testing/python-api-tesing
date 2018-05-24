#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq group:630011153
# CreateDate: 2018-3-31
# change.py

import pandas as pd
import numpy as np
import random

scientists = pd.read_csv('../data/scientists.csv')
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)
print(scientists.head())

# 转为日期 参考：https://docs.python.org/3.5/library/datetime.html
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
# 增加列
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.shape)
print(scientists.head())

random.seed(42)
random.shuffle(scientists['Age']) # 此修改会作用于scientists
print(scientists.head())

scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists.head())