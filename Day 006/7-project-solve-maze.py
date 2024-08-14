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

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()

turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move() 
    elif front_is_clear():
        move()
    else:
        turn_left()