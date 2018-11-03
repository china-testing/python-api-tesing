#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-03
"""

f = 101;
print(f)

def someFunction():
  # global f
  print(f)

  
print(f)
f = "changing global variable"
someFunction()
print(f)