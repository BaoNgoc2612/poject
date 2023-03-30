def is_triangle (a,b,c):
    is_triangle = a+b>c and a+c>b and b+c>a
    if is_triangle == False: #if not is_triangle:
        print("Day khong phai tam giac")
    if is_triangle == True: #if is_triangleo
        print("Day la tam giac")
        if (a==b==c):
            print("Day la tam giac deu")
        if ( a== b != c or b == c != a or a == c != b ):
            print("Day la tam giac can")
        if (a != b or b != c or c!= a):
            print("Day la tam giac thuong")
is_triangle(5,6,7)