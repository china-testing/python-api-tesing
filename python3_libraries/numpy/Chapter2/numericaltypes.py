import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy numerical types
#  and conversion between them.
#
# Run from the commandline with 
#
#  python numericaltypes.py

print("In: float64(42)")
print(np.float64(42))
#Out: 42.0

print("In: int8(42.0)")
print(np.int8(42.0))
#Out: 42

print("In: bool(42)")
print(np.bool(42))
#Out: True
print(np.bool(0))

print("In: bool(42.0)")
print(np.bool(42.0))
#Out: True

print("In: float(True)")
print(np.float(True))
#Out: 1.0
print(np.float(False))

print("In: arange(7, dtype=uint16)")
print(np.arange(7, dtype=np.uint16))
#Out: array([0, 1, 2, 3, 4, 5, 6], dtype=uint16)


print("In: int(42.0 + 1.j)")
try:
   print(np.int(42.0 + 1.j))
except TypeError:
   print("TypeError")
#Type error

print("In: float(42.0 + 1.j)")
print(float(42.0 + 1.j))
#Type error
