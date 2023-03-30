import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('function took', time.time() - start, 'second')
    
    return wrapper
@timer
def for_loop(number):
    result = 0
    for i in range(number + 1):
        result += i
    return result

@timer
def while_loop(number):
    result = 0
    i = 0
    while (i <= number):
        result += i
        i += 1
    return result 

for_loop(100_000_000)
while_loop(100_000_000)    