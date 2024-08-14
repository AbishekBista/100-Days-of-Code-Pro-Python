import random
from stages import stages
from word_list import word_list
from os import system

# choose a random word
chosen_word = random.choice(word_list)
lives = 6
display = []

for letter in chosen_word:
    display.append('_')

end_of_game = False
while end_of_game == False:
    guessed_letter = input("\nGuess a letter: ").lower()

    system('cls')
    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")
    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter
    
    if '_' not in display:
        end_of_game = True
        print(stages[lives])
        print("You won")

    

    if(guessed_letter not in chosen_word):
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print("You lost")
            break
        
    print(f" ".join(display))
    print(stages[lives])
    print('**********************************')