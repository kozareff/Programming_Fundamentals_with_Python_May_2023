students = int(input())

students_and_average_grades = {}
best_students = {}

for student in range(students) :
    student_name = input()
    student_grade = float(input())

    if student_name not in students_and_average_grades.keys() :
        students_and_average_grades[student_name] = student_grade
    else :
        new_grade = (student_grade + students_and_average_grades[student_name]) / 2
        students_and_average_grades[student_name] = new_grade

for student,grade in students_and_average_grades.items():
    if students_and_average_grades[student] < 4.5 :
        continue
    best_students[student] = grade


for name, average_grade in best_students.items():
    print(f"{name} -> {average_grade:.2f}")