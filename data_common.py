#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# data_common.py

import os
import shutil
import traceback
import time
from pathlib import Path
import glob
import hashlib
import re
import collections

import pandas

maps = {
    1: ("白天-室内-正常光-非走动-720的7人间的中间位置", "白天-室内-正常光"),
    2: ("白天-室内-正常光-非走动-路演区第4排(低)中间位置", "白天-室内-正常光"),
    3: ("白天-室内-正常光-非走动-海翔通往荔园路的楼下通道门口", "白天-室内-正常光"),
    4: ("白天-室内-正常光-非走动-701健身区域", "白天-室内-正常光"),
    5: ("白天-室内-正常光-非走动-电梯间内", "白天-室内-正常光"),
    6: ("白天-室内-正常光-走动-七楼楼道", "白天-室内-正常光"),
    7: ("白天-室内-正常光-走动-717办公室", "白天-室内-正常光"),
    8: ("白天-室内-正常光-动作-平躺", "白天-室内-正常光"),
    9: ("白天-室内-正常光-动作-侧躺", "白天-室内-正常光"),
    10: ("白天-室内-暗光-非走动-720办公室4人间关灯后", "白天-室内-暗光"),
    11: ("白天-室内-逆光-非走动-路演区窗口逆光", "白天-室内-逆光"),
    12: ("白天-室内-逆光-非走动-717办公室过道顶灯光", "白天-室内-逆光"),
    13: ("白天-室内-逆光-非走动-厕所头顶灯光", "白天-室内-逆光"),
    14: ("白天-室内-逆光-非走动-701健身区域", "白天-室内-逆光"),
    15: ("白天-室内-逆光-走动-路演区窗口逆光", "白天-室内-逆光"),
    16: ("白天-室内-逆光-走动-717办公室过道顶灯光", "白天-室内-逆光"),
    17: ("白天-室内-逆光-走动-厕所头顶灯光", "白天-室内-逆光"),
    18: ("白天-室外-正常光-非走动-海翔楼下空旷处（品骏快递）（背阴处正常光）",
         "白天-室外-正常光"),
    19: ("白天-室外-正常光-非走动-荔园路树荫下", "白天-室外-正常光"),
    20: ("白天-室外-正常光-走动-海翔楼下空旷处（品骏快递）（背阴处正常光）",
         "白天-室外-正常光"),
    21: ("白天-室外-正常光-走动-荔园路树荫下", "白天-室外-正常光"),
    22: ("白天-室外-逆光-非走动-海翔楼下空旷处 (品骏快递)(建议中午左右)（背对太阳）",
         "白天-室外-逆光"),
    23: ("白天-室外-逆光-非走动-荔园路树荫下（建议中午左右）（背对太阳）",
         "白天-室外-逆光"),
    24: ("白天-室外-逆光-非走动-（阴天）海翔通往荔园路的楼下通道门口（人物背对门口）",
         "白天-室外-逆光"),
    25: ("白天-室外-逆光-非走动-（阴天）手机朝上，背朝天空", "白天-室外-逆光"),
    26: ("白天-室外-逆光-走动-海翔楼下空旷处（品骏快递）（建议中午左右)（背对太阳）",
         "白天-室外-逆光"),
    27: ("白天-室外-逆光-走动-荔园路树荫下（建议中午左右）（背对太阳）",
         "白天-室外-逆光"),
    28: ("白天-室外-逆光-走动-（阴天）手机朝上，背朝天空", "白天-室外-逆光"),
    29: ("白天-室外-强光-非走动-海翔楼下空旷处（建议中午左右）（面对太阳）",
         "白天-室外-强光"),
    30: ("白天-室外-强光-非走动-荔园路树荫下（面对太阳）", "白天-室外-强光"),
    31: ("白天-室外-强光-走动-海翔楼下空旷处（建议中午左右）（面对太阳）",
         "白天-室外-强光"),
    32: ("白天-室外-强光-走动-荔园路树荫下（面对太阳）", "白天-室外-强光"),
    33: ("白天-室内-正常光-表情", "白天-室内-正常光-表情"),
    34: ("白天-室内-正常光-不戴眼镜注册，戴近视眼镜认证", "白天-室内-正常光-脸"),
    35: ("白天-室内-正常光-不戴眼镜注册，戴墨镜认证", "白天-室内-正常光-脸"),
    36: ("白天-室内-正常光-戴近视眼镜注册，不戴眼镜认证", "白天-室内-正常光-脸"),
    37: ("白天-室内-正常光-戴近视眼镜注册，戴墨镜认证", "白天-室内-正常光-脸"),
    38: ("晚上-室内-正常光-夜晚路演区沙发位置", "晚上室内正常光"),
    39: ("晚上-室内-正常光-七楼过道", "晚上室内正常光"),
    40: ("晚上-室内-正常光-701健身区域", "晚上室内正常光"),
    41: ("晚上-室内-正常光-平躺（路演区域沙发位置）", "晚上室内正常光"),
    42: ("晚上-室内-正常光-侧躺（路演区域沙发位置）", "晚上室内正常光"),
    43: ("晚上-室内-暗光-夜晚路演区沙发位置（19：00左右关灯）", "晚上室内暗光"),
    44: ("晚上-室内-暗光-7楼710的客梯间（关灯后）", "晚上室内暗光"),
    45: ("晚上-室内-暗光-720的4人间关灯后", "晚上室内暗光"),
    46: ("晚上-室内-暗光-平躺（720的4人间关灯后）", "晚上室内暗光"),
    47: ("晚上-室内-暗光-侧躺（720的4人间关灯后）", "晚上室内暗光"),
    48: ("晚上-室外-暗光-海翔楼下空旷处（品骏快递）（人物背景无灯光）",
         "晚上室外暗光"),
    49: ("晚上-室外-暗光-海翔楼下上坡处路灯下（广州银行）", "晚上室外暗光"),
    50: ("晚上-室外-强光-海翔楼下上坡处路灯下（广州银行）（面朝路灯）",
         "晚上室外强光"),
}


