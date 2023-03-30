products = {"Apple": 15000, "Orange": 20000, "Coca_Cola": 7000, "Beer": 12000}

def display_products():
    print("Products and Prices:")
    for product in products.items():
        print(product[0] +":" + str(product[1]) + "VND")
      
def  purchase_products():
    shopping_cart = {}
    while True:
        choice = input("Enter the product name to purchase (or 'q' to quit): ")
        if choice in products:
            count = int(input("How many do you want to purchase? "))
            if choice in shopping_cart:
              shopping_cart[choice] += count
            else:
               shopping_cart[choice] = count
        elif choice == "q":
          break
        else:
          print("Sorry, product not found.")
    return shopping_cart

def bill(cart):
    total = 0
    print("Invoice:")
    for product in cart.items():
        print("{:10}: {:2} x {:6} = {:6} VND".format(product[0],product[1],products[product[0]],products[product[0]]*product[1]))
        total += products[product[0]]*product[1]
    print("Total {:26} VND".format(total))

display_products()
shopping_cart = purchase_products()
bill(shopping_cart)