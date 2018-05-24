#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# datas.py
import time
import os

import pandas as pd

def get_verify_server_result(
    names,files,scores, score=0.7, output_dir="./",
    replace_file="/home/andrew/code/data/tof/base_test_data/vivo-verify-452/./",
    replace_name="output/enroll_list/",
    ):

    real_photos = pd.read_csv(files, names=['filename'])
    real_photos['filename'] = real_photos['filename'].apply(
        lambda x:x.replace(replace_file, ''))
    real_photos['person'] =  real_photos['filename'].apply(
        lambda x:x.split('/')[0])
    
    
    persons = pd.read_csv(names,names=['person'])
    persons['person'] = persons['person'].apply(
        lambda x:x.replace(replace_name, ''))
    
    df = pd.read_csv(scores, header=None, engine='c',
                     na_filter=False, low_memory=False)
    df.index = persons['person']
    
    self_errors = []    
    other_errors = []
    for person in df.index:
        print("index:", person)
        print(time.ctime())
        row = df.loc[person]
        row.index = [real_photos['person'], real_photos['filename']]
        self = row[person]
        self_error = self[(self<score) & (self>-1)]
        for item in self_error.index:
            self_errors.append((item, self_error[item]))
        print(self_error)
        others = row.drop(person,level=0)
        other_error = others[others>=score]
        for item in other_error.index:
            other_errors.append([person,item[1], other_error.loc[item]])    
        print(other_error)
                
    df_person_errors = pd.DataFrame(self_errors,columns=['filename','score'])
    df_other_errors = pd.DataFrame(other_errors,columns=['person','filename','score'])
    df_person_errors.to_csv('{}{}self_errors.csv'.format(
        output_dir.strip(os.sep), os.sep), index=False)
    df_other_errors.to_csv('{}{}others_errors.csv'.format(
        output_dir.strip(os.sep), os.sep), index=False)
    print(time.ctime())


