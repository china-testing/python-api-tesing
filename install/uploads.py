#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-1
# uploads.py

'''
photos=# select * from nodes;
 id |          name           |        up        | leaf |       creation_date        
----+-------------------------+------------------+------+----------------------------
  1 | faceunlock              |                  | f    | 2018-03-01 14:28:54.9825
  2 | detect                  | faceunlock       | f    | 2018-03-01 14:28:54.983293
  3 | detect_base             | detect           | f    | 2018-03-01 14:28:54.983691
  4 | vivo-doublechannel      | detect_base      | t    | 2018-03-01 14:28:54.984131
  5 | detect_version          | detect           | t    | 2018-03-01 14:28:54.984565
  6 | liveness                | faceunlock       | f    | 2018-03-01 14:28:54.984957
  7 | liveness_base           | liveness         | t    | 2018-03-01 14:28:54.985394
  8 | liveness_version        | detect_base      | f    | 2018-03-01 14:28:54.985762
  9 | snpe                    | liveness_version | t    | 2018-03-01 14:28:54.986084
 10 | dnn                     | liveness_version | t    | 2018-03-01 14:28:54.98634
 11 | 2pd                     | liveness_version | t    | 2018-03-01 14:28:54.986653
 12 | ocl                     | liveness_version | t    | 2018-03-01 14:28:54.986975
 13 | verify                  | faceunlock       | f    | 2018-03-01 14:28:54.98722
 14 | verify_version          | verify           | t    | 2018-03-01 14:28:54.987473
 15 | verify_base             | verify           | f    | 2018-03-01 14:28:54.987696
 16 | verify_common           | verify_base      | f    | 2018-03-01 14:28:54.987918
 17 | verify_common500enroll1 | verify_common    | t    | 2018-03-01 14:28:54.988143
 18 | verify_common500enroll5 | verify_common    | t    | 2018-03-01 14:28:54.988367
 19 | verify_common_india     | verify_common    | t    | 2018-03-01 14:28:54.988589
 20 | verify_vivo2            | verify_base      | f    | 2018-03-01 14:28:54.98881
 21 | verify_vivo2_500enroll1 | verify_common    | t    | 2018-03-01 14:28:54.989034
 22 | verify_vivo2_500enroll5 | verify_common    | t    | 2018-03-01 14:28:54.989257
 23 | verify_vivo_tof         | verify_base      | t    | 2018-03-01 14:28:54.989523
 24 | verify_oppo3d           | verify_base      | t    | 2018-03-01 14:28:54.989748
 25 | Ocular                  | faceunlock       | f    | 2018-03-01 14:28:54.989974
 26 | Ocular_base1500         | Ocular           | t    | 2018-03-01 14:28:54.990205
 27 | Ocular_version          | Ocular           | t    | 2018-03-01 14:28:54.99045

photos=# select * from owners;
 id | name |       creation_date        
----+------+----------------------------
  1 | test | 2018-03-01 14:28:54.981124

'''

import json
import glob
import os

import requests
from pyseaweed import WeedFS

owner = 1
node = 5
input_ = r"D:\sensetime\user\result"
file_type = "jpg"

w = WeedFS("172.20.15.200", 9333) # weed-fs master address and port
server = "http://172.20.15.200:5000/api/Photos"

for filename in glob.glob("{}{}*.{}".format(input_, os.sep, file_type)):    
    
    fid = w.upload_file(filename) # path to file
    file_url = w.get_file_url(fid)
    
    payload = {'url': file_url, 'owner': owner, 'node':node}
    r = requests.post(server, data=json.dumps(payload))
    
    print(r.text)







    