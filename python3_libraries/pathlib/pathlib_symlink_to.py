#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-29
# from https://pymotw.com/3/pathlib/index.html
# pathlib_symlink_to.py

import pathlib

p = pathlib.Path('example_link')

p.symlink_to('example.txt')

print(p)
print(p.resolve().name)











