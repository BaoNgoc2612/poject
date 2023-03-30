a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
deta = b**2 - 4*a*c
#if
if deta>0:
    print("Phương trình có 2 nghiệm phân biệt")
if deta<0:
    print("Phương trình vô nghiệm")
if deta==0:
    print("Phương trình có nghiệm kép")
#if...else   
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
deta = b**2 - 4*a*c
if deta==0:
    print("Phương trình có nghiem kep")
else:
    if deta>0:
       print("Phương trình co 2 nghiep phan biet")
    else:
       print("Phương trình vo nghiệm ")
#if..elif..else
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
deta = b**2 - 4*a*c
if deta>0:
    print("Phương trình có 2 nghiệm phân biệt")
elif deta<0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm kép")