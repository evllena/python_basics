# Task 1


first_list = [42, None, (-5 + 25), {4, 8, 15, 16, 23, 42}, 'Lingua latina non penis canina', True, 2.28]
for item in first_list:
    print(f'{item} : {type(item)} ')


# Task 2


second_list = list(input('Введите значения списка через пробел').split())
print(second_list)
for i in range(1, len(second_list), 2):
    second_list[i], second_list[i - 1] = second_list[i - 1], second_list[i]
print(second_list)


# Task 3

while True:
    user_input = input('Введите месяц в виде целого числа от 1 до 12: ')

    month_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
    month_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
    if user_input.isdigit() and 0 < int(user_input) <= 12:
        print(f'Месяц под номером {user_input} относится ко времени года - {month_list[int(user_input) // 3]}')
        print(f'Месяц под номером {user_input} относится ко времени года - {month_dict[int(user_input) // 3]}')
        break
    else:
        print('Ошибка!')


# Task 4


