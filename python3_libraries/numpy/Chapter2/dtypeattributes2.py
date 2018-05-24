#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-12
import numpy as np

# Chapter2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy 
# dtype attributes
#
# Run from the commandline with 
#
#  python dtypeattributes2.py
print("In: t = dtype('Float64')")
t = np.dtype('Float64')

# 获取数据类型的字符编码
print("In: t.char")
print(t.char)
#Out: 'd'

# type 属性对应于数组元素的数据类型
print("In: t.type")
print(t.type)
#Out: <type 'numpy.float64'>

# 大端序（big-endian）和小端序（little-endian）。大端序是将最高位字节存储在最低的内存
#地址处，用 > 表示；与之相反，小端序是将最低位字节存储在最低的内存地址处，用 < 表示：
print("In: t.str")
print(t.str)
#Out: '<f8'



