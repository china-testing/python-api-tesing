# ball.py

from turtle import Turtle, exitonclick

def main():
    """Bouncing ball."""
    ball = Turtle()
    ball.shape("circle")
    ball.penup()
    ball.speed(0)
    for _ in range(100):
        ball.forward(5)
        if ball.xcor() > 340:
            ball.left(180)
    exitonclick()

main()
