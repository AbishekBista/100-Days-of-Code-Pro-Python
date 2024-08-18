from turtle import Turtle, Screen

mario = Turtle()
mario.shape("turtle")
mario.color("red")
mario.forward(100)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()