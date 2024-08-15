my_details = {
    "name": "Mario",
    "job": "Plumber"
}

# access values of dictionary
print(my_details["name"])

# adding item to dictionary
my_details["age"] = "Very old"

print(my_details)

# create an empty dictionary
new_dict = {}

# wipe data of dictionary
my_details = {}

print(my_details)

# reassign values to keys
my_details["name"] = "Luigi"

# Loop through a dictionary
for key in my_details:
    print(key)
    print(my_details[key])