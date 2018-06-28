#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-29
# from https://pymotw.com/3/pathlib/index.html
# pathlib_resolve.py

import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(type(share.resolve()))
print(share.resolve())
