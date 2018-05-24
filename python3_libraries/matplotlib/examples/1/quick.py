#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq群:630011153
# CreateDate: 2018-04-02
# quick.py

import matplotlib.pyplot as plt
# 注意pylab已经不推荐使用，建议分别导入Matplotlib.pyplot和numpy

evens = list(range(2,102,2))
plt.plot(evens,label = 'x')
plt.legend()
# matplotlib2.0不推荐使用Gimp Drawing Kit (GDK)，默认不支持JPG、TIFF
# dot per inch (dpi). Slideshow 96 dpi+
plt.savefig('output.png',dpi=100)
# 要保存和show图片的情况下，show尽量在后面。
plt.show()
