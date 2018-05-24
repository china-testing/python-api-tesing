from __future__ import print_function
import numpy as np

A = np.mat('1 2 3; 4 5 6; 7 8 9')
print("Creation from string", A)
print("transpose A", A.T)
print("Inverse A", A.I)
print("Check Inverse", A * A.I)

print("Creation from array", np.mat(np.arange(9).reshape(3, 3)))
