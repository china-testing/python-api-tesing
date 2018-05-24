#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-22 pandas_value_meets_condition_all_worksheets.py

import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output.xls"

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].replace('$', '').
                           replace(',', '').astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
