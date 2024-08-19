from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Naagin')



for i in range(3):
    block = Turtle(shape="square")
    block.color("white")
    block.penup()
    block.goto(-20 * i, 0)

screen.exitonclick()