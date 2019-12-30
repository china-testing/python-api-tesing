#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29

def find_smallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i     
  return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))