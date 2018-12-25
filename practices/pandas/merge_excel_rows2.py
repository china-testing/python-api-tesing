#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/merge_excel_rows2.html
# https://github.com/china-testing/python-api-tesing/blob/master/practices/pandas/merge_excel_rows2.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-12-06
import pandas as pd

df = pd.read_csv("test2.csv", engine='c', header=None)
arr = df.values.copy()
arr.resize(20, 5)
df2 = pd.DataFrame(arr)
df2.to_csv("out2.csv", index=None, header=None)




