#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-2-25
# count_unqualified_photo_num.py
'''
第一行的奇数格表示人名

1,2列为人员vivo1_15042124750 图片路径和分数，以此类推

要求统计出每个人的分数小于7的个数，如果为0，则不输出

统计通过率0-通过率9的sheet
'''

import pandas
import pyexcel

file1 = r"pass_ST_Verify_3.47.0_SNPE.model.xls"
output_ = r"output.xls"
value = 0.9
datas = {'output':[("人名","不合格数量")]}

data_frame = pandas.read_excel(
    file1, sheet_name=None,  header=None)

for worksheet_name, df1 in data_frame.items():
    if not '通过率' in str(worksheet_name):
        continue
    names = df1.loc[0].dropna()
    df1.loc[0] = df1.loc[0].fillna(method='ffill')
    df2 = df1.T
    df2.index = [df1.loc[0].fillna(method='ffill'), df1.loc[1]]
    
    for name in names:
        df3 = df2.loc[name].T.dropna()[2:]
        count = len(df3.loc[df3['score'].astype(float)<value])
        if count:
            print(name, count)
            datas['output'].append((name, count))
           
pyexcel.save_book_as(bookdict=datas, dest_file_name=output_)              







    