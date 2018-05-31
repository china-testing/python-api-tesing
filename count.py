#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# data_common.py
import multiprocessing
import os

import bisect
import numpy as np
from sklearn.metrics import roc_curve
from data_common import output_file

def compute_roc_part(worker_id, scores, label_enroll, label_real, thres, tp, fp, total_pos_neg):
    labels = (label_enroll.reshape(-1,1) == label_real.reshape(1,-1)).astype(np.int).reshape(-1)
    scores = scores.reshape(-1)
    sorted_idx = np.argsort(scores)
    sorted_scores = scores[sorted_idx]
    sorted_labels = labels[sorted_idx]
    cum_pos = np.cumsum(sorted_labels, dtype=float)
    total_pos = cum_pos[-1]
    n = labels.size
    fn = cum_pos - sorted_labels
    tp_tmp = total_pos - fn
    fp_tmp = np.arange(n, 0, -1) - tp_tmp
    c_tp = [0]*len(thres)
    c_fp = [0]*len(thres)
    start = 0
    for i, th in enumerate(thres):
        #'Find rightmost value less than or equal to x'
        pos = bisect.bisect_right(sorted_scores, th, start)
        if pos != len(sorted_scores):
            c_tp[i] = tp_tmp[pos]
            c_fp[i] = fp_tmp[pos]
            start = pos
        else:
            c_tp[i] = total_pos
            c_fp[i] = 0
    total_pos_neg[worker_id] = np.array([total_pos, n - total_pos])
    tp[worker_id] = c_tp
    fp[worker_id] = c_fp

def roc(score,label, fprs=np.arange(0.05, 0, -0.01), output='output/roc.txt'):
    scores_ori = np.loadtxt(score, dtype=np.float32, delimiter='\n')
    labels_ori = np.loadtxt(label, dtype=np.int32, delimiter='\n')
    assert(len(scores_ori) == len(labels_ori))
    
    scores = scores_ori[scores_ori >= 0]
    labels = labels_ori[scores_ori >= 0]

    roc_fpr, roc_tpr, roc_thresholds = roc_curve(
        labels, scores, pos_label=1, drop_intermediate=False)
    
    tpr_k_score = []
    th_k_score = []
    for fpr_ratio in fprs:
        idx = np.argmin(np.abs(roc_fpr - fpr_ratio))
        tpr = roc_tpr[idx]
        th = roc_thresholds[idx]
        tpr_k_score.append(tpr)
        th_k_score.append(th)
    with open(output, 'w') as f:
        print("total_num: {}".format(len(scores_ori)),file=f)
        print("valid_num: {}".format( len(scores)),file=f)        
        print("fpr    | "+" | ".join('{:.3f}'.format(i) for i in fprs),file=f)
        print("|".join("  :-:  " for i in range(len(fprs)+1)),file=f)
        print("tpr(%) | "+" | ".join('{:.2f}'.format(i*100) for i in tpr_k_score),file=f)
        print("thres  | "+" | ".join('{:.3f}'.format(i) for i in th_k_score),file=f)
        
        scores_ori = np.loadtxt(score, dtype=np.float32, delimiter='\n')
        labels_ori = np.loadtxt(label, dtype=np.int32, delimiter='\n')
        assert(len(scores_ori) == len(labels_ori))
        
        scores = scores_ori[scores_ori >= 0]
        labels = labels_ori[scores_ori >= 0]
    
        roc_fpr, roc_tpr, roc_thresholds = roc_curve(
            labels, scores, pos_label=1, drop_intermediate=False)
        
        fprs = np.arange(0.05, 0, -0.01)
        tpr_k_score = []
        th_k_score = []
        for fpr_ratio in fprs:
            idx = np.argmin(np.abs(roc_fpr - fpr_ratio))
            tpr = roc_tpr[idx]
            th = roc_thresholds[idx]
            tpr_k_score.append(tpr)
            th_k_score.append(th)
        with open(output, 'w') as f:
            print("total_num: {}".format(len(scores_ori)),file=f)
            print("valid_num: {}".format( len(scores)),file=f)        
            print("fpr    | "+" | ".join('{:.3f}'.format(i) for i in fprs),file=f)
            print("|".join("  :-:  " for i in range(len(fprs)+1)),file=f)
            print("tpr(%) | "+" | ".join('{:.2f}'.format(i*100) for i in tpr_k_score),file=f)
            print("thres  | "+" | ".join('{:.3f}'.format(i) for i in th_k_score),file=f)        
        

def verify_roc(score,label,output='output/roc.txt'):
    print(score)
    print(label)
    fprs = [10**(-p) for p in np.arange(1, 7, 1.)]
    with open(label, 'r') as f:
        lines = f.readlines()
        #assert(len(lines) == 2)
        label_enroll = np.fromstring(lines[0].strip(), sep=' ')
        label_real = np.fromstring(lines[1].strip(), sep=' ')
    
    score = np.loadtxt(score, dtype=np.float32, delimiter=',')
    assert(score.shape[0] == len(label_enroll))
    assert(score.shape[1] == len(label_real))
    
    max_step = 2000
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    thres = np.arange(0, 1, 1e-3)
    total_num = (label_real.shape[0]-1)//max_step+1
    mgr = multiprocessing.Manager()
    tp = mgr.list(range(total_num))
    fp = mgr.list(range(total_num))
    total_pos_neg = mgr.list(range(total_num))
    worker_id = 0
    for beg_j in range(0, label_real.shape[0], max_step):
        end_j = min(beg_j + max_step, label_real.shape[0])
        label_real_part = label_real[beg_j:end_j]
        score_part = score[:, beg_j:end_j]
        pool.apply_async(compute_roc_part, args=(worker_id, score_part, label_enroll, label_real_part, thres, tp, fp, total_pos_neg))
        worker_id += 1
    pool.close()
    pool.join()
    tp = np.sum(tp, axis=0)
    fp = np.sum(fp, axis=0)
    total_pos_neg = np.sum(total_pos_neg, axis=0)
    tpr = tp/total_pos_neg[0]
    fpr = fp/total_pos_neg[1]
    csvnp = np.array([thres, 1-tpr, fpr]).T
    np.savetxt(os.path.dirname(output) + os.sep + 'tmp.csv', csvnp, fmt='%.4f,%1.4e,%1.4e')
    tpr_k_score = []
    th_k_score = []
    for fp in fprs:
        idx = np.argmin(np.abs(fpr-fp))
        tpr_k_score.append(tpr[idx])
        th_k_score.append(thres[idx])
    with open(output, 'w') as f:
        print("fpr    | "+" | ".join(format(i, '.0e') for i in fprs),file=f)
        print("|".join("  :-:  " for i in range(len(fprs)+1)),file=f)
        print("tpr(%) | "+" | ".join('{:.2f}'.format(i*100) for i in tpr_k_score),file=f)
        print("thres  | "+" | ".join('{:.3f}'.format(i) for i in th_k_score),file=f)   
