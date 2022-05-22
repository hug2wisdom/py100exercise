from random import randint

students_names = ["Lebron", "Kobe", "Durant"]
students_scores = {names: randint(1, 100) for names in students_names}
print(students_scores)

passed_students = {names: scores for (names, scores) in students_scores.items() if scores > 60}
print(passed_students)