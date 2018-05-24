import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy 
# dtype.byteorder and dtype.itemsize
#
# Run from the commandline with 
#
#  python dtypeattributes.py


print("In: a = array([[1,2],[3,4]])")
a = np.array([[1,2],[3,4]])

print("In: a.dtype.byteorder")
print(a.dtype.byteorder)
#Out: '='

print("In: a.dtype.itemsize")
print(a.dtype.itemsize)
#Out: 8


