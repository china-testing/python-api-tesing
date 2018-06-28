#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-29
# from https://pymotw.com/3/pathlib/index.html
# pathlib_parents.py

import pathlib

p = pathlib.PurePosixPath('/usr/local/lib')


print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)





