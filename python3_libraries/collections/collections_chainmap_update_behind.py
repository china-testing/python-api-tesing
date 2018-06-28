#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""Updating values underneath a ChainMap
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))
