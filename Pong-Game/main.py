
from turtle import Screen, Turtle
import time 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Manually update the screen
    ball.move()      # Move the ball

    #detecting collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detecting collision with r_paddle   
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    #detect R paddle misses the ball 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L paddle misses the ball 
    if ball.xcor() < -380:
        ball.reset_position() 
        scoreboard.r_point()

    
screen.exitonclick()