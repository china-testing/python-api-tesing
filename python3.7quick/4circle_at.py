# circle_at.py
# Use a function to draw circles

from turtle import *

def circle_at(x, y, r):
    """Draw circle with center (x, y) radius r."""
    penup()
    goto(x, y - r)
    pendown()
    setheading(0)
    circle(r)

circle_at(-200, 0, 20)
begin_fill()
circle_at(0, 0, 100)
end_fill()
circle_at(200, 0, 20)
hideturtle()
exitonclick()
