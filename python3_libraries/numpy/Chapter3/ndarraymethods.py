from __future__ import print_function
import numpy as np

a = np.arange(5)
print("a =", a)
print("Clipped", a.clip(1, 2))

a = np.arange(4)
print(a)
print("Compressed", a.compress(a > 2))

b = np.arange(1, 9)
print("b =", b)
print("Factorial", b.prod())

print("Factorials", b.cumprod())
