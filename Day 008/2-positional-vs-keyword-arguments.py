def greet_with_names(first_name, second_name):
    print(f"Hello {first_name} and {second_name}")

greet_with_names("Mario", "Luigi") # positional arguments

greet_with_names(second_name = "Luigi", first_name = "Mario") # keyword arguments