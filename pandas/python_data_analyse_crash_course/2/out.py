#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-3-31
# out.py

import pandas as pd
import numpy as np
import random

scientists = pd.read_csv('../data/scientists.csv')
names = scientists['Name']
print(names)
names.to_pickle('../output/scientists_names_series.pickle')
scientists.to_pickle('../output/scientists_df.pickle')

# .p, .pkl,  .pickle 是常用的pickle文件扩展名
scientist_names_from_pickle = pd.read_pickle('../output/scientists_df.pickle')
print(scientist_names_from_pickle)

names.to_csv('../output/scientist_names_series.csv')
scientists.to_csv('../output/scientists_df.tsv', sep='\t')
# 不输出行号
scientists.to_csv('../output/scientists_df_no_index.csv', index=None)

# Series可以转为df再输出成excel文件
names_df = names.to_frame()
names_df.to_excel('../output/scientists_names_series_df.xls')
names_df.to_excel('../output/scientists_names_series_df.xlsx')

scientists.to_excel('../output/scientists_df.xlsx', sheet_name='scientists',
                    index=False)