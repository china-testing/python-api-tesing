import numpy as np
import matplotlib.pyplot as plt


window = np.bartlett(42)
plt.plot(window)
plt.title('Bartlett window')
plt.ylabel('Weight')
plt.grid()
plt.show()
