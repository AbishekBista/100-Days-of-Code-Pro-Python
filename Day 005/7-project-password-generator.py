import random
print("Welcome to the Mario Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

generated_password = []

for index in range(1, nr_letters + 1):
    generated_password.append(letters[random.randint(1, len(letters) - 1)])


for index in range(1, nr_symbols + 1):
    generated_password.append(symbols[random.randint(1, len(symbols) - 1)])


for index in range(1, nr_numbers + 1): 
    generated_password.append(numbers[random.randint(1, len(numbers) - 1)])


random.shuffle(generated_password)

password = ""
for characters in generated_password:
    password += characters

print(f"Your strong password: {password}")