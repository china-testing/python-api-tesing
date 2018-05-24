#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-4-18 
# check_md5.py

import argparse
import time

import pandas as pd

import servers
import data_common

'''
调用示例：

$ python3 get_verify_server_result.py /opt/test_tools/base/faceunlock_test_general_meil/result/i_enroll.txt /opt/test_tools/base/faceunlock_test_general_meil/result/i_real.txt /opt/test_tools/base/faceunlock_test_general_meil/result/verify452-3.56.csv 

$ python3 get_verify_server_result.py i_enroll.txt  i_real.txt 3.41.0-result.csv  -f /home/andrew/code/data/common/verify/india_32/./  -n /opt/test_tools/base/faceunlock_test_general_meil/output/enroll_list/
'''

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('names', action="store", help=u'测试人名列表文件')
    parser.add_argument('files', action="store", help=u'测试图片列表文件')
    parser.add_argument('scores', action="store", help=u'服务器verify结果')
    parser.add_argument('-d', action="store_true", default=False, help=u'是否批量')
    parser.add_argument('-s', action="store", dest="score", default=0.7, 
                        help=u'分数的门限')
    parser.add_argument('-o', action="store", dest="output",
                        default="verify_error.xlsx", help=u'结果输出文件')
    parser.add_argument('-f', action="store", dest="replace_file",
                        default="/home/andrew/code/data/tof/base_test_data/vivo-verify-452/./",
                        help=u'文件名需要替换为空的部分')    
    parser.add_argument('-n', action="store", dest="replace_name",
                        default="output/enroll_list/", help=u'人名需要替换为空的部分')     
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.1 Rongzhong xu 2018 03 22')
    options = parser.parse_args()
    
    servers.get_verify_server_result(
            options.names, options.files, options.scores,
            score=options.score, output_dir=options.output,
            replace_file=options.replace_file,
            replace_name=options.replace_name,) 