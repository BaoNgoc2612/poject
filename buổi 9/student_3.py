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
        so_mon_muon_nhap = int(input("Số môn muốn học: "))
        for i in range(so_mon_muon_nhap):
            new_subject = input('Hãy nhập môn học mới: ')
            self.grades[new_subject] = float(input('Hãy nhập điểm của môn học mới: '))
    def dieu_kien_tot_nghiep(self):
            if int(self.gpa)/10*4 >= 2.5:
                print("Đủ điều kiện tốt nghiệp" ) 
            else: 
                print("Bạn không đủ điều kiện tốt nghiệp")
print("---------------------")
student_1 = Student()
student_1.add_new_subject()
student_1.calculate_gpa()
student_1.print_info()
student_1.dieu_kien_tot_nghiep()
print("---------------------")
student_2 = Student()
student_2.add_new_subject()
student_2.calculate_gpa()
student_2.print_info()
student_2.dieu_kien_tot_nghiep()

