import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the selection
# of ndarray elements.
#
# Run from the commandline with 
#
#  python elementselection.py
a = np.array([[1,2],[3,4]])

print("In: a")
print(a)
#Out: 
#array([[1, 2],
#       [3, 4]])

print("In: a[0,0]")
print(a[0,0])
#Out: 1

print("In: a[0,1]")
print(a[0,1])
#Out: 2

print("In: a[1,0]")
print(a[1,0])
#Out: 3

print("In: a[1,1]")
print(a[1,1])
#Out: 4 

