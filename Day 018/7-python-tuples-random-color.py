from turtle import Turtle, Screen
import random
import math
import turtle as t

t.colormode(255)

mario = Turtle()
mario.pensize(10)
mario.speed(0)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(1000):
    mario.pencolor(generate_random_color())
    direction = [0, 90, 180, 270]
    mario.setheading(random.choice(direction))
    mario.forward(30)

screen = Screen()
screen.exitonclick()