# Task 1


first_list = [42, None, (-5 + 25), {4, 8, 15, 16, 23, 42}, 'Lingua latina non penis canina', True, 2.28]
for item in first_list:
    print(f'{item} : {type(item)} ')


# Task 2


second_list = list(input('Введите значения списка через пробел: ').split())
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

user_string = list(input('Введите строку, разделяя слова пробелом: ').split())
order = 1
for word in user_string:
    if len(word) > 10:
        print(order, word[:10])
    else:
        print(order, word)
    order += 1


# Task 5

my_list = [42, 23, 16, 15, 8, 4]
length = len(my_list)
user_number = input('Введите число: ')
while not user_number.isdigit():
    user_number = input('Ошибка! Необходимо ввести целое число: ')
for item in my_list[::-1]:
    if int(user_number) > item:
        continue
    elif int(user_number) <= item:
        my_list.insert(my_list.index(item) + 1, int(user_number))
        print(my_list)
        break
if length == len(my_list):
    my_list.insert(0, int(user_number))
    print(my_list)


# Task 6

goods_list = []
features = {'название': '', 'цена': '', 'количество': ''}
analytics = {'название': [], 'цена': [], 'количество': []}
num = 0
while True:
    if input('Чтобы добавить продукт и его параметры, введите "Y", чтобы выйти - "N": ').upper() == 'Y':
        num += 1
        for i in features.keys():
            line = input(f'Введите значение свойства {i}: ')
            if i == 'название':
                features[i] = line
            else:
                features[i] = int(line)
            analytics[i].append(features[i])
        goods_list.append((num, features))
        print(goods_list)
        print(analytics)
