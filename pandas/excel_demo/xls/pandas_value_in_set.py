#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_value_in_set.py

import pandas as pd
import string
import sys

input_file = "sales_2013.xlsx"
output_file = "pandas_output.xls"

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]

writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()