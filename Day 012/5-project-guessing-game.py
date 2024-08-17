import random
from os import system
from art import logo

def show_prompt(num_of_attempts):
    if num_of_attempts > 0:
        return f"You have {num_of_attempts} attempts left."
    else:
        return "You've run out of guesses. You lose"

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    number = random.randint(1, 100)

    if difficulty == 'easy':
        num_of_attempts = 10
    elif difficulty == 'hard':
        num_of_attempts = 5

    while num_of_attempts > 0:
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number:
            print(f"You got it! The answer was {number}")
            break
        elif guessed_number > number:
            print(f"Too high!")
            num_of_attempts -= 1
            print(show_prompt(num_of_attempts))
        elif guessed_number < number:
            print(f"Too low!")
            num_of_attempts -= 1
            print(show_prompt(num_of_attempts))
            

while input("Do you want to play The Guessing Game? Type 'y' or 'no': ") == 'y':
    system('cls')
    play_game()

