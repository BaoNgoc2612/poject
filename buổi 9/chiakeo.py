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