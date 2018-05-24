#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-17
import numpy as np

c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print("median =", np.median(c))
sorted = np.msort(c)
print("sorted =", sorted)

N = len(c)
print("middle =", sorted[(N - 1)/2])
print("average middle =", (sorted[N /2] + sorted[(N - 1) / 2]) / 2)

print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean())**2))
