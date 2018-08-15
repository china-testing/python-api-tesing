#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# CreateDate: 2018-3-31

import argparse
import shutil
import os
import subprocess
import time
import re
from pathlib import Path
import sys
import shutil
import json
import pprint

import numpy as np
import zmail

import data_common
import servers
import count
import others


description = '''

功能：执行比对测试

活体示例：
python3 run_server.py liveness -t batch1.7.5
python3 run_server.py liveness -t batch1.7.6
python3 run_server.py liveness -t base
python3 run_server.py liveness -t bug

gaze示例：
python3 run_server.py gaze -t little -w -b /opt/test_tools/faceunlock_test_general_meil


landmark示例： 
$ python3 run_server.py landmark -d /home/andrew/code/tmp/sensetime -w

比对示例：

$ python3 run_server.py verify -w  -d /home/andrew/code/data/common/verify/china_500 -e jpg
$ python3 run_server.py verify -w -t vivo-verify-100
$ python3 run_server.py verify -w  -d /home/andrew/code/data/common/verify/india_32/ -e yuv

检测示例：

$ python3 run_server.py detect -w -d /home/andrew/code/data/test/检测

睁闭眼示例：

$ python3 run_server.py eyestate -w -d /home/andrew/code/data/common/bug/Eye_state/FACEUNLOCK-1150


测试工具的目录：
活体：/opt/test_tools/faceunlock_test_general_meil
其他：/opt/test_tools/base/faceunlock_test_general_meil，即默认目录。
'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('test_type', action="store", help=u'测试类型')
parser.add_argument('-d', action='store', dest='directory', default=None,
                    help='数据集目录') 
parser.add_argument('-b', action='store', dest='base', 
                    default='/opt/test_tools/release/linux-x86_64',
                    help='比对工具目录, 默认为/opt/test_tools/base/faceunlock_test_general_meil') 
parser.add_argument('-e', action='store', dest='ext', default='',
                    help='文件扩展名，默认为ir')   
parser.add_argument('-r', action='store', dest='recipients', 
                    default='lixiaoxue_vendor@sensetime.com;xurongzhong@sensetime.com',
                    help='邮件接收者')    
parser.add_argument('-s', action='store', dest='score', default=0.99, 
                    type=float, help='分数阀值，默认0.99')   
parser.add_argument('-t', action='store', dest='data_type', default='',
                    help='数据集类型')     
parser.add_argument('-w', action="store_true", default=False, help=u'是否等待结束')
parser.add_argument('-o', action='store', dest='output', default='output',
                    help='输出目录')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0 Rongzhong xu 2018 04 26')
options = parser.parse_args()

types = {
    "verify": {
        'name': 'verify',
        'process': 'sample_verify',        
        'cmd':"nohup ./run -r output/i_enroll.txt output/i_real.txt > {}.log 2>&1 &".format(options.test_type),
        'vivo-verify-100':'/home/andrew/code/data/tof/base_test_data/vivo-verify-100',
        'vivo-verify-452':'/home/andrew/code/data/tof/base_test_data/vivo-verify-452',      
        'vivo-verify-611':'/home/andrew/code/data/tof/base_test_data/vivo-verify-611',
        'little':'/home/andrew/code/data/tof/little_test_data/little_verify', 
        'bug':'/home/andrew/code/data/tof/bug/verify',
        'file_type':'ir',
        },    
    "gaze": {
        'file_type':'ir',
        'name': 'gaze_mn',
        'process': 'sample_gaze_mn',        
        'flag':'/gaze/',
        'cmd':"nohup ./run -f output/files.txt > {}.log 2>&1 &".format(options.test_type),
        #'base':'/home/andrew/code/data/tof/base_test_data/vivo-gaze/20180418_a.m.-gaze',
        'base':'/home/andrew/code/data/tof/base_test_data/vivo-gaze',
        'little':'/home/andrew/code/data/tof/little_test_data/little_gaze', 
        'bug':'/home/andrew/code/data/tof/bug/gaze',
        'nocase':'/home/andrew/code/data/tof/vivo3D_batch_test/gaze_batch/nocase(0423_0430_false2.2)',
        'case':'/home/andrew/code/data/tof/vivo3D_batch_test/gaze_batch/0418_0419_0501_case',
        'demo1.7.8':'/home/andrew/code/data/tof/vivo3D_batch_test/gaze_batch/demo_1.7.8--gaze_2.6.0_ceshi_20180430',
        },
    
    "liveness": {
        'file_type':'ir,depth',
        'name': 'liveness',
        'process': 'sample_liveness',
        'flag':'photo/',
        'cmd': "nohup ./run -l output/files.txt > {}.log 2>&1 &".format(options.test_type),
        'bug':"/home/andrew/code/data/tof/bug/liveness",
        'base':'/home/andrew/code/data/tof/base_test_data/vivo-liveness',
        'batch1.7.5':'/home/andrew/code/data/tof/vivo3D_batch_test/liveness_batch/demo_1.7.5_test',
        'batch1.7.6':'/home/andrew/code/data/tof/vivo3D_batch_test/liveness_batch/demo_1.7.6_test',
        'batch1.7.7':'/home/andrew/code/data/tof/vivo3D_batch_test/demo_1.7.7_test',
        'little':'/home/andrew/code/data/data_set/2d/little/liveness',                
        },   
    
    "detect": {
        'file_type':'ir',
        'name': 'detect',
        'process': 'sample_detect',
        'flag':'photo/',
        'cmd': "nohup ./run -d output/files.txt > {}.log 2>&1 &".format(options.test_type),     
        },
    
    "eyestate": {
        'file_type':'ir',
        'name': 'eyestate',
        'process': 'sample_eyestate',
        'flag':'photo/',
        'cmd': "nohup ./run -e output/files.txt > {}.log 2>&1 &".format(options.test_type),
        },    
    
    "landmark":{
        'file_type':'ir',
        'name': 'detect',
        'process': 'sample_align',
        'flag':'/little_photo/',
        'cmd':"nohup ./run -m output/files.txt > {}.log 2>&1 &".format(options.test_type),
        },
}


tool = options.base    
now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())    
if options.directory is None:
    if not options.data_type:
        print("data_type不能为空")
        exit(1)
    options.directory = types[options.test_type][options.data_type]
    
file_name = "{}{}{}".format(tool, os.sep, "output/files.txt")
label_name = "{}{}{}".format(tool, os.sep, "output/labels.txt")
config_name = "{}{}{}".format(tool, os.sep, "config.json")

data_version = Path(options.directory).name
raw_config = Path(options.directory).parent / "config" / (data_version + ".json")
if raw_config.is_file():
    shutil.copy2(raw_config, config_name)
    
# 检查配置文件，确认模型都存在
d = json.load(open(config_name))
print('\n{}\n'.format(config_name))
print('#'*80)
print('\n')
pprint.pprint(d)

for item in d['model']:
    path = d['model'][item]
    if not Path(options.base.rstrip(os.sep) + os.sep + path).exists():
        print("Path: {} not exist".format(path))       
        sys.exit(0)


if options.ext:
    types[options.test_type]['file_type'] = options.ext    

if options.test_type != 'verify':
    data_common.get_filelistandlabel(
        options.directory,
        types[options.test_type]['flag'],
        filetype=types[options.test_type]['file_type'],
        file_name=file_name,
        label_name=label_name)
else:
    file_name = "{}{}{}".format(tool, os.sep, "output/i_real.txt")
    servers.build_verify_input(options.directory, tool + '/output',
                               filetype=types[options.test_type]['file_type'])

configs = open(config_name).read()

search = re.search('{0}.*?(\d+.\d+.\d+)'.format(types[options.test_type]['name']),
                    configs)
if not search:
    print("Error: Can not find version!")
    exit(1)
version = search.group(1)
print(types[options.test_type]['name'], version)
cmd1 = "cd {}".format(tool)
directory = "{0}{1}result{1}{2}-{3}-{4}-{5}".format(
    tool, os.sep, options.test_type, now, options.data_type, version)
data_common.check_directory(directory)
shutil.copyfile(file_name, 
                "{}{}{}".format(directory, os.sep,os.path.basename(file_name)))
shutil.copyfile(label_name,
                "{}{}{}".format(directory, os.sep,os.path.basename(label_name)))
shutil.copyfile(config_name, 
                "{}{}{}".format(directory, os.sep,os.path.basename(config_name)))

# anlyse result
if options.test_type == 'detect':
    result = "{0}{1}{2}{1}{2}_output%files.txt.txt".format(
    tool, os.sep, options.test_type)
else:
    result = "{0}{1}{2}{1}{2}_output%files.txt.csv".format(
        tool, os.sep, options.test_type)
    
if options.test_type == 'verify':
    result = "{0}{1}{2}{1}{2}_score_output%i_enroll.txt.csv".format(
        tool, os.sep, options.test_type)   
    
if Path(result).exists():
    os.remove(result)

cmd = "{} && {}".format(cmd1,types[options.test_type]['cmd'])
print(cmd)
subprocess.call(cmd,shell=True)

print("Please see result in {}".format(directory))

# wait for result
if not options.w:
    exit(0)

print(result)       
time.sleep(3)
if not Path(result).exists():
    servers.wait_until_stop('sample')

# 如果比对工具有错，直接退出执行。
tool_log = "{}{}{}.log".format(
    options.base.rstrip(os.sep), os.sep,options.test_type)
text = open(tool_log).read()
if 'faceunlock' in text or 'tmp' in text:
    print('\n')
    print("#"*30 + "  ERROR  " + "#"*30)
    print(text)
    sys.exit(1)


new_result = "{0}{1}{2}-result.csv".format(directory, os.sep, version)
print(result)
print(new_result)
time.sleep(1)
shutil.copyfile(result, new_result)
error_name = "{0}{1}{2}----result.xlsx".format(directory, os.sep, version)

if options.test_type == 'detect':
    # 生成图片
    names = data_common.file2list(result,basename=True)
    data_common.output_file('/home/andrew/code/tmp/detection_results.txt', names)
    subprocess.call("cd  /home/andrew/code/tmp/facedet-profile && rm -rf cache",
                    shell=True)    
    subprocess.check_output("cd /home/andrew/code/tmp/facedet-profile  && python3 get_roc.py > {}/log.txt".format(directory), 
                            shell=True)       
    print("copyinig")
    src = "/home/andrew/code/tmp/facedet-profile/roc.png"
    dst = "{}/{}-roc.png".format(directory, version)
    time.sleep(0.5)
    shutil.copyfile(src, dst)

if options.test_type != 'verify':
    values = "{0}{1}{2}-values.csv".format(directory, os.sep, version)
    maps = data_common.concat_file(new_result, file_name, sep=',')
    data_common.output_file(values, maps)    

if options.test_type == 'liveness':
    new_result_ = "{0}{1}{2}-result_.csv".format(directory, os.sep, version)
    shutil.copyfile(result, new_result_)
    cmd = "sed -i  's#-1#1#' {}".format(new_result_)
    subprocess.call(cmd,shell=True)
    time.sleep(3)
     
    if options.data_type == 'base':
        replace = '/home/andrew/code/data/tof/base_test_data/vivo-liveness/'
    else:
        replace = ''
        
    df1, df2, df3, df4 = servers.get_liveness_server_result(
        new_result, file_name, label_name, score=options.score,
        replace=replace, error_name=error_name, type_=options.data_type)

    roc = "{0}{1}{2}-roc.txt".format(directory, os.sep, version)
    fprs = [0.0+0.1*p for p in np.arange(1,10)] 
    count.roc(new_result, label_name, output=roc, fprs=fprs)
   
    t1 = '参数：\n{}\n结果目录：\n{}\n配置文件：\n{}\nROC：\n{}\n'.format(
        " ".join(sys.argv), directory, open(config_name).read(), open(roc).read())
    
    t2 = 'FAR_FRR：\n{}\n分类统计：\n{}'.format(df4.to_string(), df3.to_string())
    
    print("sending email")
    recipients = options.recipients.split(';')
    if others.send_mail(recipients,"活体比对测试结果", t1 + t2, files=[error_name]):
        print("发送成功")

if options.test_type == 'gaze':
    fprs = [0.3,0.25,0.2,0.15,0.1,0.05,0.02,0.01,0.001]
    roc = "{0}{1}{2}-roc.txt".format(directory, os.sep, version)
    count.roc(result, label_name, fprs=fprs, output=roc, ) 
    servers.get_gaze_server_result(new_result, file_name, label_name, 
        error_name=error_name, type_=options.data_type)   
    
if options.test_type == 'eyestate':       
    servers.get_eye_server_result(values, error_name=error_name,)
    
    
if options.test_type == 'verify':
    person_name = "{}{}{}".format(tool, os.sep, "output/i_enroll.txt")
    print(person_name)
    shutil.copyfile(person_name, 
        "{}{}{}".format(directory, os.sep, os.path.basename(person_name)))
    roc = "{0}{1}{2}-roc.txt".format(directory, os.sep, version)
    count.verify_roc(result, label_name, output=roc, ) 
    
    servers.get_verify_server_result(
        person_name, file_name, new_result,
        replace_file=options.directory.rstrip(os.sep) + os.sep,
        replace_name=options.base + '/output/enroll_list/',
        error_name=error_name,
    )    
    


    

