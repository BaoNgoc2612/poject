students = {
    'student_1':{
        'name':"Nguyễn Văn A",
        'grades':{
            'Python':8,
            'Web':7,
            'English': 9,
        }
    },
    'student_2':{
        'name':"Nguyễn Văn b",
        'grades':{
            'Python':8,
            'Web':7,
            'English': 10,
        }
    },
    'student_3':{
        'name':"Nguyễn Văn C",
        'grades':{
            'Python':8,
            'Web':7,
            'English': 6,
        }
    }
    
}
student_grade = []
gpa = []
for student in students:
    for grade in students[student]['grades']:
        print(students[student]['grades'][grade])


    
    
   

        

    