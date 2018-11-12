# face.py
# Draw a face using functions.

from turtle import *

def circle_at(x, y, r):
    """Draw circle with center (x, y) radius r."""
    penup()
    goto(x, y - r)
    pendown()
    setheading(0)
    circle(r)

def eye(x, y, radius):
    """Draw an eye centered at (x, y) of given radius."""
    circle_at(x, y, radius)
    
def face(x, y, width):
    """Draw face centered at (x, y) of given width."""
    circle_at(x, y, width/2)
    eye(x - width/6, y + width/5, width/12)
    eye(x + width/6, y + width/5, width/12)
    
def main():
    face(0, 0, 100)
    face(-140, 160, 200)
    exitonclick()
        
main()
