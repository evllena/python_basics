from itertools import cycle, count


print("Введите стартовое число. Нажимайте enter для генерации нового числа или введите Q для завершения")

for el in count(int(input("Введите целое число для начала генерации чисел: "))):
    print(el, end=' ')
    q = input()
    if q == 'Q':
        break


print('\n')
c = count()
for el in count(int(input("Введите целое число для начала генерации чисел: "))):
    print(el, end=' ')
    if next(c) == 9:
        break

print('\n')

c = count()
list1 = [2, 4, 15, 16, 23, 42]
for el in cycle(list1):
    print(el, end=' ')
    if next(c) == 9:
        break
