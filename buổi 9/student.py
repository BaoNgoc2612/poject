class Student:
    def __init__(self,id, name, grades):
        self.id = id
        self.name = name
        self.grades = grades
        self.gpa = 0

    def print_info(self):
        print(f'Sinh viên thứ id: {self.id}')
        print(f'Tên sinh viên: {self.name}')
        for subject in self.grades:
            print(f'{subject}: {self.grades[subject]}')
        print(f'student GPA: {self.gpa}')

    def calculate_gpa(self):
        total = 0
        for subject in self.grades:
            total += self.grades[subject]
        self.gpa = total / len(self.grades)

    def add_new_subject(self):
        new_subject = input('Hãy nhập môn học mới: ')
        self.grades[new_subject] = float(input('Hãy nhập điểm của môn học mới: '))
    

student_1_grade = {'Python':9, 'Web':10, 'English':8} 
student_1 = Student(1, 'Linh', student_1_grade)
student_1.calculate_gpa()
print('-----------')
student_1.print_info()
print('------------')
student_1.add_new_subject()
student_1.calculate_gpa()
student_1.print_info()
    
#không có điểm môn nào
class Student:
    def __init__(self):
        self.id = input("Sinh viên ID: ")
        self.name = input("Tên sinh viên: ")
        self.grades = {}
        self.gpa = 0

    def print_info(self):
        print(f'Sinh viên thứ id: {self.id}')
        print(f'Tên sinh viên: {self.name}')
        for subject in self.grades:
            print(f'{subject}: {self.grades[subject]}')
        print(f'student GPA: {self.gpa}')

    def calculate_gpa(self):
        total = 0
        for subject in self.grades:
            total += self.grades[subject]
        self.gpa = total / len(self.grades)

    def add_new_subject(self):
        new_subject = input('Hãy nhập môn học mới: ')
        self.grades[new_subject] = float(input('Hãy nhập điểm của môn học mới: '))
    

student_1 = Student()
student_1.add_new_subject()
student_1.add_new_subject()
student_1.add_new_subject()
student_1.calculate_gpa()
student_1.print_info()

