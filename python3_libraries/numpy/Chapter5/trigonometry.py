import numpy as np
from pylab import *

x = np.linspace(-np.pi, np.pi, 2001)
sines = np.sin(x)
hist(np.arctanh(np.clip(sines, -0.999, 0.999)), bins=40)
show()
