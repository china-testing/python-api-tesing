#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import multiprocessing
from pathlib import Path
import argparse
import os

import data_common

def consumer(queue, results, lock):
    while True:
        item = queue.get()
        if item is None:
            break        
        name = os.path.basename(item)
        md5 = data_common.get_md5(item, is_file=True)
        
        with lock:
            if md5 in results:
                print("Same md5", results[md5], name)
            else:
                results[md5] =[]
            results[md5] = results[md5] + [name]


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', action="store", help=u'目录')
    parser.add_argument('-t', action="store", dest="typename",
                        default="*", help=u'文件扩展名')
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.1 Rongzhong xu 2018 03 22')
    options = parser.parse_args()
    
    process = []
    queue = multiprocessing.Queue()
    results = multiprocessing.Manager().dict()
    lock = multiprocessing.Lock()
    if multiprocessing.cpu_count() < 3:
        number = multiprocessing.cpu_count()
    else:
        number = multiprocessing.cpu_count() - 1
    
    # Launch the consumer process
    for i in range(number):
        t = multiprocessing.Process(
            target=consumer,args=(queue, results, lock))
        t.daemon=True
        process.append(t)
    
    for i in range(number):
        process[i].start()
    
    p = Path(options.directory)   
    for item  in p.glob('**/*.{}'.format(options.typename)):
        queue.put(str(item))
        
    for i in range(number):
        queue.put(None) 
        
    for i in range(number):
        process[i].join()       
       
    f = open("md5_files.txt",'w')   
    f2 = open("files.txt",'w')   
    for item in dict(results):
        f2.write("{},{}\n".format(item,results[item]))
        if len(results[item]) > 1:
            f.write("{},{}\n".format(item,results[item]))