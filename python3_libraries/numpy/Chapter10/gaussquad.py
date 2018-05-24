from scipy import integrate
import numpy as np

print "Gaussian integral", np.sqrt(np.pi), integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
