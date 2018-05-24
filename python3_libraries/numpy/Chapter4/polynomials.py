from __future__ import print_function
import numpy as np
import sys
import matplotlib.pyplot as plt


bhp=np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)

vale=np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)

t = np.arange(len(bhp))
poly = np.polyfit(t, bhp - vale, 3)
print("Polynomial fit", poly)

print("Next value", np.polyval(poly, t[-1] + 1))

print("Roots", np.roots(poly))

der = np.polyder(poly)
print("Derivative", der)

print("Extremas", np.roots(der))
vals = np.polyval(poly, t)
print(np.argmax(vals))
print(np.argmin(vals))

plt.plot(t, bhp - vale, label='BHP - VALE')
plt.plot(t, vals, '--', label='Fit')
plt.title('Polynomial fit')
plt.xlabel('Days')
plt.ylabel('Difference ($)')
plt.grid()
plt.legend()
plt.show()
