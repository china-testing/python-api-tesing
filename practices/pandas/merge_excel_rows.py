#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持 https://china-testing.github.io/merge_excel_rows.html
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-12-06
import pandas as pd

frame = pd.read_csv("test.csv", engine='c')
df =  frame.groupby(['state', 'year']).sum()
df.to_csv("out.csv")





