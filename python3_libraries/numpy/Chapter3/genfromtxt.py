import numpy as np

data = np.eye(2)
print(data)
np.savetxt("eye.txt", data)
print(np.genfromtxt("eye.txt"))
