from morse import morse_code_dict
from morse_code_art import art

print(art)

string = input("Enter a string to be converted to morse: ")
morse_string = ''

for letter in string:
    if letter.isalpha():
        morse_string += morse_code_dict[letter.upper()] + '   '
    elif letter.isdigit():
        morse_string += morse_code_dict[letter] + '   '
    elif letter == ' ':
        morse_string += '       '

print(morse_string)