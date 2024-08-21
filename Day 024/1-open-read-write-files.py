# First approach - manually close the file stream
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close() # close the file link

# Second approach
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to a file using w -> overwrite existing content or a -> append to existing content
with open("my_file.txt", mode="a") as file:
    file.write("\nI'll go on an adventure.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file_2.txt", mode="w") as file:
    file.write("New contents")

