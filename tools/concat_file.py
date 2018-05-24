#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-3-31

import os
import argparse
from pathlib import Path

import data_common 

parser = argparse.ArgumentParser()
parser.add_argument('file1', action="store")
parser.add_argument('file2', action='store', help='测试类型')
parser.add_argument('-s', action='store', dest='sep', default=' ',
                    help='分隔符')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 03 31')
options = parser.parse_args()

new = data_common.concat_file(options.file1,options.file2,options.sep)
data_common.output_file(options.file1, new)


