# Task 1


first_list = [42, None, (-5 + 25), {4, 8, 15, 16, 23, 42}, 'Lingua latina non penis canina', True, 2.28]
for item in first_list:
    print(f'{item} : {type(item)} ')


# Task 2


second_list = list(input('Введите значения списка через пробел').split())
print(second_list)
for i in range(1, len(second_list), 2):
    second_list[i], second_list[i - 1]= second_list[i - 1], second_list[i]
print(second_list)