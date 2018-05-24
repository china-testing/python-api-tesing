#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-7
# far_frr.py
import glob
import os

import pandas
import pyexcel

from data_common import concat_excel,file2dict

base_file = r'D:\tmp\0302\睁闭眼rgb标准测试集_v1.0_3.txt'
version1 = r'D:\tmp\0302\v2-5-0\result'
version2 = r'D:\tmp\0302\v2-6-0\result'
datas = {'output':[
    ("Version",	"Eye state v2.5.0", "Eye state v2.5.0",	
     "Eye state v2.6.0","Eye state v2.6.0"),
    ("Threshold", "FAR", "FRR","FAR", "FRR"),]}
output_ = r"D:\output.xls"

base_results = file2dict(base_file, multi=True)
print(base_results)

values = (8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0,
          9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, )

all_files1 = glob.glob("{}{}*.xls".format(version1,os.sep))
df = concat_excel(
    all_files1, usecols=[0,6,7], strips={'识别图片的路径':'/sdcard/ocular/'})
all_files2 = glob.glob("{}{}*.xls".format(version2,os.sep))
df_ = concat_excel(
    all_files2, usecols=[0,6,7], strips={'识别图片的路径':'/sdcard/oculartest/'})

values1 = []
for value in values:
    df1 = df.loc[((df['左眼分数'] >= value) | (df['右眼分数'] >=  value)) 
                 & df['识别图片的路径'].isin(base_results['0']) , :]
    df2 = df.loc[((df['左眼分数'] < value) & (df['右眼分数'] <  value))
                 & df['识别图片的路径'].isin(base_results['1']) , :]
    df3 = df_.loc[((df_['左眼分数'] >= value) | (df_['右眼分数'] >=  value))
                 & df_['识别图片的路径'].isin(base_results['0']) , :]   
    df4 = df_.loc[((df_['左眼分数'] < value) & (df_['右眼分数'] <  value)) 
                 & df_['识别图片的路径'].isin(base_results['1']) , :]  
    datas['output'].append((
        value, len(df1)/109.0, len(df2)/179.0, len(df3)/109.0, len(df4)/179.0),)      
    
pyexcel.save_book_as(bookdict=datas, dest_file_name=output_)     

