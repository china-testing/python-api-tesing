# randomwalk.py
# Draw path of a random walk.

from turtle import *
from random import randrange

def random_move(distance):
    """Take random step on a grid."""
    left(randrange(0, 360, 90))
    forward(distance)
    
def main():
    speed(0)
    while abs(xcor()) < 200 and abs(ycor()) < 200:
        random_move(10)
    exitonclick()
    
main()
