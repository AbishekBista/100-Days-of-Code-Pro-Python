from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

line = Turtle()
line.color('white')
line.hideturtle()
line.setheading(90)

line.penup()
line.goto(0, -300)
for _ in range(30):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()
    

paddle_1 = Paddle([(-380, -20),(-380, 0), (-380, 20)])
paddle_2 = Paddle([(370, -20), (370, 0), (370, 20)])

ball = Ball()

score = Score()

# paddle 1 control
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(ball.release_ball, "d")

# paddle 2 control
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")
screen.onkey(ball.release_ball, "Left")

screen.onkey(ball.reset_ball, "space")

is_game_over = False

while not is_game_over:
    ball_in_play = True

    while ball_in_play:
        screen.update()
        time.sleep(0.05)
        if ball.ball_released:
            ball.move()

            # Deflection past the upper and lower walls, bounces the ball
            if ball.ycor() > 290 or ball.ycor() < -290:
                ball.bounce()

            # Deflection with the paddle
            for parts in paddle_1.paddle:
                if parts.distance(ball) < 15:        
                    ball.bounce_on_paddle()
            
            for parts in paddle_2.paddle:
                if parts.distance(ball) < 15:
                    ball.bounce_on_paddle()

            # Deflection past the left and right wall stops the game
            if ball.xcor() > 380:
                score.increase_paddle_1_score()
                ball.is_paddle_1_turn = not ball.is_paddle_1_turn
                score.refresh_score()
                ball.ball_released = False
                if score.score_1 == 2:
                    print("This should break now")
                    ball_in_play = False

            elif ball.xcor() < -380:
                score.increase_paddle_2_score()
                ball.is_paddle_1_turn = not ball.is_paddle_1_turn
                score.refresh_score()
                ball.ball_released = False
                if score.score_2 == 2:
                    print("This should break now 2")
                    ball_in_play = False

    is_game_over = True
    
    score.show_game_over()
    

        

screen.exitonclick()