#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-29
# https://pymotw.com/3/os.path/index.html
# ospath_expanduser.py

import os.path

for user in ['', 'andrew', 'nosuchuser']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.format(
        lookup, os.path.expanduser(lookup)))

































