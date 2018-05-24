#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-7
# excel_summary_demo.py
import pandas

from data_common import merge_excel

file1= r"2.12.0.xlsx"
file2= r"2.13.0.xlsx"
output = r"output.xls"

df1 = pandas.read_excel(file1,sheet_name='paper')
df2 = pandas.read_excel(file2,sheet_name='paper')
df2 = df2.rename(index=int, columns={"汇总图片": "汇总","用例编号":"编号"})

columns = ["type","测试用例","汇总",'2pd-v2.11','2pd-v2.12','2pd-v2.13',
               '2pd-v2.14','2pd-v2.15']
df3 = merge_excel(df1, df2, '测试用例',fixes=["type","编号"], sorts=["type","编号"],
                 columns=columns)


df4 = pandas.read_excel(file1,sheet_name='human')
df5 = pandas.read_excel(file2,sheet_name='human')
df5 = df5.rename(index=int, columns={"汇总图片": "图片总数"})

columns = ['用例编号',"测试用例","图片总数",'2pd-v2.11','2pd-v2.12','2pd-v2.13',
           '2pd-v2.14','2pd-v2.15']
df6 = merge_excel(df4, df5, '用例编号',fixes=["用例编号","测试用例"], sorts=["用例编号"],
                 columns=columns)

writer = pandas.ExcelWriter(output)
df3.to_excel(writer, sheet_name='paper', index=False)
df6.to_excel(writer, sheet_name='human', index=False)
writer.save()



    