def count(datas, values):
    '''
    生成统计的用例
    '''
    total_number = compare_number = live_number = success_number = \
        test_number = 0
    print(datas)

    for row in datas:
        print(row)
        num, case_name, total, compare, live, success, test, r1, r2, r3 = row
        if num in values:
            total_number += total
            compare_number += compare
            live_number += live
            success_number += success
            test_number += test

    return ["====", maps[values[0]][0], total_number, compare_number,
            live_number, success_number, test_number, 
            percentage(compare_number, total_number), 
            percentage(live_number, total_number), 
            percentage(success_number, test_number)]


def file2html(name):
    result = ''
    for line in open(name):
        result += line + "<br>"  
    return result

def percentage(number1, number2):
    value  = 0 if number2 == 0 else float(number1) / number2
    value = 0 if not value else "{0:.5f}%".format(value * 100)   
    return value

def produce_xls(results, output, number, type_=0):
    
    if type_ ==0:
        tag = old_tag = None
        values = []
        title = ["用例编号", "测试用例", "重试总次数", "比对成功次数", "活体成功次数",
                 "成功次数", "测试次数", "比对通过率", "活体通过率", "用户通过率"]
    else:
        title = ["用例编号", "重试总次数", "比对成功次数", "活体成功次数", 
                 "睁闭眼通过次数","成功次数", "测试次数", "比对通过率", "活体通过率",
                 "用户通过率", "睁闭眼通过率"]
        
    datas = [title, ]

    for i in range(1, number + 1):

        total_number = compare_number = live_number = eye_number = \
            success_number = test_number = 0
        if type_ ==0:
            old_tag = tag
            tag = maps[i][1]

            # 用例标签与上一用例不一致时，需要对前面用例进行汇总
            if (old_tag is not None) and values and old_tag != tag:
                datas.append(count(datas, values))
                values = []
            values.append(i)

        # 没有数据的生成空表,有数据则统计
        if i not in results:
            if type_ ==0:
                datas.append([i, maps[i][1], 0, 0, 0, 0, 0, 0, 0, 0, ])
            else:
                datas.append([i, 0, 0, 0, 0, 0, 0, 0, 0, 0,0])
        else:
            for row in results[i]:
                if type_ == 0:
                    print(row)
                    total, compare, live, success, test = row
                else:
                    total, compare, live, eye, success, test = row
                    
                total_number += total
                compare_number += compare
                live_number += live
                success_number += success
                test_number += test
                if type_ != 0:
                    eye_number += eye
                
            if type_ == 0:
                result = [i, maps[i][0], total_number, compare_number, 
                          live_number,success_number, test_number]
            else:
                result =  [i, total_number, compare_number, live_number,
                           eye_number, success_number, test_number,]
            
            result.append(percentage(compare_number, total_number))
            result.append(percentage(live_number, total_number))
            result.append(percentage(success_number, test_number))
            if type_ != 0:
                result.append(percentage(eye_number, total_number))            

            datas.append(result)                

        # 最后的用例需要进行汇总
        if type_ ==0:
            if i == len(maps):
                datas.append(count(datas, values))
                values = []

    try:
        writer = pandas.ExcelWriter(output)
        df = pandas.DataFrame(datas)
        df.to_excel(writer, sheet_name='output', index=False)
        writer.save()
    except IOError:
        print("please close the output file!")


