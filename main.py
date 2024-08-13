from turtle import Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
from bricks_classes import *
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

def generate_bricks():
    red_bricks = [RedBrick(x) for x in range(-365, 400, 65)]
    yellow_bricks = [YellowBrick(x) for x in range(-365, 400, 65)]
    green_bricks = [GreenBrick(x) for x in range(-365, 400, 65)]
    blue_bricks = [BlueBrick(x) for x in range(-365, 400, 65)]
    bricks = red_bricks + yellow_bricks + green_bricks + blue_bricks
    return bricks

screen.listen()

screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

bricks = generate_bricks()
bricks_broken = 0

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    
    # Detect collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        if (ball.xcor() < paddle.xcor() and ball.x_move > 0) or (ball.xcor() > paddle.xcor() and ball.x_move < 0):
            ball.bounce_x()
        ball.bounce_y()
    
    # Detect if the ball missed the paddle and hit the bottom wall
    if ball.ycor() < -280:
        time.sleep(1)
        ball.reset_position()
        ball.reset_speed()
    
    # Detect collision with bricks
    for brick in bricks:
        # Detect if the ball hits the brick from above or below
        if ball.distance(brick) < 30 and (ball.ycor() > brick.ycor() - 20 or ball.ycor() < brick.ycor() + 20):
            brick.destroy()
            ball.bounce_y()
            bricks.remove(brick)
            bricks_broken += 1
            if bricks_broken % 4 == 0:
                ball.increase_speed()
            scoreboard.increase_score(brick.value)
        
        # Detect if the ball hits the brick from the sides
        elif ball.distance(brick) < 30 and (ball.xcor() > brick.xcor() - 30 or ball.xcor() < brick.xcor() + 30):
            brick.destroy()
            ball.bounce_x()
            bricks.remove(brick)
            bricks_broken += 1
            if bricks_broken % 4 == 0:
                ball.increase_speed()
            scoreboard.increase_score(brick.value)
    
    # Detect if all bricks are destroyed
    if len(bricks) == 0:
        time.sleep(2)
        scoreboard.level_up()
        bricks = generate_bricks()

screen.exitonclick()