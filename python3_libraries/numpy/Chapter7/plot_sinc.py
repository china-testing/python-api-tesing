import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 4, 100)
vals = np.sinc(x)

plt.plot(x, vals)
plt.title('Sinc function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
