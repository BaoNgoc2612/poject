a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
is_triangle = a+b>c and a+c>b and b+c>a 
#
if is_triangle == False  : 
        print("Day khong phai tam giác")
if (a==b==c) and (is_triangle == True):
   print("Day la tam giac deu")
if ( a== b != c or b == c != a or a == c != b ) and (is_triangle == True):
    print("Day la tam giac can")
if (a != b or b != c or c!= a) and is_triangle == True:
    print("Day la tam giac thuong")
# if...if
if is_triangle == True:
    print("Day la tam giac")
    if (a==b==c):
       print("Day la tam giac deu")
    if ( a== b != c or b == c != a or a == c != b ):
       print("Day la tam giac can")
    if (a != b or b != c or c!= a):
       print("Day la tam giac thuong")
#if...else
if not is_triangle:
    print("Day khong phai tam giac")
else:
    #if (a==b==c):
       #print("Day la tam giac deu")
    if ( a== b != c or b == c != a or a == c != b ):
       print("Day la tam giac can")
    if (a != b or b != c or c!= a):
       print("Day la tam giac thuong")
    else:
        print("Day la tam giac deu")
        
#if...elif
if is_triangle == True:
    print("Day la tam giac")
    if ( a== b != c or b == c != a or a == c != b ):
       print("Day la tam giac can")
    elif (a != b or b != c or c!= a):
       print("Day la tam giac thuong")
    else:
       print("Day la tam giac deu")
else:
    print("Day khong phai tam giac")
 
 
 
 
 
 
    
if is_triangle == False  : 
        print("Day khong phai tam giác")
elif (a==b==c):
   print("Day la tam giac deu")
elif( a== b  or b == c  or a == c ) :
    print("Day la tam giac can")
else:
    print("Day la tam giac thuong")

