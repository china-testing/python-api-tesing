#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# parse_test_cases_data.py

'''
汇总测试用例生成的数据。

使用方法：

参数input_directory：为包含测试结果的目录。input_directory下面有测试人员的拼音名目录，
拼音名目录下有数字目录，比如01，对应测试用用例的序号。01目录下面有log.xls之类的测试记录
文件。

参数：output：为汇总测试的输出文件。
'''

import traceback
import re
import shutil
import os

import pandas

from data_common import maps, produce_xls

input_directory = r"D:\test"
output = r"D:\output.xls"
file_type = "xls"


def get_result(file_name, type_=0):
    '''
    统计测试工具生成的用例。
    '''
    try:
        if file_name.endswith('csv'):
            records = pandas.read_csv(file_name)
        else:
            records = pandas.read_excel(file_name)
        total = len(records)
        compare = len(records[records['比对'] == '通过'])
        live = len(records[records['活体'] == '通过'])
        eye = len(records[records['睁闭眼'] == '通过'])
        success = len(records[records['结果'] == '通过'])
        test = len(records[records['当前尝试次数'] == 1])

    except Exception as info:
        print('Error in reading: {}'.format(file_name))
        print(info)
        traceback.print_exc()
        print('continue...')
        total = compare = live = eye = success = test = 0
    
    if type_ != 0 :
        print(records)
        return (total, compare, live, eye, success, test)
    else:
        return (total, compare, live, success, test)

def get_results(input_directory,file_name='xls', type_=0):
    # 遍历目录以统计测试工具生成的xls文件
    results = {}
    for root, dirs, files in os.walk(input_directory):
    
        for file_name in files:
            if file_name.endswith(file_type):
                seq = int(root.split(os.sep)[-1].lstrip('0'))
                result = get_result(
                    u"{}{}{}".format(root, os.sep, file_name),type_)
                if seq not in results:
                    results[seq] = []
                results[seq].append(result)
                if str(seq) not in file_name:
                    os.chdir(root)
                    shutil.move(file_name, u"{}_{}".format(seq, file_name))
    return results


results = get_results(input_directory,type_=0)
print(results)
produce_xls(results, output, 50, type_=0)

#results = get_results(input_directory,type_=1)
#print(results)
#produce_xls(results, output, 76, type_=1)