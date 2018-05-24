#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-04-02
# font.py

import matplotlib.pyplot as plt

fontparams = {'size':16,'fontweight':'light','family':'monospace','style':'normal'}
x = [1,2,3]
y = [2,4,6]
plt.plot(x,y)
plt.xlabel('xlabel',size=20,fontweight='semibold',family='serif',style='italic')
plt.ylabel('ylabel',fontparams)
plt.show()