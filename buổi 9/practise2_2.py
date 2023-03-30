class Card:
    def __init__(self, suit, value):
        self.value = value #self.suit la ten thuoc tinh 
        self.suit = suit#suit la gia tri 
card_1 = Card(3, "Heart")
card_2 = Card(2, 'Clubs')
print(f'Quan bai thu nhat:{card_1.value}---{card_1.suit}')
print(f'Quan bai thu nhat:{card_2.value}---{card_2.suit}')
#tao 1 lop student
class Student:
    def __init__(self, ID, name, grades, ):
        self.ID = ID
        self.name = name
        self.grades =grades
        self.gpa = 0        
student_1_grades = {'Python': 9, 'Web': 10, 'English': 8}        
student_1 = Student(1, "Nguyen A", 9, 8, 10)
student_2 = Student(2, "Nguyen B", 6, 7, 8)
print(f'Sinh vien ID: {student_1.ID}')
print(f'Ten sinh vien: {student_1.name}')
print("Diem hoc phan")
print(f'Python: {student_1.python}')
print(f'Web: {student_1.web}')
print(f'English: {student_1.english}')
    
     
