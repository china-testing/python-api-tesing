from __future__ import print_function
import numpy as np

print("Significance 8", np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=8))
print("Significance 9", np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=9))
