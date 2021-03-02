# Task 1

def divide(dividend, divisor):
    if divisor == 0:
        return "На ноль делить нельзя! Введите другой делитель!"
    return dividend / divisor


num1 = float(input("Введите делимое: "))
num2 = float(input("Введите делитель: "))
print(f"Результат деления {num1} на {num2} - {divide(num1, num2)}")


# Task 2

def user_info(name, lastname, birth_year, city, email, phone):
    return f"Имя пользователя - {name} {lastname}, год рождения - {birth_year}," \
           f"город проживания - {city}, эл.почта - {email}, телефон - {phone}."


print(user_info(name="Лена", lastname="Ермолаева", birth_year=1992, city="Красноярск",
                email="helen.ermolaeva@mail.ru", phone=89135623691))


# Task 3


def sum_largest(first, second, third):
    return (first + second + third) - min(first, second, third)


result = sum_largest(float(input('Введите число: ')), float(input('Введите число: ')), float(input('Введите число: ')))
print(f"Сумма двух наибольших чисел равняется {result}")


# Task 4


def power1(x, y):
    return x ** y


def power2(x, y):
    power = 1
    res = 1
    while power <= y:
        res *= x
        power += 1
    return res


print(power1(2, 4))
print(power2(2, 4))


# Task 5


def sum_all():
    sum_numbers = 0
    while True:
        num_list = input("Введите числа через пробел, чтобы закончить, введите '&': ").split()
        for number in num_list:
            if number == '&':
                return f"Сумма всех введенных чисел составляет {sum_numbers}"
            else:
                sum_numbers += float(number)
        print(f"Сумма всех введенных чисел составляет {sum_numbers}")


print(sum_all())


# Task 6


def upper_reg(word):
    if word.islower():
        return word.capitalize()
    else:
        return "Неверный формат. Слово должно содержать только строчные буквы."


print(upper_reg("word"))
print(upper_reg("Word"))
print(upper_reg("слово"))


def upper_reg1(word):
    if word.islower():
        return word.capitalize()
    else:
        return False


user_input = input("Введите слова, состоящие из строчных букв через пробел: ").split()
for w in user_input:
    result = upper_reg1(w)
    if result:
        print(upper_reg1(w), end=' ')
