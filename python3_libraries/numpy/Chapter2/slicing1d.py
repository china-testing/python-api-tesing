import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates one dimensional arrays slicing.
#
# Run from the commandline with 
#
#  python slicing1d.py

print("In: a = arange(9)")
a = np.arange(9)

print("In: a[3:7]")
print(a[3:7])
#Out: array([3, 4, 5, 6])

print("In: a[:7:2]")
print(a[:7:2])
#Out: array([0, 2, 4, 6])

print("In: a[::-1]")
print(a[::-1])
#Out: array([8, 7, 6, 5, 4, 3, 2, 1, 0])

print("In: s = slice(3,7,2)")
s = slice(3,7,2)
print("In: a[s]")
print(a[s])
#Out: array([3, 5])


print("In: s = slice(None, None, -1)")
s = slice(None, None, -1)

print("In: a[s]")
print(a[s])
#Out: array([8, 7, 6, 5, 4, 3, 2, 1, 0])

