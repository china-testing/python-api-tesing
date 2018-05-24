#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：144081101
# CreateDate: 2018-1-8 
# check_md5.py

import multiprocessing
from pathlib import Path
import argparse
import os

import pandas as pd

import data_common
import photos

def consumer(queue, results, lock):
    while True:
        filename = queue.get()
        if filename is None:
            break      
        print(filename)
        if not '/photo/' in filename:
            continue
        photos.raw2jpg(filename)
        location = photos.find_face(filename + ".jpg",rotate=90, model='cnn')
        if location:
            print("Error: {}".format(filename))
            with lock:
                results.append(filename)      


if __name__ == '__main__':
    
    process = []
    queue = multiprocessing.Queue()
    results = multiprocessing.Manager().list()
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
    
    df = pd.read_excel('/opt/test_tools/base/faceunlock_test_general_meil/result/live_detect_error.xlsx')
    
    for item  in df['ir']:
        queue.put(item)
        
    for i in range(number):
        queue.put(None) 
        
    for i in range(number):
        process[i].join()       
       
    data_common.output_file("output.txt", results)
