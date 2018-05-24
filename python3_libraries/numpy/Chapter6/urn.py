from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


points = np.zeros(100)
np.random.seed(16)
outcomes = np.random.hypergeometric(25, 1, 3, size=len(points))

for i in range(len(points)):
   if outcomes[i] == 3:
      points[i] = points[i - 1] + 1
   elif outcomes[i] == 2:
      points[i] = points[i - 1] - 6
   else:
      print(outcomes[i])

plt.plot(np.arange(len(points)), points)
plt.title('Game show simulation')
plt.xlabel('# Rounds')
plt.ylabel('Score')
plt.grid()
plt.show()
