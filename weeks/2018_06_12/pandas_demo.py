#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def test(x):
    if x['A'] in x['B']:
        return True
    else:
        return False

df = pd.DataFrame( {'A':['Ford', 'Toyota', 'Ford','Audi'], 
                    'B':['Ford F-Series pickup', 'Camry', 'Ford Taurus/Taurus X', 'Audi test']} )
print(df)
# 输出列B包含列A内容的记录
print(df[df.apply(test, axis=1)])

# 输出列A为Ford或Toyota的记录
print(df[df['A'].str.match('Ford|Toyota')])