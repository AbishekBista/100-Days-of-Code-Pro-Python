from turtle import Turtle, Screen

mario = Turtle()

for _ in range(4):
    mario.forward(100)
    mario.right(90)



screen = Screen()
screen.exitonclick()