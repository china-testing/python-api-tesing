from __future__ import print_function
import numpy as np

print("Decimal 6", np.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=7))
print("Decimal 7", np.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=8))
