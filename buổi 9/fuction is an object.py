def func_1():
    print("called func_1")
func_1()
print(func_1)

print("-----")
def func_1():
    print("called func_1")
def func_2(func):
    func()
func_2(func_1)

print("-----")
def func_1(func):
    def wrapper():
        print('Begin')
        func()
        print('End')
    return wrapper
def func_2():
    print('Processing')    
func_1(func_2)()

print("-----")
def func_1(func):
    def wrapper():
        print('Begin')
        func()
        print('End')
    return wrapper
def func_2():
    print('Processing')    
func_3 = func_1(func_2)
func_3()

print("-----")
def func_1(func):
    def wrapper():
        print('Begin')
        func()
        print('End')
    return wrapper
def func_2():
    print('Processing')
func_2()

print("-----")
def func_1(func):
    def wrapper(*args,**kwargs):
        print("Begin")
        func(*args, **kwargs)
        print("End")
    return wrapper
def func_2(message):
    print(message)
func_2('hello')

print("-----")
def func_1(func):
    def wrapper(*args,**kwargs):
        print("Begin")
        func(*args, **kwargs)
        print("End")
    return wrapper
def func_2(message):
    print(message)
def func_3(message1,message2):
    print(message1)
    print(message2)
func_2("hello")
print("-----------------")
func_3("Hi!", "Bye!")

print("-----")
def func_1(func):
    def wrapper(*args,**kwargs):
        print("Begin")
        func(*args, **kwargs)
        print("End")
def summation(a,b):
    return a + b
result = summation(3,5)
print(result)

print("-----")
def func_1(func):
    def wrapper(*args, **kwargs):
        print("Begin")
        temp = func(*args, **kwargs)
        print("End")
        return temp
    return wrapper     
def summation(a,b):
    return a + b
result = summation(3,5)
print(result)
