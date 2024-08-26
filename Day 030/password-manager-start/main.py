from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for item in range(nr_letters)]
    symbols_list = [random.choice(symbols) for item in range(nr_symbols)]
    nr_numbers = [random.choice(numbers) for item in range(nr_numbers)]
    password_list = letters_list + symbols_list + nr_numbers

    random.shuffle(password_list)
    password_char = ''.join(password_list)
    password_input.insert(0, password_char)
    pyperclip.copy(password_char)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_input.get()
    user_name = username_input.get()
    password = password_input.get()
    new_data = {
        website_name: {
            "email": user_name,
            "password": password
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as file:   
                # Read data
                data = json.load(file)        
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)            
        else:
            data.update(new_data)
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website_name = website_input.get()
    if len(website_name) == 0:
        messagebox.showinfo(title="Oops", message="Do not leave the website field empty!")
    else:
        try:
            with open('data.json', mode='r') as data:
                all_details = json.load(data)
        except FileNotFoundError:
            messagebox.showinfo(title="No data", message="No data file found!")
        else:
            try:
                user_name = all_details[website_name]['email']
                password = all_details[website_name]['password']
            except KeyError:
                messagebox.showinfo(title="No data stored", message=f"Details for {website_name} not found")
            else:
                messagebox.showinfo(title=f"{website_name}", message=f"Email: {user_name}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
password_logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/User name:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'mario@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2)

search_button = Button(width=30, text="Search", command=search)
search_button.grid(row=4, column=1, columnspan=2)

generate_password_button = Button(width=30, text="Generate Password", command=generate_password)
generate_password_button.grid(row=5, column=1, columnspan=2)

add_button = Button(width=30, text="Add", command=save_password)
add_button.grid(row=6, column=1, columnspan=2)

window.mainloop()