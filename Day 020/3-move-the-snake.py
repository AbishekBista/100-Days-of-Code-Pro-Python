from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Naagin')

# turns off the tracer
screen.tracer(0)

segments = []

for i in range(3):
    block = Turtle(shape="square")
    block.color("white")
    block.penup()
    block.goto(-20 * i, 0)
    segments.append(block)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].forward(20)



       

screen.exitonclick()