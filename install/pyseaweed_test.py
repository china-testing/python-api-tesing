#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-2-27
# pyseaweed_test.py

from pyseaweed import WeedFS

# File upload
w = WeedFS("172.20.15.200", 9333) # weed-fs master address and port
fid = w.upload_file("/home/andrew/obama0.png") # path to file

# Get file url
file_url = w.get_file_url(fid)
print(file_url)







    