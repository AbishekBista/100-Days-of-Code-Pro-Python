from turtle import Turtle
import random

STARTING_BALL_POSITION = (-355, 0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_released = False
        self.ltr = True
        self.is_paddle_1_turn = True
        self.create_ball()
    
    def create_ball(self):
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.setposition(STARTING_BALL_POSITION)

    def release_ball(self):
        self.setheading(315)
        self.ball_released = True

    def move(self):
        self.forward(10)

    def bounce(self):
        if self.ltr:
            if self.ycor() >= 290:
                self.setheading(315)
            elif self.ycor() <= -290:
                self.setheading(45)
        else:
            if self.ycor() >= 290:
                self.setheading(225)
            elif self.ycor() <= -290:
                self.setheading(135)

    def bounce_on_paddle(self):
        self.ltr = not self.ltr
        
        if not self.ltr:
            self.setheading(random.choice([135, 225]))
        else:
            self.setheading(random.choice([45, 315]))

    def reset_ball(self):
        if not self.ball_released:
            if self.is_paddle_1_turn:
                self.setposition(-355, 0)
            else:
                self.setposition(355, 0)
            
        
        



