#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-3-31

import json
import pprint
import argparse


description = '''

功能：以更可读的方式显示json文件

-d参数可以显示北京标注数据的人脸数据，并计算宽度width和高度height。

示例： 
$  python3 read_json.py /home/andrew/code/data/detectdata-20180507/20180418_tof_mayongxin/Label/ffff9a9a9a4fb559a9e4ee439c7eaf56.json  -d
$  python3 read_json.py /home/andrew/code/data/detectdata-20180507/20180418_tof_mayongxin/Label/ffff9a9a9a4fb559a9e4ee439c7eaf56.json
'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('filename', action="store", help=u'文件名')
parser.add_argument('-d', action="store_true", default=False, 
                    help=u'是否显示详细数据，主要针对北京标注数据使用。')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 05 11')
options = parser.parse_args()

d = json.load(open(options.filename))
print('\n{}\n'.format(options.filename))
print('#'*80)
print('\n')
pprint.pprint(d)

if options.d:
    print('#'*80)
    print('\nimage\n')
    pprint.pprint(d['image'])
    for face in d['objects']['face']:
        print('#'*80)
        print('\nface\n')    
        pprint.pprint(face['position'])
        print("width", face['position']['right'] - face['position']['left'])
        print("height", face['position']['bottom'] - face['position']['top'])
    
    