def check_directory(name):
    if Path(name).exists():
        print("{0} Exists，Now Delete it!".format(name))
        try:
            shutil.rmtree(name)
            time.sleep(0.5)
        except Exception as info:
            print('Error: shutil.rmtree {}'.format(name))
            print(info)
            traceback.print_exc()
            print('Please close file and directories and continue...')

    print("mkdir {0} .".format(name))
    Path(name).mkdir(parents=True, exist_ok=True)
    
def get_labels(files, real):
    labels = []
    for file_ in files:
        if real in file_:
            labels.append(1)
        else:
            labels.append(0)    
    return labels
    
def get_filelistandlabel(src, real, filetype="ir",file_name='output/files.txt', 
    label_name='output/label.txt'):
    types = filetype.split(",")
    # print(src)
    if len(types)>1:
        filetype = types[0]
    # print(src, filetype)
    files = find_files_by_type(src,filetype)
    # print(files)
    files.sort()  
    if len(types)==2:
        files2 = find_files_by_type(src,types[1])
        files2.sort()
        files = concat_list(files, files2, sep=' ')
    labels = get_labels(files, real)      
    output_file(file_name, files)
    output_file(label_name, labels)
        

def find_files_by_type(src, filetype="ir"):
    p = Path(src)
    #print(str(p))
    files = []
    for file_name in p.glob('**/*.{0}'.format(filetype)):    
        files.append(str(file_name))
    return files

def copy_files_by_types(src, dst, types="csv,py",
                        directories=None, one_directory=True):
    '''
    拷贝指定扩展名的文件从源目录src到目的目录dst。
    directories: 是否指定目录，多个目录用逗号分隔。
    one_directory：是否拷贝到一个目录，选择为False会建立目录层次。

    示例：

    copy_files_by_types(r"d:\tmp", r"d:\tmp2", types="csv,py",
        directories=None, one_directory=False)

    copy_files_by_types(r"d:\tmp", r"d:\tmp2", types="csv,py,pdf",
        one_directory=False, directories="back,test")
    '''

    check_directory(dst)

    p = Path(src)
    for file_ext in types.split(','):
        for file_name in p.glob('**/*.{0}'.format(file_ext)):
            # print(file_name)

            if directories is not None:
                flag = False
                for directory in directories.split(','):
                    if os.sep + directory + os.sep in str(file_name):
                        flag = True
                if not flag:
                    continue

            if not one_directory:

                dirname = str(file_name.parent).replace(src, dst)
                dst_filename = "{}{}{}".format(
                    dirname, os.sep, file_name.name)

                if not Path(dirname).exists():
                    print("mkdir {}".format(dirname))
                    Path(dirname).mkdir(parents=True, exist_ok=True)
            else:
                dst_filename = "{}{}{}".format(
                    dst, os.sep, Path(file_name).name)

            print("Copying {} to {}".format(file_name, dst_filename))
            shutil.copyfile(str(file_name), dst_filename)
            

