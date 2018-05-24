#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_concat_data_from_multiple_workbooks.py

import pandas as pd
import glob
import os

input_path = "/media/andrew/6446FA2346F9F5A0/code/foundations-for-analytics-\
with-python/excel"
output_file = "pandas_output.xls"

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(
    writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()