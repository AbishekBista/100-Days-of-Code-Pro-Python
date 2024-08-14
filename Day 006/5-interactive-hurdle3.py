def turn_left():
    print("Turns left")

def move():
    print("Moves straight")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def at_goal():
    return True

def wall_in_front():
    return True

def front_is_clear():
    return True


while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

