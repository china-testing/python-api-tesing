import numpy as np
import matplotlib.pyplot as plt


window = np.hamming(42)
plt.plot(window)
plt.title('Hamming window')
plt.ylabel('Weight')
plt.grid()
plt.show()
