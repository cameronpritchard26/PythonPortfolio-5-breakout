from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
    
    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self) -> None:
        self.y_move *= -1
    
    def bounce_x(self) -> None:
        self.x_move *= -1

    def reset_position(self) -> None:
        self.goto(0, -200)
        self.bounce_x()
        self.bounce_y()
    
    def increase_speed(self) -> None:
        self.ball_speed *= 0.9
    
    def reset_speed(self) -> None:
        self.ball_speed = 0.1