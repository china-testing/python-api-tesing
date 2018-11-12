#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-25
# factorial.py

def factorial(n):
    """Return n! = 1*2*3*...*n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    for n in range(20):
        print(n, factorial(n))
    print(factorial(2000))

main()
