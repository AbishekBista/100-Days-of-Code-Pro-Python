import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data = pandas.DataFrame(student_dict)

# Loop through rows of a data frame

for(index, row) in student_data.iterrows():
    print(row)

