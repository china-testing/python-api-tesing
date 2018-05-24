#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-04-02
# quick.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Prepare 4 lines with different slopes
x = np.linspace(0,200,100) # Prepare 100 evenly spaced numbers from
# 0 to 200
y1 = x*2
y2 = x*3
y3 = x*4
y4 = x*5
# Set line width to 2 for clarity
mpl.rcParams['lines.linewidth'] = 2
# Drawing the 4 lines
plt.plot(x,y1,label = '2x', c='0') # Black solid line
plt.plot(x,y2,label = '3x', c='0.2', ls='--') # Dark grey dashed line
plt.plot(x,y3,label = '4x', c='0.4', ls='-.') # Grey dash-dot line
plt.plot(x,y4,label = '5x', c='0.6', ls=':') # Light grey dotted line
plt.legend()
plt.show()