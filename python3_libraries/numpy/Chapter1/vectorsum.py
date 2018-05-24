#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：6089740
# CreateDate: 2018-04-12
# vectorsum.py

import sys
from datetime import datetime
import numpy as np

"""
该段代码演示Python中的向量加法
使用如下命令运行程序：
python vectorsum.py n
n为指定向量大小的整数
加法中的第一个向量包含0到n的整数的平方
第二个向量包含0到n的整数的立方
程序将打印出向量加和后的最后两个元素以及运行消耗的时间
"""

def numpysum(n):
   a = np.arange(n) ** 2
   b = np.arange(n) ** 3
   c = a + b

   return c

def pythonsum(n):
   a = list(range(n))
   b = list(range(n))
   c = []

   for i in range(len(a)):
      a[i] = i ** 2
      b[i] = i ** 3
      c.append(a[i] + b[i])

   return c
   

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)
