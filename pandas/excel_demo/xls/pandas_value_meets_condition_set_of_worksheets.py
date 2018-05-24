#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_value_meets_condition_set_of_worksheets.py

import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output.xls"

my_sheets = [0,1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheetname=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
	row_list.append(data[data['Sale Amount'].replace('$', '').
	                     replace(',', '').astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()
