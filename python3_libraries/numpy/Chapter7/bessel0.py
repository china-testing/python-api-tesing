import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 4, 100)
vals = np.i0(x)

plt.plot(x, vals)
plt.title('Modified Bessel function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
