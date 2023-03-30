class Hang_hoa:
    def __init__(self,products):
        self.products = products
        self.hoa_don = []

    def print_products(self):
        for product in self.products:              
            print(f'{product}:{self.products[product]} VND')

    def mua_hang(self):       
        quit = False
        while not quit:
            print('Nếu bạn không muốn mua nữa nhập "q" nhé ')
            choice = input('Bạn Muốn Mua Gì: ')
            check = 0
            for product in self.products:
                if choice == product:
                    so_luong = int(input('Bạn mua bao nhiêu: '))
                    thanh_tien = (hang_hoa[product]) * so_luong
                    self.hoa_don.append(product)
                    self.hoa_don.append(so_luong)
                    self.hoa_don.append(thanh_tien)
                    check = 1
            if check == 0:
                print('Không có trong menu thử nhập lại nhé :>')
            if choice == 'q':
                quit = True
                print('Xin cảm ơn')
                check = 1   
    def print_bill(self):
        total = 0
        for i in range(0,len(self.hoa_don),3):
            total += self.hoa_don[i+2]
            print(f'{self.hoa_don[i]} * {self.hoa_don[i+1]} = {self.hoa_don[i+2]} vnd')
        print(f'Bạn cần Thanh Toán: {total} vnd')
        
                      
hang_hoa = {'Coca' : 8000,'Bánh mì' : 10000, 'Táo' : 20000, 'Cam' : 15000}
customer = Hang_hoa(hang_hoa)
print("----Menu----")
customer.print_products()
print("------------")
customer.mua_hang()
print("----Total----")
customer.print_bill()
