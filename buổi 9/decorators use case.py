import datetime

def log(func):
    ""
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write("\n" + str(func) + "Fuction call with " + " ".join([str(arg) for  arg in args]) + "at" + str(datetime.datetime.now()))
            temp = func(*args, **kwargs)
            return temp
    return wrapper

def summation(a,b):
    return a + b
summation(9,9)

print("--------")
import datetime
def log(func):
    ""
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write("\n" + str(func) + "Fuction call with " + " ".join([str(arg) for  arg in args]) + "at" + str(datetime.datetime.now()))
            temp = func(*args, **kwargs)
            return temp
    return wrapper
def for_loop(number):
    result = 0
    for i in range(number+1):
        result += i
    return result
for_loop(100_000_000)