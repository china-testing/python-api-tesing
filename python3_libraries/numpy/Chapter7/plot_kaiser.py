import numpy as np
import matplotlib.pyplot as plt


window = np.kaiser(42, 14)
plt.plot(window)
plt.title('Kaiser window')
plt.ylabel('Weight')
plt.grid()
plt.show()
