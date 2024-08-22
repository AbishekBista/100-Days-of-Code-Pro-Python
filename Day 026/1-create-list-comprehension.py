# Long method to create another list from an existing list
# numbers = [1, 2, 3]

# new_list = []

# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# print(new_list)

# A shorter method
numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(new_list)

name = "Mario"

new_name = [letter for letter in name]
print(new_name)

new_list = [n * 2 for n in range(1, 5)]
print(new_list)


# Conditional list comprehension

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) <=4]

print(short_names)

shouting_names = [name.upper() for name in names if len(name) > 4]

print(shouting_names)