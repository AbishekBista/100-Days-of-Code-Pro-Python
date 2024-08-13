score_input = input("Enter a list of scores: ")
score_list = score_input.split()

max_score = 0
for score in score_list:
    if int(score) > max_score:
        max_score = int(score)

print(f"The highest score in the class: {max_score}")