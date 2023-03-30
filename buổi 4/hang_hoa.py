products = ["Apple", 15000, "Orange", 20000, "Coca_Cola", 7000, "Beer", 12000]
print(f'Mat hang: {products[0]} co gia tien la {products[1]}' + "VND")

products = ['apple', 10, 'banana', 9, 'lemon',10]
print(products[4],products[5])
so_luong_can_mua = int(input(f'Ban muon mua bao nhieu qua {products[4]}: '))
print("ban phai tra: ", so_luong_can_mua*products[5])

products = ['apple', 'banana', 'lemon', 'orange', 'pinnapple']
price = [10, 9, 20, 25]
print(products[0], price[0])
print(products[1], price[1])
print(products[2], price[2])
print(products[3], price[3])
print('-------------------')
for i in range(0,4):
    print(products[i], price[i])
print('--------------------')
for product in products:
    print(product)
for p in price:
    print(p)