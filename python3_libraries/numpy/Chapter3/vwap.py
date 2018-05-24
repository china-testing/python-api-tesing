#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-17

import numpy as np

#  unpack 参数设置为 True ，意思是分拆存储不同列的数据，即分别将收
# 盘价和成交量的数组赋值给变量 c 和 v 。
c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
vwap = np.average(c, weights=v)
print("VWAP =", vwap)

print("mean =", np.mean(c))

# 计算TWAP
t = np.arange(len(c))
print("twap =", np.average(c, weights=t))
