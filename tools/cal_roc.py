#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np
import argparse
from sklearn.metrics import roc_curve

import count

description = '''根据分数矩阵和label文件生成活体ROC.

示例：
1. 生成roc，采用默认区间：0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49

$ cal_roc.py  4.1.0-result.csv  labels.txt 
fpr    | 0.41 | 0.42 | 0.43 | 0.44 | 0.45 | 0.46 | 0.47 | 0.48 | 0.49
  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  
tpr(%) | 99.95 | 99.96 | 99.96 | 99.96 | 99.97 | 99.97 | 99.98 | 99.98 | 99.98
thres  | 0.724 | 0.681 | 0.640 | 0.599 | 0.565 | 0.534 | 0.500 | 0.471 | 0.440

2. 生成roc，采用默认区间：0.1 0.2 0.3 0.4 0.5

$ cal_roc.py  4.1.0-result.csv  labels.txt  -r '0.1 0.2 0.3 0.4 0.5'
fpr    | 0.10 | 0.20 | 0.30 | 0.40 | 0.50
  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  
tpr(%) | 77.51 | 99.62 | 99.88 | 99.95 | 99.98
thres  | 1.000 | 0.973 | 0.927 | 0.775 | 0.417

注意： 在172.20.15.200因为把脚本目录加入了PATH, 所以在任何目录执行该脚本。其他服务器未必
如此。

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('score', default='', type=str, help='生成的分数矩阵')
parser.add_argument('label', default='', type=str, help='label文件')
parser.add_argument('-r', '--roc', 
    default='0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49', 
    help='ROC初始值，默认为0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49')
parser.add_argument('-n', '--number', default='10', type=int, 
                    help='ROC列数，默认为10')
parser.add_argument('-v', '--value', default='0.1', type=float, 
                    help='ROC间隔值，默认为0.1')



args = parser.parse_args()

fprs=[float(x) for x in args.roc.split()]

count.roc(args.score, args.label, output=sys.stdout, fprs=fprs)
