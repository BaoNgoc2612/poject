number_of_students = int(input('Nhap so sinh vien: '))
number_of_subjects = int(input('nhap so mon hoc: '))
student_grades = []
avagare_student_grades =[]
for i in range(0, number_of_students, 1):
    print(f'hãy nhập điểm của sinh viên thứ {i+1}: ')
    temps = []
    for j in range(number_of_subjects):
        temp = float(input(f'Hãy nhập điểm môn thứ {j+1}: '))
        temps.append(temp)
    student_grades.append(temps)
print(student_grades)
for student_grade in student_grades:
    total  = 0
    for grade in student_grade:
        float(grade)
        total += grade
    avagare_student_grade = total/number_of_subjects
    avagare_student_grades.append(avagare_student_grade)
print(avagare_student_grades)