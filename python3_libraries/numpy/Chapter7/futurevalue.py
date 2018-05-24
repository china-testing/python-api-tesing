from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


print("Future value", np.fv(0.03/4, 5 * 4, -10, -1000))

fvals = []

for i in xrange(1, 10):
   fvals.append(np.fv(.03/4, i * 4, -10, -1000))

plt.plot(range(1, 10), fvals, 'bo')
plt.title('Future value, 3 % interest,\n Quarterly payment of 10')
plt.xlabel('Saving periods in years')
plt.ylabel('Future value')
plt.grid()
plt.legend(loc='best')
plt.show()
