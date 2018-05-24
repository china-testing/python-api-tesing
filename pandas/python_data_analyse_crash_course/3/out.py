#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-3-31
# out.py

import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")
print(anscombe)
dataset_1 = anscombe[anscombe['dataset'] == 'I']
plt.plot(dataset_1['x'], dataset_1['y'])