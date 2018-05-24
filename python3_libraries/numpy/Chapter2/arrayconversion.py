import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy record data type.
#
# Run from the commandline with 
#
#  python3 arrayconversion.py
b = np.array([ 1.+1.j,  3.+2.j])
print("In: b")
print(b)
#Out: array([ 1.+1.j,  3.+2.j])

print("In: b.tolist()")
print(b.tolist())
#Out: [(1+1j), (3+2j)]

print("In: b.tostring()")
print(b.tostring())
#Out: '\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00@'

print("In: fromstring(b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00@', dtype=complex)")
print(np.fromstring(b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00@', dtype=complex))
#Out: array([ 1.+1.j,  3.+2.j]

print("In: fromstring('20:42:52',sep=':', dtype=int)")
print(np.fromstring('20:42:52',sep=':', dtype=int))
#Out: array([20, 42, 52])

print("In: b")
print(b)
#Out: array([ 1.+1.j,  3.+2.j])

print("In: b.astype(int)")
print(b.astype(int))
#/usr/local/bin/ipython:1: ComplexWarning: Casting complex values to real discards the imaginary part
#  #!/usr/bin/python
#Out: array([1, 3])

print("In: b.astype('complex')")
print(b.astype('complex'))
#Out: array([ 1.+1.j,  3.+2.j])

