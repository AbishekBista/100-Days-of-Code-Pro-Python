from turtle import Turtle, Screen

mario = Turtle()


def move_forward():
    mario.forward(10)

screen = Screen()
screen.listen()

screen.onkey(key="space", fun=move_forward)
screen.exitonclick()