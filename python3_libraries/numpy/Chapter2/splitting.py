#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-12

import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates array splitting.
#
# Run from the commandline with 
#
#  python splitting.py
print("In: a = arange(9).reshape(3, 3)")
a = np.arange(9).reshape(3, 3)

print("In: a")
print(a)
#Out: 
#array([[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]])

# 水平分割
print("In: hsplit(a, 3)")
print(np.hsplit(a, 3))
#Out: 
#[array([[0],
#       [3],
#       [6]]),
# array([[1],
#       [4],
#       [7]]),
# array([[2],
#       [5],
#       [8]])]

# 垂直分割 
print("In: split(a, 3, axis=1)")
print(np.split(a, 3, axis=1))
#Out: 
#[array([[0],
#       [3],
#       [6]]),
# array([[1],
#       [4],
#       [7]]),
# array([[2],
#       [5],
#       [8]])]

# 
print("In: vsplit(a, 3)")
print(np.vsplit(a, 3))
#Out: [array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]

print("In: split(a, 3, axis=0)")
print(np.split(a, 3, axis=0))
#Out: [array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]

# 深度分割 
print("In: c = arange(27).reshape(3, 3, 3)")
c = np.arange(27).reshape(3, 3, 3)

print("In: c")
print(c)
#Out: 
#array([[[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8]],
#
#       [[ 9, 10, 11],
#        [12, 13, 14],
#        [15, 16, 17]],
#
#       [[18, 19, 20],
#        [21, 22, 23],
#        [24, 25, 26]]])

print("In: dsplit(c, 3)")
print(np.dsplit(c, 3))
#Out: 
#[array([[[ 0],
#        [ 3],
#        [ 6]],
#
#       [[ 9],
#        [12],
#        [15]],
#
#       [[18],
#        [21],
#        [24]]]),
# array([[[ 1],
#        [ 4],
#        [ 7]],
#
#       [[10],
#        [13],
#        [16]],
#
#       [[19],
#        [22],
#        [25]]]),
# array([[[ 2],
#        [ 5],
#        [ 8]],
#
#       [[11],
#        [14],
#        [17]],
#
#       [[20],
#        [23],
#        [26]]])]

