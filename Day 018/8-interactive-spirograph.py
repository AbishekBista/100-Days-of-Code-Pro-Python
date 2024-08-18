import turtle as t
import random

t.colormode(255)
mario = t.Turtle()

mario.speed(0)
mario.pensize(2)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circle(gap_size):
    for i in range(int(360/gap_size)):
        mario.pencolor(generate_random_color())
        mario.circle(100)
        mario.setheading(mario.heading() + gap_size)

draw_circle(7)

screen = t.Screen()
screen.exitonclick()