#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# 讨论钉钉免费群21745728 qq群144081101 567351477
# CreateDate: 2018-11-03
"""

# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
  f = 'I am learning Python'
  print(f)
someFunction()
print(f)