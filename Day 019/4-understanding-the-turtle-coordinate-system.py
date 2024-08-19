from turtle import Turtle, Screen
import random
screen = Screen()

# set up the width and height of the window
screen.setup(width=500, height=400)

# take input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

is_race_on = False

for color in colors:
    i = colors.index(color)
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, -70 + i * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won the bet")
            else:
                print("You've lost the bet")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)







screen.exitonclick()