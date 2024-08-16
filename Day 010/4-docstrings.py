def format_name(f_name, l_name):
    """Takes first and last name as input and gives a title case version of the full name"""
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input."
    return f"{f_name.title()} {l_name.title()}"


full_name = format_name(input("What is your first name? "), input("What is your last name? "))

print(full_name)