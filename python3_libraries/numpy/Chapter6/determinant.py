from __future__ import print_function
import numpy as np

A = np.mat("3 4;5 6")
print("A\n", A)

print("Determinant", np.linalg.det(A))
