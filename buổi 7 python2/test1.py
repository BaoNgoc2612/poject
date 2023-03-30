
products = {
    'Apple':15000,
    "Orange": 20000, 
    "Coca_Cola": 7000,
    "Beer": 12000,
} 
print("------Menu------")
for product in products.items():
    print(f'{product[0]}: {product[1]}VND')
print("----------------")
print("Bạn muốn mua gì")
cart = {}
while True:
    choice = input('Bạn muốn mua hàng hoá gì (nhập "q" để kết thúc): ')
    if choice == 'q':
        break
    if choice in products:
        so_luong_muon_mua = int(input("Bạn muốn mua số lượng bao nhiêu: "))
        print(f'Đã thêm {choice} vào giỏ hàng')
        if choice not in cart:
            cart[choice] = so_luong_muon_mua
        else:
            cart[choice] += so_luong_muon_mua
    else:
        print('Hàng hoá không tồn tại')

print("Invoice:")
total = 0
for product in cart.items():
        #print("{:10}: {:2} x {:6} = {:6} VND".format(product[0],product[1],products[product[0]],products[product[0]]*product[1]))
        print(f'{product[0]}: {products[product[0]]}*{product[1]}')
        total += products[product[0]]*product[1]
#print("Total {:26} VND".format(total))
print(f'Tổng tiền hoá đơn là: {total} VND')

