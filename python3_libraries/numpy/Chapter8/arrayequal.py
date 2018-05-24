from __future__ import print_function
import numpy as np

print("Pass", np.testing.assert_allclose([0, 0.123456789, np.nan], [0, 0.123456780, np.nan], rtol=1e-7, atol=0))
print("Fail", np.testing.assert_array_equal([0, 0.123456789, np.nan], [0, 0.123456780, np.nan]))
