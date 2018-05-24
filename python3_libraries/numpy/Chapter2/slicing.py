import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates multi dimensional arrays slicing.
#
# Run from the commandline with 
#
#  python slicing.py
print("In: b = arange(24).reshape(2,3,4)")
b = np.arange(24).reshape(2,3,4)

print("In: b.shape")
print(b.shape)
#Out: (2, 3, 4)

print("In: b")
print(b)
#Out: 
#array([[[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],
#
#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])


print("In: b[0,0,0]")
print(b[0,0,0])
#Out: 0


print("In: b[:,0,0]")
print(b[:,0,0])
#Out: array([ 0, 12])

print("In: b[0]")
print(b[0])
#Out: 
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])


print("In: b[0, :, :]")
print(b[0, :, :])
#Out: 
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])

print("In: b[0, ...]")
print(b[0, ...])
#Out: 
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])


print("In: b[0,1]")
print(b[0,1])
#Out: array([4, 5, 6, 7])


print("In: b[0,1,::2]")
print(b[0,1,::2])
#Out: array([4, 6])


print("In: b[...,1]")
print(b[...,1])
#Out: 
#array([[ 1,  5,  9],
#       [13, 17, 21]])

print("In: b[:,1]")
print(b[:,1])
#Out: 
#array([[ 4,  5,  6,  7],
#       [16, 17, 18, 19]])

print("In: b[0,:,1]")
print(b[0,:,1])
#Out: array([1, 5, 9])

print("In: b[0,:,-1]")
print(b[0,:,-1])
#Out: array([ 3,  7, 11])

print("In: b[0,::-1, -1]")
print(b[0,::-1, -1])
#Out: array([11,  7,  3])

print("In: b[0,::2,-1]")
print(b[0,::2,-1])
#Out: array([ 3, 11])

print("In: b[::-1]")
print(b[::-1])
#Out: 
#array([[[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]],
#
#       [[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]]])


print("In: s = slice(None, None, -1)")
s = slice(None, None, -1)
print("In: b[(s, s, s)]")
print(b[(s, s, s)])
#Out: 
#array([[[23, 22, 21, 20],
#        [19, 18, 17, 16],
#        [15, 14, 13, 12]],
#
#       [[11, 10,  9,  8],
#        [ 7,  6,  5,  4],
#        [ 3,  2,  1,  0]]])

