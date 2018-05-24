#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-04-02
# latex.py

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,200,100) # Prepare 100 evenly spaced numbers from 0 to
200
y1 = x # Prepare an array of y equals to x squared
y2 = x+20
# Plot a curve of square numbers
plt.plot(x,y1,label = '$x$')
plt.plot(x,y2,label = r'$x^2+\alpha$')
plt.legend()
plt.show()