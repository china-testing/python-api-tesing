#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq group:630011153
# CreateDate: 2018-3-31
# df.py

import pandas as pd
import numpy as np

scientists = pd.read_csv('../data/scientists.csv')
print(scientists[scientists['Age'] > scientists['Age'].mean()])
first_half = scientists[: 4]
second_half = scientists[ 4 :]
print(first_half)
print(second_half)
print(first_half + second_half)
print(scientists * 2)