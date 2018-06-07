#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os
import glob
import json
import pprint
import json

import data_common

directory = 'data'
files = data_common.find_files_by_type(directory,'json')

i = 1
file_list = []
results = []
poses = []
for filename in files:
    d = json.load(open(filename))
    name = d['image']['rawFilename'].strip('.jpg')
    pos = d['objects']['face'][0]['position']
    num = len(d['objects']['face'])
    if num > 1:
        print(filename)
        print(name)
        pprint.pprint(d['objects']['face'])
    out = "# {}\n{}\n3 640 480 1\n0\n{}\n".format(i, name, num)
    for face in d['objects']['face']:
        pos = face['position']
        top = round(pos['top'])
        bottom = round(pos['bottom'])
        left = round(pos['left'])
        right = round(pos['right'])
        out = out + "1 {} {} {} {}\n".format(left, top, right, bottom)
        poses.append("{},{},{},{},{},{},{}".format(name, 
            left, top, right, bottom, right - left, bottom -top))
    i = i + 1
    #print(out)
    file_list.append(name)
    results.append(out.rstrip('\n'))

data_common.output_file("files.txt",file_list)
data_common.output_file("results.txt",results)
data_common.output_file("poses.txt",poses)


