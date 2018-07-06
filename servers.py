#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# datas.py
import time
import os
import subprocess

from pathlib import Path

import pandas as pd
import numpy as np

def get_live_frr_far(df,colomn1,score,colomn2):
    
    total = len(df)
    #print(df.head())
    unknow = len(df[df[colomn1] == -1])
    df = df[df[colomn1] != -1]
    real_number = len(df[df[colomn2] == 0])
    photo_number = len(df[df[colomn2] == 1])
    num_2d = len(df.loc[df['filename'].str.contains('/2D_photo/')])
    num_3d = len(df.loc[df['filename'].str.contains('/3D_photo/')])
    num_3d_high = len(df.loc[df['filename'].str.contains('/3D_Highcost/')])
    num_3d_low = len(df.loc[df['filename'].str.contains('/3D_Lowcost/')])
    
    # 真人识别为假人
    frr_number = len(df.loc[((df[colomn1] > score) & (df[colomn2] == 0))])
    # 假人识别为真人
    far_number = len(df.loc[((df[colomn1] < score) & (df[colomn2] == 1))])
    # 2d假人识别为真人
    
    far_number_2d = far_number_3d = 0
    far_number_2d = len(df.loc[((df[colomn1] < score) & (df[colomn2] == 1) &
                                df['filename'].str.contains('/2D_photo/', regex=False))]) 
    ## 3d假人识别为真人
    far_number_3d = len(df.loc[((df[colomn1] < score) & (df[colomn2] == 1) &
                                df['filename'].str.contains('/3D_photo/', regex=False))])  
    far_number_3d_high = len(df.loc[((df[colomn1] < score) & (df[colomn2] == 1) &
                                df['filename'].str.contains('/3D_Highcost/', regex=False))])   
    far_number_3d_low = len(df.loc[((df[colomn1] < score) & (df[colomn2] == 1) &
                                     df['filename'].str.contains('/3D_Lowcost/', regex=False))])       
    frr = 0 if not real_number else frr_number/float(real_number)
    far2d = 0 if not num_2d else far_number_2d/float(num_2d)
    far3d = 0 if not num_3d else far_number_3d/float(num_3d)
    far3d_high = 0 if not num_3d_high else far_number_3d_high/float(num_3d_high)
    far3d_low = 0 if not num_3d_low else far_number_3d_low/float(num_3d_low)
    far = 0 if not photo_number else far_number/float(photo_number)
    return (far, frr, total, real_number, frr_number, photo_number, far_number, 
            unknow, unknow/float(total),
            num_2d, far_number_2d, far2d, num_3d, far_number_3d, far3d, 
            num_3d_high, far_number_3d_high, far3d_high,
            num_3d_low, far_number_3d_low, far3d_low)

def get_gaze_frr_far(df,colomn1,score):
    
    total = len(df)
    unknow = len(df[df[colomn1] == -1])
    df = df[df[colomn1] != -1]
    real_number = len(df.loc[df['filename'].str.contains('/gaze/')])
    no_number = len(df.loc[df['filename'].str.contains('/no_gaze/')])
    
    # 真人识别为假人
    frr_number = len(df.loc[(df['score'] < score) & df['filename'].str.contains('/gaze/')])
    # 假人识别为真人
    far_number = len(df.loc[(df['score'] > score) & df['filename'].str.contains('/no_gaze/')] )
    frr = 0 if not real_number else frr_number/float(real_number)
    far = 0 if not no_number else far_number/float(no_number)
    return (far, frr, total, real_number, frr_number, no_number, far_number, unknow, unknow/float(total))


