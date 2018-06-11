# spiral.py
# Draw spiral shapes

from turtle import *

def spiral(firststep, angle, gap):
    """Move turtle on a spiral path."""
    step = firststep
    while step > 0:
        forward(step)
        left(angle)
        step -= gap

def main():
    spiral(100, 71, 2)
    exitonclick()

main()
