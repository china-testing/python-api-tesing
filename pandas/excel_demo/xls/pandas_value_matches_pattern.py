#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_value_matches_pattern.py

import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output.xls"

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_matches_pattern = data_frame[
    data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(
    writer, sheet_name='jan_13_output', index=False)
writer.save()