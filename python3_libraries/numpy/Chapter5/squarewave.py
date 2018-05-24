import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, 99)
k = 2 * k - 1
f = np.zeros_like(t)

for i, ti in enumerate(t):
   f[i] = np.sum(np.sin(k * ti)/k)

f = (4 / np.pi) * f

plt.plot(t, f)
plt.title('Square wave')
plt.grid()
plt.show()
