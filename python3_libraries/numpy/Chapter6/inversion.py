from __future__ import print_function
import numpy as np

A = np.mat("0 1 2;1 0 3;4 -3 8")
print("A\n", A)

inverse = np.linalg.inv(A)
print("inverse of A\n", inverse)

print("Check\n", A * inverse)
