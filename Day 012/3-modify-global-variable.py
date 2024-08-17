enemies = 1

def increase_enemies():
    # enemies = 2 # creates a new variable with local scope instead of modifying the global variable

    # global enemies # nice workaround but not good practise, instead return the modified value and assign it to the global variable
    
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")