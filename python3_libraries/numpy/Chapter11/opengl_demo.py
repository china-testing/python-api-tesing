import pygame
from pygame.locals import *
import numpy as np
     
from OpenGL.GL import *
from OpenGL.GLU import *

def display_openGL(w, h):
  pygame.display.set_mode((w,h), pygame.OPENGL|pygame.DOUBLEBUF)

  glClearColor(0.0, 0.0, 0.0, 1.0)
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

  gluOrtho2D(0, w, 0, h)


def main():
    pygame.init()
    pygame.display.set_caption('OpenGL Demo')
    DIM = 400
    display_openGL(DIM, DIM)
    glColor3f(1.0, 0, 0)
    vertices = np.array([[0, 0], [DIM/2, DIM], [DIM, 0]])
    NPOINTS = 9000
    indices = np.random.random_integers(0, 2, NPOINTS)
    point = [175.0, 150.0]

    for i in xrange(NPOINTS):
       glBegin(GL_POINTS)
       point = (point + vertices[indices[i]])/2.0
       glVertex2fv(point)
       glEnd()

    glFlush()
    pygame.display.flip()
     
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

    
if __name__ == '__main__':
  main()
