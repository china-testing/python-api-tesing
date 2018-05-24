#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting QQ群:630011153
# CreateDate: 2018-3-9
# write_csv.py

import pandas as pd

data ={'qq': [37391319,37391320], 'group':[1,2]}

df = pd.DataFrame(data=data, columns=['qq','group'])
df.to_csv('2.csv',index=False)



