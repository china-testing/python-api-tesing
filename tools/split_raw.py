#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import argparse

from photos import *
from data_common import *
    
parser = argparse.ArgumentParser()
parser.add_argument('directory', action="store", help=u'文件名')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 04 11')
options = parser.parse_args()

files = find_files_by_type(options.directory,filetype="raw")
for filename in files:
    split_raw(filename)
