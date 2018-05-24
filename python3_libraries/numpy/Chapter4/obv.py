from __future__ import print_function
import numpy as np

c, v=np.loadtxt('BHP.csv', delimiter=',', usecols=(6, 7), unpack=True)

change = np.diff(c)
print("Change", change)

signs = np.sign(change)
print("Signs", signs)

pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1])
print("Pieces", pieces)

print("Arrays equal?", np.array_equal(signs, pieces))

print("On balance volume", v[1:] * signs)
