import pandas

code_data = pandas.read_csv('nato_phonetic_alphabet.csv')

code_letter_dict = {row['letter']: row['code'] for (index, row) in code_data.iterrows()}

name = input("Enter a name: ").upper()

nato_code = [code_letter_dict[letter] for letter in name]

print(nato_code)