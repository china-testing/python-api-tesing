from __future__ import print_function
import numpy as np

a = np.arange(-4, 4)

print("Remainder", np.remainder(a, 2))
print("Mod", np.mod(a, 2))
print("% operator", a % 2)
print("Fmod", np.fmod(a, 2))
