def sum_three_numbers(number_1,number_2,number_3):
    total = number_1 + number_2 + number_3
    print(total)
    return total
total1= sum_three_numbers(1,5,7)
total2 = sum_three_numbers(3,7,9)
print(total1 + total2)

def sum_multiply_three_numbers(number_1,number_2,number_3):
    total = number_1 + number_2 + number_3
    multiply = number_1 * number_2 * number_3
    print(f'Kết quả là:{total}')
    print(f'Kết quả là: {multiply}')
    return total,multiply
result1, result2 = sum_multiply_three_numbers(3,5,7) 
print(result1)
print(result2)

def print_message(message, time=2):
    for i in range(time):
        print(message)
print_message("I am learning python",1)
#nếu không khai báo biến thì ko sử dụng được
def print_message():
    local ="cntt"
    print(f'local inside function: {local} ')
    return local
local = print_message()
print(f'name out side function: {local}')