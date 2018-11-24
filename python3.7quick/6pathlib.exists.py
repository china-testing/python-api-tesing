#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-10

import pathlib

file = pathlib.Path("china-testing.github.io.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")