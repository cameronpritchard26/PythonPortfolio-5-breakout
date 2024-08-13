from turtle import Turtle

class RedBrick(Turtle):

    Y_POSITION = 240

    def __init__(self, x_pos) -> None:
        super().__init__()
        self.value = 10
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.goto((x_pos, RedBrick.Y_POSITION))
    
    def destroy(self) -> None:
        self.hideturtle()
        del self

class YellowBrick(Turtle):

    Y_POSITION = 205

    def __init__(self, x_pos) -> None:
        super().__init__()
        self.value = 5
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.goto((x_pos, YellowBrick.Y_POSITION))
    
    def destroy(self) -> None:
        self.hideturtle()
        del self

class GreenBrick(Turtle):

    Y_POSITION = 170

    def __init__(self, x_pos) -> None:
        super().__init__()
        self.value = 2
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.goto((x_pos, GreenBrick.Y_POSITION))
    
    def destroy(self) -> None:
        self.hideturtle()
        del self

class BlueBrick(Turtle):

    Y_POSITION = 135

    def __init__(self, x_pos) -> None:
        super().__init__()
        self.value = 1
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.goto((x_pos, BlueBrick.Y_POSITION))
    
    def destroy(self) -> None:
        self.hideturtle()
        del self