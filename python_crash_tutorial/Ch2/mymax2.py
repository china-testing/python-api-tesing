#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-12 
# mymax2.py
# Write max function without built-in max().

def mymax2(x, y):
    """Return larger of x and y."""
    largest_so_far = x
    if y > largest_so_far:
        largest_so_far = y
    return largest_so_far
    
def main():
    print("MyMax: Enter two values to find the larger.")
    first = float(input("First value: "))
    second = float(input("Second value: "))
    print("The larger value is", mymax2(first, second))
    
main()
