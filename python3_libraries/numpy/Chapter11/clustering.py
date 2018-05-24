import numpy as np
import sklearn.cluster
import pygame, sys
from pygame.locals import *

np.random.seed(42)
positions = np.random.randint(0, 400, size=(30, 2))

positions_norms = np.sum(positions ** 2, axis=1)
S = - positions_norms[:, np.newaxis] - positions_norms[np.newaxis, :] + 2 * np.dot(positions, positions.T)

aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
labels = aff_pro.labels_

polygon_points = []

for i in xrange(max(labels) + 1):
   polygon_points.append([])


# Sorting points by cluster
for label, position in zip(labels, positions):
   polygon_points[label].append(position)

pygame.init()
screen = pygame.display.set_mode((400, 400))


while True: 
   for point in polygon_points:
      pygame.draw.polygon(screen, (255, 0, 0), point)

   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   pygame.display.update()
