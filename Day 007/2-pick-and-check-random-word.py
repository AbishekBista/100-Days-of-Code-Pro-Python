import random
word_list = ["ardvaark", "baboon", "camel"]

# choose a random word
random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]

guessed_letter = input("Enter a letter: ")

for letter in chosen_word:
    if guessed_letter == letter:
        print("Right")
    else:
        print("Wrong")
    