def count_number_by_filetypes(directory, file_types, output=False):
    '''
    统计用户目录directory的用例目录下的指定类型文件的个数。
    可以指定多种文件类型。
    output为True时会在屏幕输出。
    比如：count_number_by_filetypes(r'd:\tmp3',"jpg,pdf", output=True)
    '''
    datas = {}
    for file_ext in file_types.split(','):
        datas[file_ext] = count_number_by_filetype(directory, file_ext, output)
    return datas

def count_number_by_filetype(directory, file_type, output=False):
    '''
    统计用户目录directory的用例目录下的指定类型文件的个数。
    output为True时会在屏幕输出。
    比如：count_number_by_filetypes(r'd:\tmp3',"jpg", output=True)
    '''    
    datas = {}
    dirs = glob.glob("{0}/*/".format(directory))
    
    if output:
        print('\n', file_type, ':\n')
    
    for dir_ in (dirs):
        files = glob.glob("{0}/*.{1}".format(dir_, file_type))
        datas[int(dir_.split(os.sep)[-2].lstrip('0'))] = len(files)         
    
    for seq in range(1,len(maps) + 1):         
        if seq not in datas:
            datas[seq] = 0
        if output:
            print(datas[seq])
            
    return datas    

def concat_excel(files, usecols=None, index_col=None, strips={}):
    all_data_frames = []
    for file_name in files:
        df = pandas.read_excel(file_name, index_col=index_col, usecols=usecols)
        all_data_frames.append(df)
    df = pandas.concat(all_data_frames, ignore_index=True)
    if strips:
        for item in strips:
            df[item] = df[item].str.replace(strips[item], "")
    return df


def file2dict(filename, change=False, multi=False, basename=False, sep='\s'):
    result = {}
    for line in open(filename):
        if line.strip():   
            if change:
                value, key = line.split(sep)
            else:
                key, value = line.split(sep)
            key = key.strip()
            value = value.strip()
            if basename:
                key = os.path.basename(key)            
            if multi:   
                if key not in result:
                    result[key] = []
                result[key].append(value)
            else:
                result[key] = value
    return result

def file2dict1(filename, value=-1, basename=False):
    '''
    输入文件只有一列，从该列提取一个字段做key。
    '''
    result = collections.OrderedDict()
    for line in open(filename):
        item = line.strip()
        if not item:
            continue
        key = item.split('/')[value]
        if basename:
            item = os.path.basename(item)
        result[key] = item
    return result

def get_md5(content, is_file=False):
    if is_file:
        return hashlib.md5(open(content,'rb').read()).hexdigest()
    else:
        return hashlib.md5(content).hexdigest()

def merge_excel(df1, df2, key,fixes=None,columns=None,sorts=None):
    """
    key: 能区分行的列名
    fixes： 不需要相加的列，默认为None
    columns： 需要输出的列，默认为None，输出所有列
    sorts： 排序
    """

    df1.fillna(method='ffill',inplace=True)
    df2.fillna(method='ffill',inplace=True)   
    columns1 = set(df1.columns)
    columns2 = set(df2.columns)  
    for item in columns2 - columns1:
        df1[item] = 0
    for item in columns1 - columns2:
        df2[item] = 0        
    key1 = list(df1[key])
    key2 = list(df2[key])
    df = df1.iloc[0:0]
    
    for item in set(key1)|set(key2):
        if item in set(key1)&set(key2):
            value = df1.iloc[key1.index(item)] + df2.iloc[key2.index(item)]
            value[key] = df1.iloc[key1.index(item)][key]
            for name in fixes:
                value[name] = df1.iloc[key1.index(item)][name]
        elif item in set(df1[key]):
            value = df1.iloc[key1.index(item)]
        else:
            value = df2.iloc[key2.index(item)]    
        df = pandas.concat([df, value.to_frame().T]) 
    
    if sorts:
        df = df.sort_values(by=sorts)
    if sorts:
        df = df.loc[:,columns]      
    return df

