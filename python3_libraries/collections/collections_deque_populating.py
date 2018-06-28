#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Adding items to a deque.
"""

#end_pymotw_header
import collections

# Add to the right
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)
