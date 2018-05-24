import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

while True: 
   sysFont = pygame.font.SysFont("None", 19)
   rendered = sysFont.render('Hello World', 0, (255, 100, 100))
   screen.blit(rendered, (100, 100))

   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   pygame.display.update()
