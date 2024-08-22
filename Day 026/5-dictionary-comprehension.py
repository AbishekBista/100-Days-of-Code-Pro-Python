# new_dict = {new_key: new_value for item in list if test} for lists
# new_dict = {new_key: new_value for (key, value) in dict.items() if test} for dictionary
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

scores_dict = { name: random.randint(1, 101) for name in names }

print(scores_dict)

scores_dict = {'Alex': 31, 'Beth': 67, 'Caroline': 33, 'Dave': 26, 'Eleanor': 42, 'Freddie': 66}

pass_dict = { name:score for (name, score) in scores_dict.items() if score >= 60 }
print(pass_dict)

