# ballclass.py

from turtle import Turtle, exitonclick

class Ball(Turtle):
    """Round turtle that bounces."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)

    def move(self):
        """Move forward, bouncing against right side."""
        self.forward(5)
        if self.xcor() > 340:
            self.left(180)
            
def main():
    ball = Ball()
    for _ in range(100):
        ball.move()
    exitonclick()

if __name__ == "__main__":
    main()
