# bounce.py
# Bounce the turtle.

from turtle import *

def move(distance):
    """Move forward, reversing direction at right side."""
    forward(distance)
    if xcor() > 320:
        setheading(180)

def main():
    shape("circle")
    penup()
    speed(0)
    for _ in range(100):
        move(10)
    exitonclick()
    
main()
