#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import pandas as pd

df = pd.read_csv("/opt/test_tools/base/faceunlock_test_general_meil/result/gaze2.2.0.csv",names=['score','filename'],sep='\s')

df1 = df.loc[(df['score'] < 0.5) & df['filename'].str.contains('/gaze/')]
df2 = df.loc[(df['score'] > 0.5) & df['filename'].str.contains('/no_gaze/')]

writer = pd.ExcelWriter("gaze_error.xls")
df1.to_excel(writer, sheet_name='注视识别为非注视', index=False)
df2.to_excel(writer, sheet_name='非注视识别为注视', index=False)
writer.save()
