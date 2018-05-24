#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153
# CreateDate: 2018-04-12

import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates ndarray attributes.
#
# Run from the commandline with 
#
#  python arrayattributes2.py
b = np.arange(24).reshape(2, 12)
print("In: b")
print(b)
#Out: 
#array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])

print("In: b.ndim")
print(b.ndim)
#Out: 2

print("In: b.size")
print(b.size)
#Out: 24

print("In: b.itemsize")
print(b.itemsize)
#Out: 8

print("In: b.nbytes")
print(b.nbytes)
#Out: 192

print("In: b.size * b.itemsize")
print(b.size * b.itemsize)
#Out: 192

print("In: b.resize(6,4)")
print(b.resize(6,4))

print("In: b")
print(b)
#Out: 
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11],
#       [12, 13, 14, 15],
#       [16, 17, 18, 19],
#       [20, 21, 22, 23]])

print("In: b.T")
print(b.T)
#Out: 
#array([[ 0,  4,  8, 12, 16, 20],
#       [ 1,  5,  9, 13, 17, 21],
#       [ 2,  6, 10, 14, 18, 22],
#       [ 3,  7, 11, 15, 19, 23]])

print("In: b.ndim")
print(b.ndim)
#Out: 1

print("In: b.T")
print(b.T)
#Out: array([0, 1, 2, 3, 4])


print("In: b = array([1.j + 1, 2.j + 3])")
b = np.array([1.j + 1, 2.j + 3])

print("In: b")
print(b)
#Out: array([ 1.+1.j,  3.+2.j])

print("In: b.real")
print(b.real)
#Out: array([ 1.,  3.])

print("In: b.imag")
print(b.imag)
#Out: array([ 1.,  2.])

print("In: b.dtype")
print(b.dtype)
#Out: dtype('complex128')

print("In: b.dtype.str")
print(b.dtype.str)
#Out: '<c16'


print("In: b = arange(4).reshape(2,2)")
b = np.arange(4).reshape(2,2)

print("In: b")
print(b)
#Out: 
#array([[0, 1],
#       [2, 3]])

print("In: f = b.flat")
f = b.flat

print("In: f")
print(f)
#Out: <numpy.flatiter object at 0x103013e00>

print("In: for it in f: print it")
for it in f: 
   print(it)
#0
#1
#2
#3

print("In: b.flat[2]")
print(b.flat[2])
#Out: 2


print("In: b.flat[[1,3]]")
print(b.flat[[1,3]])
#Out: array([1, 3])


print("In: b")
print(b)
#Out: 
#array([[7, 7],
#       [7, 7]])

print("In: b.flat[[1,3]] = 1")
b.flat[[1,3]] = 1

print("In: b")
print(b)
#Out: 
#array([[7, 1],
#       [7, 1]])

