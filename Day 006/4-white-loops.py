def turn_left():
    print("Turns left")

def move():
    print("Moves straight")
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def at_goal():
    return False


while not at_goal():
    jump()