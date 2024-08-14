import random
word_list = ["ardvaark", "baboon", "camel"]

# choose a random word
random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]

print(f"The solution is {chosen_word}")
display = []
for letter in chosen_word:
    display.append('_')

while '_' in display:
    guessed_letter = input("Enter a letter: ").lower()
    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter
      
    print(display)

print("You won")