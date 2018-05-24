#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong@126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-30

'''
根据bug列表生成统计。
'''
    
import pathlib
import glob
import os

import pyexcel
import pandas

input_ = r"D:\sensetime\user\result"
output_ = r"D:\output.xls"
file_type = "xls"
value = 9.5

datas = {'output':[("BUG名","BUG图片总数","闭眼总数","未检测到人脸总数")]}
files = glob.glob("{}{}*.{}".format(input_, os.sep, file_type))

for file_name in files:
    df = pandas.read_excel(file_name)
    closes = len(df.loc[(df['左眼分数'] < value) & (df['右眼分数'] < value), :])
    empties = len(df.loc[(df['备注'].notnull()), :])
    print(file_name, len(df), closes, empties)
    datas['output'].append(
        (os.path.basename(file_name), len(df), closes, empties))    

pyexcel.save_book_as(bookdict=datas, dest_file_name=output_)     
    