def output_file(name, items):
    '''输出列表为文本文件'''
    f = open(name,'w')
    for item in items:
        f.write("{}\n".format(item))
    f.close()

def get_filename(items):
    '''将列名中的文件字符串只保留文件名'''
    return [ os.path.basename(x.strip()) for x in items]  

def get_filename_without_ext(items, full=False):
    '''将列名中的文件字符串只保留文件名'''
    if full:
        return [ os.path.splitext(x.strip())[0] for x in items]  
    else:
        return [ os.path.basename(x.strip()).split('.')[0] for x in items]  

def get_shuangtong_photos(diretory):
    results = {}
    base_human = r'{}{}human_test'.format(diretory, os.sep)
    base_paper = r'{}{}paper'.format(diretory, os.sep)
    base_noface = r'{}{}noface'.format(diretory, os.sep)
    
    human_photos = get_filename(glob.glob('{}{}*.*'.format(base_human,os.sep)))
    human_photos = get_filename(human_photos)
    paper_photos = get_filename(glob.glob('{}{}*.*'.format(base_paper,os.sep)))
    paper_photos = get_filename(paper_photos)
    noface_photos = get_filename(glob.glob('{}{}*.*'.format(base_noface,os.sep)))
    noface_photos = get_filename(noface_photos)    
    results['human_test'] = human_photos
    results['paper'] = paper_photos
    results['noface'] = noface_photos
    return results

def get_bj_results(filename,return_dict=False):
    names=['name','left','top','length','height','v','score']
    df = pandas.read_csv(filename, names=names, sep='\s', engine='python')
    rename = lambda x: os.path.basename(x)
    df['name'] = df['name'].apply(rename)    
    if return_dict:
        results = {}
        for num in range(len(df)):
            row =  df.iloc[num]
            results[row['name']] = (
                row['left'],row['top'],row['left'] + row['length'],
                row['top'] + row['height']) 
        return results
    else:
        return df
    
def rename_shuangtong(name):
    names = name.split('/')
    if 'noface' in name:
        filename = "double/{}/{}".format(names[-2],names[-1])      
    else:
        filename = "{}{}/{}".format(
            "20180228_双通人脸检测_zhourong/Image/33941/双通活体检测全集数据/",
            names[-2],names[-1])
    return filename    
    
def get_sz_shuangtong_results(
    filenames,shuangtong_photos, output_file=False,
    out_filename="/home/andrew/code/detection_results.txt"):
    
    print(filenames)
    cols = [0,3,6]
    df_paper = pandas.read_excel(filenames['paper'],usecols=cols) 
    df_human = pandas.read_excel(filenames['human_test'],usecols=cols) 
    #df_noface = pandas.read_excel(filenames['noface'],usecols=cols) 
    df = pandas.concat([df_paper, df_human])
    df['图片的路径'] = df['图片的路径'].apply(rename_shuangtong)
    print(df["人脸检测时间"].mean())
    
    if output_file:
        # 生成北京需要的测试结果        
        detection_results = ""
        for num in range(len(df)):
            row =  df.iloc[num]
            name = row['图片的路径']
            result = row['测试结果']
            # left, top, right,  bottom
            #if os.path.basename(name) in shuangtong_photos['noface']:
                #if result != '未检测到人脸':
                    #detection_result = "{0}\n".format(name)                
                    ##detection_results = detection_results +  detection_result   
                #else:
                    #print("Error: Find face in {}".format(os.path.basename(name)))
                
            #else:
            if result != '未检测到人脸':
                sore = float(result.split(':')[-1].strip())
                temps = result.split('[')
                left, top = temps[1].strip(']').split(',')
                right,  bottom = temps[2].split(']')[0].split(',')  
                detection_result = "{0} {1} {2} {3} {4} 1 {5} \n".format(
                name,left, top, int(right) - int(left),  int(bottom) - int(top), sore)
                detection_results = detection_results +  detection_result
            else:
                detection_result = "{0}\n".format(name)                
                #detection_results = detection_results +  detection_result
             
        f = open(out_filename, 'wb')
        f.write(detection_results.encode(encoding='utf_8', errors='strict'))
        f.close()   
    else:
        return df

