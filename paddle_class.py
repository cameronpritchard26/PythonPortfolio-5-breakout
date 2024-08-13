from turtle import Turtle

class Paddle(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto((0, -250))

    def move_left(self) -> None:
        self.setx(self.xcor() - 20)
        if self.xcor() < -300:
            self.setx(-300)

    def move_right(self) -> None:
        self.setx(self.xcor() + 20)
        if self.xcor() > 300:
            self.setx(300)