import turtle as t
import random

colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
screen = t.Screen()
t.colormode(255)
mario = t.Turtle()

mario.penup()
mario.hideturtle()
mario.setposition(-200, -200)
mario.speed(0)

def draw_row():
    for _ in range(10):
        mario.pendown()
        mario.dot(20, random.choice(colors))
        mario.penup()
        mario.forward(50)

for _ in range(10):
    draw_row()
    mario.backward(10 * 50)
    mario.setheading(90)
    mario.forward(50)
    mario.setheading(0)

mario.hideturtle()




screen.exitonclick()