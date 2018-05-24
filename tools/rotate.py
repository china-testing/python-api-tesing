#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-3-27
# pillow_rotate.py
import glob
import os 
import argparse

from PIL import Image

import photos
import data_common

description = '''

功能：旋转图片

示例： $ python3 rotate.py /home/andrew/code/tmp_photos2 /home/andrew/code/tmp_photos3 -a 270
'''

parser = argparse.ArgumentParser(description=description, 
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('src', action="store", help=u'源目录')
parser.add_argument('dst', action="store", help=u'目的目录')
parser.add_argument('-t', action="store", dest="type", default="jpg", 
                    help=u'文件扩展名, 默认为jpg')
parser.add_argument('-a', action="store", dest="angle", default=90, type=int,
                    help=u'旋转角度，默认为90度，方向都为逆时针。')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 04 26')
options = parser.parse_args()

data_common.check_directory(options.dst)
files = data_common.find_files_by_type(options.src, filetype=options.type)
photos.rotate(files, options.dst, options.angle)

