import pandas

code_data = pandas.read_csv('nato_phonetic_alphabet.csv')

code_letter_dict = {row['letter']: row['code'] for (index, row) in code_data.iterrows()}

is_correct_input = False

while not is_correct_input:
    name = input("Enter a name: ").upper()
    try:
        nato_code = [code_letter_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_code)
        is_correct_input = True