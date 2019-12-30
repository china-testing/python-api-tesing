#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29


def binary_search(items, item):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

l = list(range(1,100,3))

print(binary_search(l, 31)) 
print(binary_search(l, 30)) 