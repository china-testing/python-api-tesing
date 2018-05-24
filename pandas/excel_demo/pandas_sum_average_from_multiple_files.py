#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_sum_average_from_multiple_files.py
import pandas as pd
import glob
import os

input_path = r"D:\code\foundations-for-analytics-with-python\csv"
output_file = r"output_files\12output.csv"

all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frames = []
for input_file in all_files:
    print(input_file)
    data_frame = pd.read_csv(input_file, index_col=None)
    
    print(data_frame)
    
    sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) 
      for value in data_frame.loc[:, 'Sale Amount']])
    
    total_cost = sales.sum()
    average_cost = sales.mean()

    data = {'file_name': os.path.basename(input_file),
            'total_sales': total_cost,
            'average_sales': average_cost}

    all_data_frames.append(pd.DataFrame(
        data, columns=['file_name', 'total_sales', 'average_sales']))

data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frames_concat.to_csv(output_file, index = False)