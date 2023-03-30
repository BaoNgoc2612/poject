number_student = []
number_sujects = []
ten_mon_hoc = []
diem_hoc_phan = []
student_grades = []
GPA = []
number_student = int(input("Nhap vao so hoc sinh: "))
number_sujects = int(input("Nhap vao so mon hoc: "))
for i in range(number_sujects):
    ten_mon_hoc.append(input("Nhap vao mon hoc: "))
for j in range(number_student):
    name = input("Tên sinh viên: ")
    for h in range(number_sujects):
        diem_hoc_phan.append(float(input(f'Nhap vao diem cua mon thu {(h+1)} cua hoc sinh thu {(j+1)} : ')))
    student_grades.append(diem_hoc_phan)
print(student_grades)
for student_grade in student_grades:
    total  = 0
    for diem_hoc_phan in student_grade:       
        total += diem_hoc_phan
    avagare_student_grade = total/number_sujects
    GPA.append(avagare_student_grade)



    





   
 
 
