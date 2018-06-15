#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# 技术支持 钉钉群：21745728(可以加钉钉pythontesting邀请加入) 
# qq群：144081101 591302926  567351477
# CreateDate: 2018-6-12 
# balance_table.py
# Print table of account balances earning interest.

def balance(p, r, t):
    """Return new balance using compound annual interest."""
    return p*(1 + r)**t

def main():
    print("Calculates compound interest over time.")
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): "))
    years = int(input("Number of years: "))
    for year in range(years + 1):
        print(year, balance(principal, rate, year))
    
main()
