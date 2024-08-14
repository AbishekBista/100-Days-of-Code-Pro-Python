def my_function():
    print("Hello")
    print("Hi")

my_function()

def turn_left():
    print("Turns left")

def move():
    print("Moves straight")

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()