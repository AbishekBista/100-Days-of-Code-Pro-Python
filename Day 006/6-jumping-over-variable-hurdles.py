def turn_left():
    print("Turns left")

def move():
    print("Moves straight")

def at_goal():
    return True

def wall_in_front():
    return True

def front_is_clear():
    return True

def wall_on_right():
    return True


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    # prepare to go up
    turn_left()
    while wall_on_right():
        move()
    
    # prepare to move one to the side
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

