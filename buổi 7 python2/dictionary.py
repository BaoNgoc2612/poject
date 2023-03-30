student = {
    'name':'Nguyễn Thị Bảo Ngọc',
    'age': 21,
    'male':True,
    'major': 'CNTT'
    }
print(student['name'])
print(student['age'])
print(student['male'])
print(student['major'])
for number in student:
    print(f'key:{number} - value:{student[number]}')
    
for key,value in student.items():
    print(f'key:{key}-value:{value}')

student["grade"] = 4.0
print(student["grade"])

#dic lồng nhau
students ={
    'studentA':{
        'name':'Nguyễn Thị Bảo Ngọc',
        'age': 21,
        'male':True,
        'major': 'CNTT',   
    },
    'studentB':{
        'name':'Nguyễn Thị Bảo Ngọc',
        'age': 21,
        'male':True,
        'major': 'CNTT',
    }
}
for number in students:
    print(f'thong tin ve {number}')
    for infor in student[number]:
        print(f'key:{infor}-value:{student[number][infor]}')
