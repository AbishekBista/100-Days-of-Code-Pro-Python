import random
# input the names
name_input = input("Enter the names: ")

# get the name array using split
name_list = name_input.split(", ")

# generate a random number
random_index = random.randint(0, len(name_list) - 1)
payee = name_list[random_index]

print(f"Bill will be paid by: {payee}")



