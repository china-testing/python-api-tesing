from __future__ import print_function
import numpy as np

print("Pass", np.testing.assert_array_less([0, 0.123456789, np.nan], [1, 0.23456780, np.nan]))
print("Fail", np.testing.assert_array_less([0, 0.123456789, np.nan], [0, 0.123456780, np.nan]))
