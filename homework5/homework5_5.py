with open("task5.txt", "w") as f:
    f.write(input("Введите числа, разделенные пробелами: "))
with open("task5.txt") as f:
    res = f.readline().split()
    my_sum = 0
    for number in res:
        my_sum += int(number)
    print(f"Сумма введенных вами чисел равняется {my_sum}.")
