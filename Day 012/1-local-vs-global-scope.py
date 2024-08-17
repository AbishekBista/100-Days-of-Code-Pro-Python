enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

player_health = 100
# Local scope
def drink_potion():
    potion_strength = 2 # has local scope
    print(potion_strength)
    print(player_health) # has global scope

drink_potion()
# print(potion_strength)