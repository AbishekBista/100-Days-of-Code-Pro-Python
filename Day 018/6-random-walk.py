from turtle import Turtle, Screen
import random
import math

mario = Turtle()
mario.pensize(10)
mario.speed(0)

for _ in range(1000):
    random_r = random.random()
    random_g = random.random()
    random_b = random.random()
    tup = (random_r, random_g, random_b)
    mario.pencolor(tup)
    direction = [0, 90, 180, 270]
    mario.setheading(random.choice(direction))
    mario.forward(30)

screen = Screen()
screen.exitonclick()