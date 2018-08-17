#/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-15
# photos.py

import os
import traceback

import cv2
import numpy as np
from PIL import Image, ImageDraw

def mark_image(filename, dst, poses, angle=None, relative=False):
    '''
    files： 文件列表
    dst： 目的文件目录
    poses: 为颜色跟对应的坐标(left, top, right,  bottom)。 
    比如{"green":(1,1,99,100)}
    '''
    colors = {'blue': (255,0,0), 'green': (0,255,0), 'red': (0,0,255),}
    image = cv2.imread(filename)
    for color in poses:
        print(poses[color])
        left = left2 = int(poses[color][0])
        top = top2 = int(poses[color][1])
        right = right2 = int(poses[color][2])
        bottom = bottom2 = int(poses[color][3])
        
        if relative:
            right = left + right
            right2 = left + right
            bottom = top + bottom
            bottom2 = top + bottom
                   
        if angle == 'left':
            left2 = top
            right2 = bottom
            top2 = 400 - right
            bottom2 = 400 - left
            
        if angle == 'right':
            left2 = 640 - bottom
            right2 = 640 - top
            top2 = left
            bottom2 = right     
            
        if angle == None:
            left2 = left
            right2 = right
            top2 = top
            bottom2 = bottom      
        
            
        print((left2, top2), (right2, bottom2))    
        print(left2, top2, right2, bottom2, end=' ') 
        print()
        cv2.rectangle(image,(left2, top2), (right2, bottom2), colors[color], 1)
    cv2.imwrite(dst, image)

def mark_images(files, out,shenzhens, beijings):
    for filename in files:
        name = os.path.basename(filename)
        sz = shenzhens.get(name)
        bj = beijings.get(name)  
        bj_sz_photo_compare(sz,bj,filename,prefix=out)

def bj_sz_photo_compare(sz,bj,filename,prefix="_"):
    poses = {}
    if sz:
        poses["green"] = sz
        print("shenzhen:",sz)
    else:
        print("shenzhen: Can not recognize!",)
    if bj:
        poses["red"] = bj
        print("beijing:",bj)
    else:
        print("beijing: Can not recognize!",)
    name = os.path.basename(filename)
    if type(name) == bytes:
        name = name.decode()   
    new_name = "{}{}".format(prefix,name)
    print("Please see {}".format(new_name))
    mark_image(filename,new_name,poses)    
 
def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def rotate(files, dst, value=90):
    for file_ in files:
        img = Image.open(file_)
        img = img.rotate(value, expand=True)
        name = "{}{}{}".format(dst, os.sep, os.path.basename(file_))
        img.save(name)
        
def rotate2(files, dst, value=90):
    for file_ in files:
        img = cv2.imread(file_,0)
        result = rotateImage(img, value)
        cv2.imwrite("{}{}{}".format(dst, os.sep, os.path.basename(file_)), 
                    result) 

def find_face(filename, rotate=None, model=None):
    img = cv2.imread(filename, 0)
    if rotate:
        img = rotateImage(img, rotate)
    if model:
        return face_recognition.face_locations(img,model=model)  
    else:
        return face_recognition.face_locations(img)  
    
def raw2jpg(filename, height=400, width=640):
    try:
        img = np.fromfile(filename, dtype=np.uint16)
        img = img.reshape( (height, width) )
        img.astype(np.float)
        img = np.sqrt(img)
        img = img * (255 / img.max())
        #img.astype(np.uint8)
        cv2.imwrite(filename+'.jpg', img)
    except Exception as info:
        print('Error: {}'.format(filename))
        print(info)
        traceback.print_exc()
        return False

    return True    

def split_raw(filename):
    img = np.fromfile(filename, dtype=np.uint16)
    print(filename)
    size = int(img.shape[0])
    ir = img[0:int(size/2)]
    ir.tofile(r"{}.ir".format(filename))  
    depth = img[int(size/2):]
    depth.tofile(r"{}.depth".format(filename))         
    
