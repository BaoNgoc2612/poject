foods = ["ice tea", 10000, "peach tea", 12000, "coffee", 15000, "milk coffee", 20000, "milk tea",2500]
print("Ban muon mua gi")
select_food = input("Mon do muon mua: ")
quantity = int(input('Nhap vao so luong can mua: '))
check = 0
for i in range(0,len(foods),2):
    if(select_food == foods[i]):
           print(f'so tien ban phai tra: {foods[i+1] * quantity}')
           check = 1
if(check == 0):
    print("Ban da nhap sai")
    

    
    

    