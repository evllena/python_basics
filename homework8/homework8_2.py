class MyZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
while True:
    b = input("Введите делитель: ")

    try:
        data1, data2 = float(a), float(b)
        if data2 == 0:
            raise MyZeroDivision("Ошибка! Деление на 0 невозможно!")

    except ValueError:
        print("Ошибка!Введите числа!")
    except MyZeroDivision as my_error:
        print(my_error)
    else:
        print(round(data1 / data2))
        break
