from __future__ import print_function
import numpy as np

a = np.arange(5)
indices = np.searchsorted(a, [-2, 7])
print("Indices", indices)

print("The full array", np.insert(a, indices, [-2, 7]))
