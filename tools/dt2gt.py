#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os
import argparse

import pandas as pd

import data_common

description = '''
转换测试结果为dt和gt。

输入：

1，android：安卓手机的测试结果。
2，server：服务器端比对程序的输出。这种输入本身就是dt。

输出：
    程序的当前目录输出如下：
    a, gt.txt
    b, dt.txt
    c, files.txt 文件列表

gt为检测绘制roc的标准结果。dt为检测结果。

gt的来源：

1，采集组标注的json文件。
2，把服务器端的比对结果转成gt，本程序实现该功能。适用场景为将服务端版本1作为标准结果，
服务器端的版本2或手机端的测试结果作为dt.
3,把手机端的比对结果转成gt，本程序实现该功能。适用场景为将手机端版本1作为标准结果，
手机端版本2的测试结果作为dt.

dt的来源：
1，服务器端的比对结果。
2，手机端测试结果

实例：

python3 dt2gt.py android /home/andrew/code/gongrui/detect/20180619/tracksample-v4.7.4.2-ppl.xls

'''

parser = argparse.ArgumentParser(description=description,
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('type_name', action="store", help=u'android或者server')
parser.add_argument('filename', action="store", help=u'测试结果文件')
parser.add_argument('--version', action='version',
    version='%(prog)s 1.0 Rongzhong xu 2018 06 15')
options = parser.parse_args()

i = 1
file_list = []
results = []
detection_results = []

if options.type_name == 'server':
    df = pd.read_table(options.filename, sep='\s', 
        names=['name','left', 'top', 'width', 'height', 'sep', 'value'])
    rename = lambda x: os.path.basename(x)
    df['name'] = df['name'].apply(rename) 
    for num in range(len(df)):
        row = df.loc[num]
        out = "# {}\n{}\n3 640 480 1\n0\n1\n".format(i, row['name'])
        out = out + "1 {} {} {} {}\n".format(row['left'], row['top'], row['left'] 
            + row['width'], row['top'] + row['height'])
        i = i + 1
        #print(out)
        file_list.append(row['name'])
        results.append(out.rstrip('\n'))
        
if options.type_name == 'android':
    print('In android')
    df = pd.read_excel(options.filename, usecols=[0,4],names=['name','result'])
    rename = lambda x: os.path.basename(x)
    df['name'] = df['name'].apply(rename) 
    print(df.head())
    for num in range(len(df)):
        row =  df.iloc[num]
        result = row['result']
        if result != '未检测到人脸':
            temps = result.split('[')
            left, top,  = temps[1].strip(']').split(',')
            right, bottom = temps[2].strip(']').split(',')     
            out = "# {}\n{}\n3 640 480 1\n0\n1\n".format(i, row['name'])
            out = out + "1 {} {} {} {}\n".format(left, top, right, bottom)
            detection_result = "{0} {1} {2} {3} {4} 1 {5}".format(
                        row['name'],left, top, int(right) - int(left), 
                        int(bottom) - int(top), 0.99)            
            i = i + 1
            #print(out)
            file_list.append(row['name'])
            results.append(out.rstrip('\n'))  
            detection_results.append(detection_result)
    
data_common.output_file("files.txt",file_list)
data_common.output_file("gt.txt",results)
data_common.output_file("dt.txt",detection_results)


