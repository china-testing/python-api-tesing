#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-3-27
# rectangle.py
import argparse
import json

import photos

description = '''

功能：在图片上画框，

示例： 
$ python3 rectangle.py image_1515231433877.ir.jpg '{"red":[181,286,330,441]}' -a left
上面的181,286,330,441分别表示左、上、右、下。

$ python3 rectangle.py image_1515231433877.ir.jpg '{"red":[181,286,330,441],"blue":[175,288,335,449]}' -a left

'''

parser = argparse.ArgumentParser(description=description, 
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('filename', action="store", help=u'文件名')
parser.add_argument('poses', action="store", help=u'颜色和位置')
parser.add_argument('-o', action="store", dest="output", default="output.jpg", 
                    help=u'输出文件名')
parser.add_argument('-a', action="store", dest="angle", default="", 
                    help=u'方向，默认为空，可以填left 或 right')
parser.add_argument('-r', action="store_true", default=False,
                    dest="relative", help=u'后面两个值是否为宽度和高度。')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 05 09')
options = parser.parse_args()

poses = json.loads(options.poses)
print(poses)
photos.mark_image(options.filename, options.output, poses, angle=options.angle,
                  relative=options.relative)