def get_result_filelist(directoy):
    '''获取深圳的XLS结果文件列表'''
    p = Path(directoy)
    files = p.glob('**/*.{0}'.format("xls"))   
    xls_files = {}
    for filename in files:
        version = re.search('v\d+\.\d+\.\d+',str(filename)).group()
        if version not in xls_files:
            xls_files[version] = {}        
        if "双通" in str(filename):         
            if "paper" in str(filename):           
                xls_files[version]['paper'] = str(filename)
            elif "human" in str(filename):
                xls_files[version]['human_test'] = str(filename)
            else:
                xls_files[version]['noface'] = str(filename)
        else:
            xls_files[version]['tongyong'] = str(filename)
    return xls_files

def file2list(filename,basename=False):
    result = []
    for line in open(filename):
        item = line.strip()
        if item:
            if basename:
                item = os.path.basename(item)
            result.append(item)
    return result

def concat_list(list1, list2, sep=','):
    result = []
    for i in range(len(list1)):
        try:
            result.append("{}{}{}".format(list1[i], sep, list2[i]))  
        except Exception as info:
            print('Error: concat_list')
            print(i)
            print(len(list1), len(list2))
            #print(list1)
            #print(list2)
            if len(list1) > i:
                print(list1[i])
            else:
                print(list2[i])
            print(info)
            traceback.print_exc()
            continue

            
    return result


def concat_file(file1, file2, sep=','):
    list1 = file2list(file1)
    list2 = file2list(file2)
    result = concat_list(list1, list2, sep)
    return result

def check_pair_file(src, type1, type2, flag=False):
    print("directory: {}".format(src))
    files1 = find_files_by_type(src, type1)
    print("{}: {}".format(type1, len(files1)))
    files1_name = get_filename_without_ext(files1, full=True) 
    files2 = find_files_by_type(src, type2)
    print("{}: {}".format(type2, len(files2)))
    files2_name = get_filename_without_ext(files2, full=True) 
    print(set(files1_name)^set(files2_name))
    for name in set(files1_name)^set(files2_name):
        #print(name)
        if name in files1_name:
            location = files1[files1_name.index(name)]
        else:
            location = files2[files2_name.index(name)]
        print(location)
        if flag:
            print("--remove {}".format(location))
            os.remove(location)

def get_leaf_directories(input_directory):
    results = set()
    for root, dirs, files in os.walk(input_directory):
        if files:
            results.add(root)
    return results    
    
def get_compare_reulst(files, server_file, key, out, server_columns, output_columns):
    '''
    data_common.get_compare_reulst(['_little_photo.xls','_little_real.xls'],
         'liveness_little.csv',  '活体分数', 'dataframe.xlsx',
        ["server_score", "filename", "depth_file_name"], 
        ['活体分数','server_score','diff_score'])
        
    data_common.get_compare_reulst('verify.xls',
        server_result_file, '最高相似度', 
        'dataframe.xlsx',
        ["server_score", "name","filename"], 
        ['最高相似度','server_score','diff_score'])
     
    data_common.get_compare_reulst(['gaze.xls', 'no_gaze.xls'],
        server_result_path + '\gaze_little.csv',  '注视分数', 
        'dataframe.xlsx',
        ["server_score", "filename"], 
        ['注视分数','server_score','diff_score'])       
    '''
    if type(files) is list:
        df = concat_excel(files)
    else:
        df = pandas.read_excel(files)
    df.index = df[u'识别图片的路径'].apply(
        lambda x:os.path.basename(x.split()[0]))
    
    df_server = pandas.read_csv(server_file, sep='\s', names=server_columns)
    df_server.index = df_server['filename'].apply(
        lambda x:os.path.basename(x.split()[0]))
    print(df.index)
    print(df_server.index)
    df['server_score'] = df_server['server_score']
    df['diff_score'] = df['server_score'] - df[key]

    df.to_excel(out, columns=output_columns)    
    

if __name__ == '__main__':
    src = '/home/andrew/code/data/tof/vivo3D_batch_test/liveness/demo_1.7.5_test'
    files = find_files_by_type(src)
    print(files)