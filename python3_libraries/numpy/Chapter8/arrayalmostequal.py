from __future__ import print_function
import numpy as np

print("Decimal 8", np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=8))
print("Decimal 9", np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=9))
