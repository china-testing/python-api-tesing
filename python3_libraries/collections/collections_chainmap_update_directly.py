#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""Updating values through a ChainMap
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('a:', a)
