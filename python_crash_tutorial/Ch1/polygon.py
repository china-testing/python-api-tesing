# polygon.py
# Draw regular polygons

from turtle import *

def polygon(n, length):
    """Draw n-sided polygon with given side length."""
    for _ in range(n):
        forward(length)
        left(360/n)
        
def main():
    """Draw polygons with 3-9 sides."""
    for n in range(3, 10):
        polygon(n, 80)
    exitonclick()
    
main()
