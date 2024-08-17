from game_data import data
from art import logo, vs
import random
from os import system

def format_description(data):
    """A function that takes a dictionary and formats it in proper format"""
    name = data["name"]
    description = data["description"].lower()
    country = data["country"]
    return f"{name}, a {description}, from {country}."

def is_correct(choice, option_a, option_b):
    """A function that takes an dictionary and returns the correct option with the highest follower count"""
    if option_a["follower_count"] > option_b["follower_count"]:
        return choice == "a"
    else:
        return choice == "b"
    
option_b = random.choice(data)
is_game_over = False
score = 0

print(logo)

while not is_game_over:
    option_a = option_b
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)
    print(f"Compare A: {format_description(option_a)}")
    print(vs)
    print(f"Against B: {format_description(option_b)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    system('cls')
    print(logo)

    if is_correct(choice, option_a, option_b):
        score += 1
        print(f"You're right! Current score: {score}")
        
    else:   
        print(f"Sorry, that's wrong. Your score: {score}")
        is_game_over = True



