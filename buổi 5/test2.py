
    
me_nu = []
so_luong = int(input('Nhap so lượng bạn muốn mua: '))
for i in range(0, so_luong):
    do_uong = input("Nhập đồ uống: ")
    me_nu.append(do_uong)
    gia_tien = float(input('Nhap giá tiền: '))
    me_nu.append(gia_tien) 
for i in range(0,2*so_luong,2):
    print(f'tên sản phẩm:{me_nu[i]}')   
    
