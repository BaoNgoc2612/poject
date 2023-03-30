hang_hoa = {'coca' : 8000,'banh mi' : 10000, 'tao' : 20000, 'cam' : 15000}
hoa_don = []
print('---Menu---')
for ten in hang_hoa:
    print(f'{ten} -- {hang_hoa[ten]}')
print('----------')
quit = False
while not quit:
    print('nếu bạn không muốn mua nữa nhập "q" nhé ')
    choice = input('Ban Muon Mua Gi: ')
    check = 0
    for ten in hang_hoa:
        if choice == ten:
            so_luong = int(input('Ban mua bao nhieu: '))
            thanh_tien = (hang_hoa[ten]) * so_luong
            hoa_don.append(ten)
            hoa_don.append(so_luong)
            hoa_don.append(thanh_tien)
            check = 1
    if check == 0:
        print('Không có trong menu thử nhập lại nhé :>')
    if choice == 'q':
        quit = True
        print('Xin cảm ơn')
        check = 1
tong = 0
for i in range(0,len(hoa_don),3):
    print(f'Tên: {hoa_don[i]} -- Số Lượng: {hoa_don[i+1]} -- Thành tiền: {hoa_don[i+2]} vnd')
    tong += hoa_don[i+2]
print(f'Bạn cần Thanh Toán: {tong} vnd')