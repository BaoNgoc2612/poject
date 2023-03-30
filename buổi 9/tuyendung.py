print("------------")
import sys

run = True
def input_personal_info():
    try:
        person_infor = {}
        person_infor['name'] = input('Hãy nhập tên của bạn: ')
        person_infor['gender'] = input('Hãy nhập giới tính của bạn(nam/nữ): ')
        person_infor['age'] = int(input('Hãy nhập tuổi của bạn: '))
        person_infor['experience'] = int(input('Hãy nhập số năm kinh nghiệm của bạn trong ngành dịch vụ: '))
        person_infor['height'] = float(input('Hãy nhập chiều cao của bạn (theo mét): '))
        person_infor['weight'] = float(input('Hãy nhập cân nặng của bạn (theo kg): '))
        return person_infor
    except ValueError:
        print('Có lỗi exception',sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        print('Bạn cần phải nhập lai')

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