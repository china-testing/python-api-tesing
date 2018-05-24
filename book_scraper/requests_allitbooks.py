#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong@126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-19

'''
根据bug列表生成统计。
'''
import argparse
import re
import shutil
import os
import time
import random
import traceback

import requests

def find_address(url, key, type_=False):
    print(url)
    keys = key.lower().split()
    result = requests.get(url)
    books = re.findall(r'href="(.*?)" rel="bookmark', result.text)
    #print(set(books))
    valids = []
    for item in set(books):
        if type_:
            flag = True        
        else:
            flag = False
            for key_ in keys:
                if key_ in item:
                    flag = True
                    break
        if flag:
            valids.append(item)  
    #print(valids)
    return valids

def find_addresses(key, type_=False):
    if type_:
        url = "{}{}".format(r"http://www.allitebooks.com/", key)  
    else:
        keys = key.lower().split()
        url = "{}{}".format(r"http://www.allitebooks.com/?s=", "+".join(keys)) 
    print(url)
    result = requests.get(url)
    page_num = re.search(r'/\s+(\d+)\s+Pages', result.text)
    urls =[url,]
    if page_num:
        page_num = int(page_num.group(1))
   
        # http://www.allitebooks.com/?s=testing
        # http://www.allitebooks.com/page/2/?s=testing
        for i in range(2, page_num + 1):
            urls.append(url.replace('com/', 'com/page/{}/'.format(i)))
        
    addresses = []
    for address in urls:
        result = find_address(address, key, type_)
        if result:
            addresses =  addresses + result
        else:
            return addresses
    return addresses
        

parser = argparse.ArgumentParser()
parser.add_argument('keys', action="store", help=u'要查询的关键字，以空格分隔')
parser.add_argument('-d', action="store_true", default=False, help=u'是否下载')
parser.add_argument('-o', action="store", dest="o",
                    default="/home/andrew/code/tmp_books", help=u'输出目录')
parser.add_argument('-c', action="store_true", default=False, help=u'按类别下载')
parser.add_argument('-y', action="store", dest="year",
                    default=2013, help=u'输出目录')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 03 19')

options = parser.parse_args()
print(options.d)

valids = find_addresses(options.keys, options.c)
print(valids)        

actuals = []
for file_link in valids:
    attempts = 0   
    result = False
    while attempts < 3:    
        try:
            result = requests.get(file_link,timeout=10)
            result = True
        except Exception as info:
            time.sleep(random.randint(1,5))
            attempts += 1
            print('Error: {}'.format(file_link))
            print(info)
            traceback.print_exc()
    
    if not result:
        continue
    year_search = re.search(r'Year.*?(\d+)<', result.text)
    year = year_search.group(1) if year_search else '1900'
    link_search = re.search('ref="(.*?)" target="_blank"', result.text)
    if not link_search:
        print("Can not find link in {}".format(file_link))
        continue
    else:
        link = link_search.group(1)
    print(year, link)
    if int(year) < int(options.year):
        print("skip old files!")
        continue
    
    name = '-{}.'.format(year).join(link.split('/')[-1].split('.'))
    filename = "{}{}{}".format(options.o, os.sep, name) if options.o else name	
    url = link.replace(" ","%20")
    actuals.append("* [{0}]({1})".format(name, url))
    
    if options.d:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)  
        else:
            print("Failed to download {}".format(url))
                
for item in actuals:
    print(item)