#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_column_by_name_all_worksheets.py

import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output.xls"

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
	column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(
        writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()