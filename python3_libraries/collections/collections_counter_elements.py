#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Produce the elements of the counter.
"""

#end_pymotw_header
import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))
