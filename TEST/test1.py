number = int(input("Nhap vao 1 so: "))
if 1 < number < 10:
    print("Ban da nhap dung")
    total = 0
    for i in range(1, number-1,2):
        total = total + number
    print(total)
else:
    print("Ban da nhap sai")
    
