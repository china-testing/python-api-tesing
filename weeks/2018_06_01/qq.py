#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong@126.com wechat:pythontesting qq:37391319
# 
# CreateDate: 2018-6-1

import re
from pypinyin import lazy_pinyin

name = r'test.txt'

text = open(name,encoding='utf-8').read()
#print(text)

results = re.findall(r'(:\d+)\s(.*?)\(\d+', text)

names = set()
for item in results:
    names.add(item[1])  

keys = list(names)
keys = sorted(keys)

def compare(char):
    try:
        result = lazy_pinyin(char)[0][0]
    except Exception as e:
        result = char
    return result
    
keys.sort(key=compare)
print(keys)
    


