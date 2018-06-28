#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""ChainMap as a namespace stack
"""

#end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)
