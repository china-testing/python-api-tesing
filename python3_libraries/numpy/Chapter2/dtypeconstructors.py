#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-12

import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy dtype constructors.
#
# Run from the commandline with 
#
#  python dtypeconstructors.py
# Python中的浮点数类型
print("In: dtype(float)")
print(np.dtype(float))
#Out: dtype('float64')

# 字符编码来指定单精度浮点数类型
print("In: dtype('f')")
print(np.dtype('f'))
#Out: dtype('float32')

# 字符编码来指定双精度浮点数类型
print("In: dtype('d')")
print(np.dtype('d'))
#Out: dtype('float64')

# 两个字符作为参数传给数据类型的构造函数, 第一个字符表示数据类型，
# 第二个字符表示该类型在内存中占用的字节数（2、4、8分别代表精度为16、32、64位的浮点数）
print("In: dtype('f8')")
print(np.dtype('f8'))
#Out: dtype('float64')


print("In: dtype('Float64')")
print(np.dtype('Float64'))
#Out: dtype('float64')

print(np.sctypeDict.keys())
