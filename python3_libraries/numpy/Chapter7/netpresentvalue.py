from __future__ import print_function
import numpy as np

cashflows = np.random.randint(100, size=5)
cashflows = np.insert(cashflows, 0, -100)
print("Cashflows", cashflows)

print("Net present value", np.npv(0.03, cashflows))
