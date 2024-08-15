student_scores = {
    "Harry": 81,
    "Ron": 79,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[student] = grade

print(student_grades)