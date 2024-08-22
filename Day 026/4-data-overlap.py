with open("file1.txt") as file:
    number_1 = file.read().split("\n")

with open("file2.txt") as file:
    number_2 = file.read().split("\n")

combined_numbers = [int(n) for n in number_1 if n in number_2]

print(combined_numbers)
