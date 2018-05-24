#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-4-18 
# check_md5.py

'''
python3 get_live_server_result.py /opt/test_tools/base/faceunlock_test_general_meil/result/label-live.txt  /opt/test_tools/base/faceunlock_test_general_meil/result/live-files.txt  /opt/test_tools/base/faceunlock_test_general_meil/result/live3.71.csv -s 0.99
'''

import pandas as pd
import os
import argparse

import servers

parser = argparse.ArgumentParser()
parser.add_argument('labels', action="store", help=u'labels')
parser.add_argument('files', action="store", help=u'测试图片列表文件')
parser.add_argument('scores', action="store", help=u'服务器liveness结果')
parser.add_argument('-s', action="store", dest="score", default=0.99, type=float,
                    help=u'分数的门限')
parser.add_argument('-r', action="store_true", default=False, 
                    help=u' 是否用中文用例名字替换数字。')
parser.add_argument('-o', action="store", dest="output",
                    default="live_result.xlsx", help=u'结果输出目录') 
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 04 18')
options = parser.parse_args()

servers.get_liveness_server_result(options.scores, options.files, 
    options.labels, score=options.score, error_name=options.output)
    
    


