#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_select_contiguous_rows.py
import pandas as pd

input_file = r"supplier_data_unnecessary_header_footer.csv"
output_file = r"11output.csv"

data_frame = pd.read_csv(input_file, header=None)
data_frame = data_frame.drop([0,1,2,16,17,18])
print(data_frame)
data_frame.columns = data_frame.iloc[0]
print(data_frame)
data_frame = data_frame.reindex(data_frame.index.drop(3))
print(data_frame)
data_frame.to_csv(output_file, index=False)