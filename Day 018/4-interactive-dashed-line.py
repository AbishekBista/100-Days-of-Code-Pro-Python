from turtle import Turtle, Screen

mario = Turtle()

for _ in range(15):
    mario.forward(10)
    mario.penup()
    mario.forward(10)
    mario.pendown()



screen = Screen()

screen.exitonclick()