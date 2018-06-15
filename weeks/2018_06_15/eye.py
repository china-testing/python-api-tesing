#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-012
import pandas as pd

import servers

filename = "data.csv"
servers.get_eye_server_result(filename)

#df = pd.read_csv(filename, sep=' |,', engine='python',names=['left_score','left_valid','right_score','right_valid','name'])
#print(df.head())

#df_unknow = df[df['left_score'] == -1]
#print(df_unknow.head())


#df_error = df[df['left_score'] == -2]
#print(df_error.head())

#df2 = df[df['left_score'] > -1]

#close_error = df2[df2['name'].str.contains('/close/') & ((df2['left_score'] > 9.5) | (df2['right_score'] > 9.5))]
#print(close_error.head())

#open_error = df2[df2['name'].str.contains('/open/') & (df2['left_score'] < 9.5) & (df2['right_score'] < 9.5)]
#print(open_error.head())

#invalid_error = df2[df2['name'].str.contains('/invalid/') & ((df2['left_valid'] > 9.5) | (df2['right_valid'] > 9.5))]
#print(invalid_error.head())

#valid_error = df2[df2['name'].str.contains('/valid/') & (df2['left_valid'] < 9.5) & (df2['right_valid'] < 9.5)]
#print(valid_error.head())
## 中文
#writer = pd.ExcelWriter("output.xlsx")
#df_unknow.to_excel(writer, sheet_name='未认识人脸', index=False)
#df_error.to_excel(writer, sheet_name='图片格式错误', index=False)
#close_error.to_excel(writer, sheet_name='闭眼识别为睁眼', index=False)
#open_error.to_excel(writer, sheet_name='睁眼识别为闭眼', index=False)
#invalid_error.to_excel(writer, sheet_name='无效识别为有效', index=False)
#valid_error.to_excel(writer, sheet_name='有效识别为无效', index=False)
#writer.save()