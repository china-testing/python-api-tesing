#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import argparse

from data_common import *
    
description = '''

功能：检查文件是否落单。

活体的比对要使用ir和depth文件，文件必须一一对应。但是采集的数据有时会只有ir或者depth文件。

本程序检查文件是否一一匹配，并输出不匹配的文件到屏幕，如果加以-d参数，则会把这些文件予以删除。

示例：
$ python3 pair.py /home/andrew/code/tmp_photos/liveness
directory: /home/andrew/code/tmp_photos/liveness
ir: 47
depth: 49
{'/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_27_0.0', '/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_28_0.0'}
/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_27_0.0.depth
/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_28_0.0.depth

$ python3 pair.py /home/andrew/code/tmp_photos/liveness -d # 删除落单的文件
directory: /home/andrew/code/tmp_photos/liveness
ir: 47
depth: 49
{'/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_27_0.0', '/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_28_0.0'}
/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_27_0.0.depth
--remove /home/andrew/code/tmp_photos/liveness/real/20180414/hacker_27_0.0.depth
/home/andrew/code/tmp_photos/liveness/real/20180414/hacker_28_0.0.depth
--remove /home/andrew/code/tmp_photos/liveness/real/20180414/hacker_28_0.0.depth

'''    
parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('directory', action="store", help=u'目录')
parser.add_argument('-d', action="store_true", default=False, help=u'是否删除文件')
parser.add_argument('-type1', action="store", dest="type1", default="ir", 
                    help=u'第1个文件扩展名，默认为ir，通常不需要修改')
parser.add_argument('-type2', action="store", dest="type2", default="depth", 
                    help=u'第2个文件扩展名，默认为depth，通常不需要修改')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 04 02')
options = parser.parse_args()

check_pair_file(options.directory, options.type1, options.type2, options.d)