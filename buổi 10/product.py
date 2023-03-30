class Product:
    def __init__(self):
        self.name = input("Hay nhap ten hang hoa: ")
        self.price = int(input("Hay nhap gia cua hang hoa: "))

    def print_info(self):
        print(f'{self.name} -- {self.price}')

    def update_price(self, new_price):
        self.price = new_price

    def update_name(self, new_name):
        self.name = new_name

# product_1 = Product()
# product_1.print_infor()


class Product_list:
    def __init__(self):
        self.product_list = []

    def add_product(self):
        new_product = Product()
        self.product_list.append(new_product)

    def print_info(self):
        for product in self.product_list:
           product.print_info()

   # def del_product(self):
    #    pass

    #def update_product(self):
    #    self.product_list[0].update_price(30000)


class Bill():
    def __init__(self):
        self.buying_list = {}
        self.total = 0
    def buy(self, product_list):    
        while True:
                print("----Menu----")
                product_list.print_info()
                choice = input("Nhập tên hàng hóa bạn muốn mua (nhấn q để thoát): ")
                if choice == 'q':
                    break
                for product in product_list.product_list: 
                        if choice == product.name :
                            quantity = int(input("Bạn muốn mua số lượng bao nhiêu: "))             
                        if product.name not in self.buying_list:
                            self.buying_list[product.name] = {"quantity": 0, "price": product.price}
                        self.buying_list[product.name]["quantity"] += quantity
        print("---Invoice---")        
        total = 0
        for product_name,product_info in self.buying_list.items():
            quantity = product_info["quantity"]
            price = product_info["price"]
            total += quantity * price
            print(f"{product_name}: {quantity} x {price} = {quantity * price}")
            
                               
            
         
        
product_list_1 = Product_list()
product_list_1.add_product()
product_list_1.add_product()
#product_list_1.update_product()
#product_list_1.print_info()

product_bill_1 = Bill()
product_bill_1.buy(product_list_1)



        
    