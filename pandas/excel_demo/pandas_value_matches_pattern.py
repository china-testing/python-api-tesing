#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_value_matches_pattern.py

import pandas as pd

input_file = r"supplier_data.csv"
output_file = r"4output.csv"

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number']\
.str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)