me_nu = ["ice tea", 10000, "peach tea", 12000, "coffee", 15000, "milk coffee", 20000]
quit = False 
while not quit:
    print("Bạn muốn làm gì:")
    print("Bấm 1 để xem menu\nBấm 2 để thêm món mới\nBấm 3 để thoát chương trình")
    lua_chon = (input("Nhap vao lua chon cua ban: "))
    
    if lua_chon == "1": 
        print("----Menu----")   
        for i in range(0,len(me_nu),2):
           print(f'{me_nu[i]} -- {me_nu[i+1]}VND')
    if lua_chon == "2":
        so_luong = int(input("Nhập số lượng món cần thêm: "))
        for i in range(so_luong):
            mon_moi = input("Nhập món mới: ")
            gia_tien = int(input("Nhập giá tiền: "))
            me_nu.append(mon_moi)
            me_nu.append(gia_tien)
            for i in range(0,len(me_nu),2):
                print(f'{me_nu[i]} -- {me_nu[i+1]}VND')
            print("Món đã được thêm vào Menu.")
    elif lua_chon == "3":
        print("Cảm ơn bạn đã dùng dịch vụ của nhà hàng.Hẹn gặp lại!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        
    