def load_verify_server_result(names,files,scores, 
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
    
    score = np.fromfile(scores, dtype=np.float32)
    score = score.reshape(len(persons), len(real_photos))
    df = pd.DataFrame(score, columns=real_photos['filename'])
    df.index = persons['person']
    return df, real_photos


def get_verify_errors(df, real_photos, positive=0.7, negative=0.7):
    
    other_errors = []
    self_errors = []
    self_nums = 0
    other_nums = 0
    for person in df.index:
        print("index: {}   {}".format(person,time.ctime()))
        row = df.loc[str(person)]
        #print(row)
        row.index = [real_photos['person'].astype(str), real_photos['filename']]
        #print(row)
        self = row[str(person)]
        self_nums = self_nums + len(self)
        self_error = self[(self<positive) & (self>-1)]
        for item in self_error.index:
            self_errors.append((item, self_error[item]))
        #print(self_error)
        others = row.drop(person,level=0)
        other_nums = other_nums + len(others)
        other_error = others[others>=negative]
        for item in other_error.index:
            other_errors.append([person,item[1], other_error.loc[item]])    
        #print(other_error)
                
    df_person_errors = pd.DataFrame(self_errors,columns=['filename','score'])
    df_other_errors = pd.DataFrame(other_errors,columns=['person','filename','score'])
    
    return df_person_errors, df_other_errors, self_nums, other_nums

def get_verify_frr_far(selfs_num, others_num, df_person_errors, df_other_errors, colomn, score):
    
    frr_num = len(df_person_errors[df_person_errors[colomn] < score])
    far_num = len(df_other_errors[df_other_errors[colomn] > score])
    frr = 0 if not frr_num else frr_num/float(selfs_num)
    far = 0 if not far_num else far_num/float(others_num)
    return (far, frr, selfs_num + others_num, selfs_num, frr_num, others_num, far_num)
    
def get_verify_server_result(
    names,files,scores, score=0.7, output_dir="./",
    replace_file="/home/andrew/code/data/tof/base_test_data/vivo-verify-452/./",
    replace_name="output/enroll_list/", error_name="verify_error.xlsx"):

    df, real_photos = load_verify_server_result(
        names, files, scores, replace_file=replace_file, 
        replace_name=replace_name)    

    #print(df.head())
    #print(real_photos.head())
    df.to_csv("count.csv")
    
    df_person_errors, df_other_errors, selfs_num, others_num = \
        get_verify_errors(df, real_photos, positive=0.9, negative=0.7)
    
    writer = pd.ExcelWriter(error_name)
    df_person_errors.to_excel(writer, sheet_name='本人识别分值低于0.9', index=False)
    df_other_errors.to_excel(writer, sheet_name='他人识别高于0.7', index=False)   
    
    #print(df_person_errors.head())
    #print(df_other_errors.head())
    
    values = [0.70, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80,
              0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90]
    
    results = []
    for value in values:
        result = get_verify_frr_far(
            selfs_num, others_num, df_person_errors, df_other_errors, 'score',
            value)
        results.append([value, *result])
        
    df4 = pd.DataFrame(
        results, 
        columns=["Threshold","FAR", "FRR", "number","real_number", "frr_number",
                 "no_number", "far_number"])
    
    df4.to_excel(writer, sheet_name='FAR_FRR', index=False)  
    writer.save()
    
def check_process(name):
    cmd = "ps afx | grep -i '{}' | grep -v grep |wc -l".format(name)
    result = subprocess.check_output(cmd, shell=True)
    return True if int(result.strip()) else False

def wait_until_stop(name,sep=1):
    print("Waiting " + name)
    while check_process(name):
        time.sleep(sep)

def get_liveness_server_result(scores, files, labels, score=0.95,
        replace='/home/andrew/code/data/tof/base_test_data/vivo-liveness/',
        error_name="live_error.xlsx",type_=''):
    
    cases = {
        "01": "注册",
        "02": "全脸-稳定拍摄",
        "03": "全脸-晃动拍摄",
        "04": "半脸-鼻子以下超出画面",
        "05": "半脸-眉毛以上超出画面",
        "06": "遮挡大部分五官",
        "07": "遮挡部分五官",
        "08": "手机平放桌面",
        "09": "一睁一闭",
        "10": "闭眼(戴墨镜、裸眼、普通眼镜) ",
        "11": "闭眼(戴墨镜、普通眼镜下滑挡住眼睛) ",
        "12": "闭眼(手机晃动)",
        "13": "注视",
        "14": "非注视",
        "15": "侧躺、平躺"}
    
    
    def rename(name):
        type_ = os.path.dirname(name.replace(replace,"").split()[-1])
        last = type_.split('/')[-1]
        if last in cases and replace:
            type_ = type_.replace(last,cases[last])
        return type_
    
    
    df_score = pd.read_csv(scores, header=None, names=['score'], engine='c',
                     na_filter=False, low_memory=False)
    df_file = pd.read_csv(files, header=None, names=['filename'])
    df_label = pd.read_csv(labels, header=None, names=['label'], engine='c',
                     na_filter=False, low_memory=False)
    
    df = pd.concat([df_label, df_score, df_file], axis=1)
    df['type'] = df['filename'].apply(rename)
    # print(df.head())
    
    results =[]
    
    for name, group in df.groupby('type'):
        result = get_live_frr_far(group, 'score', score, 'label')
        results.append([name,  *result[:9]])
        
        
    for name, group in df.groupby('label'):
        result = get_live_frr_far(group, 'score', score, 'label')
        results.append([name,  *result[:9]])  
    
    # 真人识别为假人
    df1 = df.loc[((df['score'] > score) & (df['label'] == 0))]
    # 假人识别为真人
    df2 = df.loc[((df['score'] < score) & (df['label'] == 1))]
    result = get_live_frr_far(df, 'score', score, 'label')
    results.append(["All", *result[:9]])
    writer = pd.ExcelWriter(error_name)
    df1.to_excel(writer, sheet_name='真人识别为假人', index=False)
    df2.to_excel(writer, sheet_name='假人识别为真人', index=False)
    
    #print(results)
    df3 = pd.DataFrame(results, columns=[
        "类别","far", "frr", "总数","真人总数","真人识别为假人", "假人总数", 
        "假人识别为真人","未识别数","未识别率"])
    df3.to_excel(writer, sheet_name='分类统计', index=False)

    
    results = []
    values = [0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 0.999]
    for value in values:
        result = get_live_frr_far(df, 'score', value, 'label')
        results.append([value, *result])
        
    columns=["Threshold","FAR","FRR","total",
             "real_num","frr_num", "photo_num", "far_num", "unknow","unknow_rate",
            'num_2d', 'far_number_2d', 'far2d', 
            'num_3d', 'far_number_3d', 'far3d',
            'num_3d_high', 'far_number_3d_high', 'far3d_high',
            'num_3d_low', 'far_number_3d_low', 'far3d_low']
    
    df4 = pd.DataFrame(results, columns=columns) 
    df4.to_excel(writer, sheet_name='FAR_FRR', index=False)
    writer.save()
    return df1, df2, df3, df4
    
    
def get_gaze_server_result(scores, files, labels, score=0.3,
        error_name="gaze_error.xlsx", type_=""):
    
    values = []    
    for i in range(18):
        values.append(i*0.05+0.1)    

    df_score = pd.read_csv(scores, header=None, names=['score'])
    df_file = pd.read_csv(files, header=None, names=['filename'])
    df_label = pd.read_csv(labels, header=None, names=['label'])
    
    df = pd.concat([df_label, df_score, df_file], axis=1)
    
    df1 = df.loc[(df['score'] < score) & df['filename'].str.contains('/gaze/')]
    df2 = df.loc[(df['score'] > score) & df['filename'].str.contains('/no_gaze/')]
    
    writer = pd.ExcelWriter(error_name)
    df1.to_excel(writer, sheet_name='注视识别为非注视', index=False)
    df2.to_excel(writer, sheet_name='非注视识别为注视', index=False)


    
    results = []
    for value in values:
        result = get_gaze_frr_far(df, 'score', value)
        results.append([value, *result])
    
    df4 = pd.DataFrame(
        results, 
        columns=["Threshold","FAR", "FRR", "number","real_number", "frr_number",
                 "no_number", "far_number","unknow","unknow_rate"])
    
    df4.to_excel(writer, sheet_name='FAR_FRR', index=False)
    writer.save()
    
    
def get_eye_server_result(values, score=0.95,
        error_name="eye_error.xlsx", type_=""):             
    
    df = pd.read_csv(values, sep=' |,', engine='python',
        names=['left_score','left_valid','right_score','right_valid','name'])
    
    df_unknow = df[df['left_score'] == -1]     
    df_error = df[df['left_score'] == -2]
    
    df2 = df[df['left_score'] > -1]   
    close_error = df2[df2['name'].str.contains('/close/') & ((df2['left_score'] > 9.5) | (df2['right_score'] > 9.5))]
    open_error = df2[df2['name'].str.contains('/open/') & (df2['left_score'] < 9.5) & (df2['right_score'] < 9.5)]
    invalid_error = df2[df2['name'].str.contains('/invalid/') & ((df2['left_valid'] > 9.5) | (df2['right_valid'] > 9.5))]
    valid_error = df2[df2['name'].str.contains('/valid/') & (df2['left_valid'] < 9.5) & (df2['right_valid'] < 9.5)]
    writer = pd.ExcelWriter(error_name)
    df_unknow.to_excel(writer, sheet_name='未认识人脸', index=False)
    df_error.to_excel(writer, sheet_name='图片格式错误', index=False)
    close_error.to_excel(writer, sheet_name='闭眼识别为睁眼', index=False)
    open_error.to_excel(writer, sheet_name='睁眼识别为闭眼', index=False)
    invalid_error.to_excel(writer, sheet_name='无效识别为有效', index=False)
    valid_error.to_excel(writer, sheet_name='有效识别为无效', index=False)
    writer.save()


def build_verify_input(directory, output,filetype='ir'):
    peoples = {}
    files = []
    p = Path(directory)
    root = "{}{}".format(directory.rstrip(os.sep), os.sep)
    print('root', root,"filetype", filetype)
    
    for file_name in p.glob('**/*.{0}'.format(filetype)):
        file_str = str(file_name)
        #print(file_str)
        people = file_str.split(os.sep)[-3]
        if not people in peoples:
            peoples[people] = []
        peoples[people].append(file_str.replace(root,""))
    
    enroll_list = "{}{}enroll_list".format(output, os.sep)
    if not os.path.exists(enroll_list):
        os.makedirs(enroll_list)
    
    label_enroll = np.array([], dtype=int)
    label_real = np.array([], dtype=int)
    
    with open("{}{}i_enroll.txt".format(output, os.sep), 'w') as i_enroll:
        with open("{}{}i_real.txt".format(output, os.sep), 'w') as i_real:
            for i, key in enumerate(peoples.keys()):
                print("{}/enroll_list/{}".format(
                    output.rstrip(os.sep),key), file=i_enroll)
                label_enroll = np.append(label_enroll, i)
                with open("{}{}{}".format(enroll_list, os.sep, key), 'w') as en:
                    for imgname in peoples[key]:
                        if '/enroll/' in imgname.lower():
                            #print(imgname)
                            print("{}{}".format(root,imgname), file=en)
                        else:
                            print("{}{}".format(root,imgname), file=i_real)
                            label_real = np.append(label_real, i)
    
    with open("{}{}labels.txt".format(output, os.sep), 'w') as flabel:
        #for i in range(len(people)):
            #flabel.write(i)
        #flabel.write('\n')
        label_enroll.tofile(flabel, sep=' ')
        print('', file = flabel)
        label_real.tofile(flabel, sep=' ')    