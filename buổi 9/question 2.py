class Student():
  def __init__(self):
    print("Student new")
  def Student_inf(self):
    self.ID = input("Id: ")
    self.GPA = int(input("GPA: "))
    self.Age = input("Age: ")
    self.Grade = input("Grade: ")
  
  def Scholarship(self):
    if int(self.GPA) >= 8:
      return "Win scholarship" 
    else: 
      return "No scholarship"


a = Student()
a.Student_inf()
z=a.Scholarship()
with open("result of the scholarship.txt","w") as wr:
  wr.write(z)