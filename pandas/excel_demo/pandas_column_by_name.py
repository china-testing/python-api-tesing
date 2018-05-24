#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_column_by_index.py
import pandas as pd

input_file = r"supplier_data.csv"
output_file = r"output_files\7output.csv"

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[
    :, ['Invoice Number', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)