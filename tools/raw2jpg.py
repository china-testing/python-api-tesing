#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import argparse

from photos import *
from data_common import *
    
parser = argparse.ArgumentParser()
parser.add_argument('filename', action="store", help=u'文件名')
parser.add_argument('-b', action="store_true", default=False, help=u'是否批量')
parser.add_argument('-t', action="store", dest="type", default="ir", 
                    help=u'文件类型')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 04 11')
options = parser.parse_args()

if options.b:
    for name in find_files_by_type(options.filename,filetype=options.type):
        raw2jpg(name)    
else:
    raw2jpg(options.filename)