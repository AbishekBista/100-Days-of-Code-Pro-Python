from turtle import Turtle, Screen

mario = Turtle()

def move_forward():
    mario.forward(20)

def move_backward():
    mario.backward(20)

def turn_left():
    mario.left(45)

def turn_right():
    mario.right(45)

def reset():
    mario.reset()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()