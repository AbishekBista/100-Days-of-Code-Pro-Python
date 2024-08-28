from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    french_words = pandas.read_csv('data/words_to_learn.csv')
    print('Words to learn loaded')
except FileNotFoundError:
    print('File not found, reading from french_words')
    french_words = pandas.read_csv('data/french_words.csv')

# word_dictionary = [{row['French'], row['English']} for (index, row) in french_words.iterrows()]
word_dictionary = french_words.to_dict(orient="records")

word_index = 0

flip_timed = None

# CHOOSE RANDOM FRENCH WORDS FUNCTION
def choose_random_word():
    global word_index
    global flip_timed
    window.after_cancel(flip_timed)
    canvas.itemconfig(card_face, image=front_card_image)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(french_word_holder, fill="black")
    word_map = random.choice(word_dictionary)
    french_word = word_map["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(french_word_holder, text=french_word)
    word_index = word_dictionary.index(word_map)
    flip_timed = window.after(3000, flip_card)

    

def flip_card():
    global word_index
    print("I was called madam")
    canvas.itemconfig(card_face, image=back_card_image)
    canvas.itemconfig(title, text="English", fill="white")
    print(word_index)
    english_word = word_dictionary[word_index]["English"]
    canvas.itemconfig(french_word_holder, text=english_word, fill="white")

def is_known():
    global word_index
    word_dictionary.remove(word_dictionary[word_index])
    print(len(word_dictionary))
    data = pandas.DataFrame(word_dictionary)
    data.to_csv('data/words_to_learn.csv')
    choose_random_word()
    
# UI Section
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timed = window.after(3000, flip_card)

front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_face = canvas.create_image(410, 263, image=front_card_image)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
french_word_holder = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0,  command=choose_random_word)
wrong_button.grid(row=1, column=0,)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

choose_random_word()

window.mainloop()