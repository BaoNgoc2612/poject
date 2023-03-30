def input_number():
  number_student = []
  number_subject = []
  ten_mon_hoc = []
  number_student = int(input("Nhap vao so hoc sinh: "))
  number_subject = int(input("Nhap vao so mon hoc: "))
  for i in range(number_subject):
    ten_mon_hoc.append(input("Nhap vao mon hoc: "))
  return number_student, number_subject, ten_mon_hoc

def input_information():
  Danh_sach_lop = []
  for i in range(number_student):
    ID = int(input("Sinh vien Id: "))
    name = input("Tên sinh viên: ")
    print("Điểm học phần: ")
    diem = []
    for j in ten_mon_hoc:
      diem_hoc_phan = int(input(j + " : "))
      diem.append(diem_hoc_phan)
    print("Average grade: ", GPA(diem))
    diem_trung_binh = GPA(diem)
    Danh_sach_lop.append([ID, name, diem, diem_trung_binh])
  return Danh_sach_lop
def GPA(danh_sach_mon):
  return sum(danh_sach_mon)/ len(danh_sach_mon)
number_student, number_subject, ten_mon_hoc  = input_number()
Danh_sach_lop = input_information() 

def danh_sach_lop(Danh_sach_lop):
  for i in Danh_sach_lop:
    print("-"*20)
    print("Sinh viên Id: ", i[0])
    print("Tên sinh viên:", i[1])
    print("Điểm học phần: ")
    for j in range(number_subject):
      print(ten_mon_hoc[j], ": " ,i[2][j])
    print("average grade: ", i[3])  
danh_sach_lop(Danh_sach_lop)

