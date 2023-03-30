first_number = input("Nhap so thu nhat: ")
second_number = input("Nhap so thu hai: ")
third_number = input("Nhap vao so thu ba: ")


if first_number > second_number and first_number > third_number:
    print(f'So thu nhat la {first_number}')
if first_number < second_number and second_number > third_number:
    print(f'So thu hai la {second_number}')
if first_number < third_number and second_number < third_number:
    print(f'So thu ba la {third_number}')