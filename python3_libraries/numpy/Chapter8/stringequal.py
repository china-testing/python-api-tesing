from __future__ import print_function
import numpy as np

print("Pass", np.testing.assert_string_equal("NumPy", "NumPy"))
print("Fail", np.testing.assert_string_equal("NumPy", "Numpy"))
