# Task 1

def divide(dividend, divisor):
    if divisor == 0:
        return "На ноль делить нельзя! Введите другой делитель!"
    return dividend / divisor


num1 = float(input("Введите делимое: "))
num2 = float(input("Введите делитель: "))
print(f"Результат деления {num1} на {num2} - {divide(num1, num2)}")