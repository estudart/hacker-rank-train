grades = [4, 73, 67, 38, 33]


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        else:
            if grade % 5 >= 3:
                final_grades.append(grade - (grade % 5) + 5)
            else:
                final_grades.append(grade)
    return final_grades

print(gradingStudents(grades))