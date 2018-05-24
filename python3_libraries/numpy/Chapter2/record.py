import numpy as np

# Chapter 2 Beginning with NumPy fundamentals
#
# Demonstrates the NumPy record data type.
#
# Run from the commandline with 
#
#  python record.py
print("In: t = dtype([('name', numpy.str_, 40), ('numitems', numpy.int32), ('price', numpy.float32)])")
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
print(t)
#Out: dtype([('name', '|S40'), ('numitems', '<i4'), ('price', '<f4')])

print("In: t['name']")
print(t['name'])
#Out: dtype('|S40')


print("In: itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)")
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)


print("In: itemz[1]")
print(itemz[1])
#Out: ('Butter', 13, 2.7200000286102295)

