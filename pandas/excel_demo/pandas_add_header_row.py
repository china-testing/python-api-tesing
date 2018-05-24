#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_add_header_row.py
import pandas as pd

input_file = r"supplier_data_no_header_row.csv"
output_file = r"11output.csv"
header_list = ['Supplier Name', 'Invoice Number', \
'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
print(data_frame)
data_frame.to_csv(output_file, index=False)