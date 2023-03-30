
n = int(input("Nhap gia tri n: "))
tong = 0
numbers = []
for i in range(1,n+1):
    numbers.append(i)
for number in numbers:
    tong += number
print(tong)
    
    