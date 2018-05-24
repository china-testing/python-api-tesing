from __future__ import print_function
import numpy as np

A = np.mat("4 11 14;8 7 -2")
print("A\n", A)

U, Sigma, V = np.linalg.svd(A, full_matrices=False)

print("U")
print(U)

print("Sigma")
print(Sigma)

print("V")
print(V)

print("Product\n", U * np.diag(Sigma) * V)
