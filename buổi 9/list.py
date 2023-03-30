outputComprehemsion = [i*i for i in range(1,11)]
print(outputComprehemsion)
print("------------")
def factorials(number):
    output = 1
    for i in range(2, number+1):
        output *= i
    return output
output = [factorials(i) for i in range(2,8)]
print(output)
print("------------")
def is_prime(number):
    check = True
    for i in range(2, int(number/2)+1):
        if (number % i == 0):
            check = False
            break
    if(check):
            return number 
output = [i for i in range(2,20) if(is_prime(i))]
print(output)

print("------------")
def is_prime(number):
    check = True
    for i in range(2, int(number/2)+1):
        if (number % i == 0):
            check = False
            break
    if(check):
            return number 
primeList = [i if(is_prime(i)) else 0 for i in range(2,20)]
print(primeList)

print("------------")
def input_personal_info():
    person_infor = {}
    person_infor['name'] = input('Hãy nhập tên của bạn: ')
    person_infor['gender'] = input('Hãy nhập giới tính của bạn(nam/nữ): ')
    person_infor['age'] = int(input('Hãy nhập tuổi của bạn: '))
    person_infor['experience'] = int(input('Hãy nhập số năm kinh nghiệm của bạn trong ngành dịch vụ: '))
    person_infor['height'] = float(input('Hãy nhập chiều cao của bạn (theo mét): '))
    person_infor['weight'] = float(input('Hãy nhập cân nặng của bạn (theo kg): '))
    return person_infor

def is_qualified(person_infor):

    def print_qualified_message():
        print('Xin chúc mừng bạn đã trúng tuyển')
    def print_not_qualified_message():
        print('Xin lỗi bạn không hợp lệ')
    
    if person_infor['gender'] == 'nam':
        print_not_qualified_message()
        return False

    if 30 <= person_infor['age'] <= 40:
        if person_infor['experience'] >= 5 and person_infor['height'] >= 1.55 and person_infor['weight'] <= 45:
            print_qualified_message()
        elif person_infor['experience'] >= 2 and person_infor['height'] >= 1.6 and person_infor['weight'] <= 50:
            print_qualified_message()
        else:
            print_not_qualified_message()
    elif 18 <= person_infor['age'] < 30:
        if person_infor['height'] >= 1.6 and person_infor['weight'] <= 50:
            print_qualified_message()
        else:
            print_not_qualified_message()
    else:
        print_not_qualified_message()

is_qualified(input_personal_info())

print("--------------------------------------------")
import sys
run = True
while run:
    try:
        numberOfCandy = int(input('Hãy nhập số kẹo của bác: '))
        numberOfStudent = int(input('Hãy nhập số học sinh: '))
        numberOfCandyPerStudent = int(numberOfCandy / numberOfStudent)
        numberOfCandyLeft = numberOfCandy % numberOfStudent
        print('Số kẹo mỗi học sinh nhận được: ', numberOfCandyPerStudent)
        print('Số kẹo thừa: ',numberOfCandyLeft)
    except ZeroDivisionError:
        print('Có lỗi exception', sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        print('Bạn đã nhập số học sinh là 0 nên chương trình không thực hiện được')
    except ValueError:
        print('Có lỗi exception',sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        print('Bạn cần phải nhập số')
    option = input("Bấm 'c' để tiếp tục, bấm 'k' để dừng: ")
    run = True if option == 'c' else False

print('Chương trình kết thúc')