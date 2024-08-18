from turtle import Turtle, Screen
from random import random
import math

mario = Turtle()

for i in range(3, 11):
    random_r = random()
    random_g = random()
    random_b = random()
    tup = (random_r, random_g, random_b)
    mario.pencolor(tup)
    for j in range(i):
        mario.forward(100)
        mario.left(360/i)



screen = Screen()
screen.exitonclick()