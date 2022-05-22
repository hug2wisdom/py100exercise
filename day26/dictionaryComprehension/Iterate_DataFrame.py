# Loop a DataFrame just look like loop a dictionary.
import pandas
student_dict = {
    "student": ["lebron", "kobe", "durant", "bruce"],
    "score": [99, 98, 93, 34]
}

student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# loop through the rows of the dataFrame

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "lebron":
        print(row.score)