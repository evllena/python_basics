from sys import argv


def payment():
    try:
        hours, rate, bonus = float(argv[1]), float(argv[2]), float(argv[3])
        print(f"Зарплата составляет {hours * rate + bonus}")
    except ValueError:
        print("Ошибка! Введите три числа!")


payment()

