drinks = ["ice tea", 10000, "peach tea", 12000, "coffee", 15000, "milk coffee", 20000]
foods = ["huong duong", 10000, "banh chuoi", 15000 , "my tron", 30000, "pho", 40000]
special_food = ["bo nhat", 200000, "suon cuu", 500000]
menus = [drinks, foods, special_food]

#for menu in menus:
  #  for i in range(0,len(menus),2):
   #    print(f'{menu[i]} --- {menu[i+1]}')    
for i in range(0, len(menus),1):
    if(i==0):
        print("--Meunu do uong--")
    elif(i==1):
        print("--Menu do an--")
    
    for j in range(0,len(menus[i]),2):
        print(menus[i][j], '--', menus[i][j+1])
        
        

        
        

