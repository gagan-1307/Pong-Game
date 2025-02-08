import turtle,time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# creating snake and screen
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor('black')
screen.tracer(0)  # Turn off automatic screen updates


paddle1=Paddle(450)
paddle2=Paddle(-450)    
screen.listen()
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")


ball=Ball()
score=Scoreboard()
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor()>330 or ball.ycor()<-330:
        ball.bounce_y()
        
    if ball.distance(paddle1) < 50 and ball.xcor() > 420 or ball.distance(paddle2) < 50 and ball.xcor() < -420:
        ball.bounce_x()
        
    if ball.xcor() > 480:
        ball.reset_position()
        score.l_score()
        
    if ball.xcor() < -480:
        ball.reset_position()
        score.r_score()
    
screen.exitonclick()