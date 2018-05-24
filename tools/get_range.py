#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-1-8 
# check_md5.py
import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('filename', action="store", help='要处理的结果文件')
parser.add_argument('colomns', action="store", help='列名用逗号分隔')
parser.add_argument('colomn', action="store", help='要处理的列名')
parser.add_argument('low', action="store", help='低值',type=float)
parser.add_argument('high', action="store", help='高值',type=float)
parser.add_argument('-o', action="store", dest="output",
                    default="output.csv", help='输出文件名，默认为output.csv')  
parser.add_argument('-S', action="store", dest="sep",
                    default="\s", help=r'分隔符，默认为\s') 
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 04 19')
options = parser.parse_args()

#names = options.colomns.split(",")
df = pd.read_csv(options.filename, sep=options.sep)
print(df)

#df = df.loc[1:,:]
df1 = df.loc[(df[options.colomn].astype('float') < options.high) & (df[options.colomn].astype('float') > options.low)]

df1.to_csv(options.output, index=None)
