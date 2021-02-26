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