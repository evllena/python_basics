import datetime


# task 1

name = input("Пожалуйста, введите свое имя: ")
print(name, ", сколько Вам лет? Введите число: ")
age = int(input())
print("{}, какой ваш девиз по жизни? ".format(name))
credo = input()
print(f"{name}, к {age} годам Вы поняли: '{credo}'")
print("В 2050 году в этот день Вам будет", age + 29, "лет.")


# task 2
# пока искала, как вывести строку в нужном формате, нашла способ с помошью datetime, который показался проще и удобнее
# поэтому привожу 2 варианта сразу


user_time = int(input("Введите количество секунд: "))
seconds = user_time % 60
hours = user_time // 3600
minutes = user_time % 3600 // 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
a = datetime.time(hours, minutes, seconds)
print(a)


# task 3

number = int(input("Введите целое число от 1 до 9: "))
while number <= 0 or number > 9:
    number = int(input("Пожалуйста, введите целое число от 1 до 9!!! "))
user_sum = number + (number * 10 + number) + (number * 100 + number * 10 + number)
print(f"Ваш результат - {user_sum}.")

# task 4

user_number = int(input("Введите целое положительное число: "))
max_number = user_number % 10
num = user_number
while num > 0:
    digit = num % 10
    if digit > max_number:
        max_number = digit
        if max_number == 9:
            break
    num = num // 10
print(f"Самая большая цифра в введенном вами числе {user_number} равняется {max_number}.")

# task 5

revenue = int(input("Введите сумму Вашей выручки в евро: "))
expenses = int(input("Введите сумму Ваших издержек в евро: "))
user_res = revenue - expenses
if user_res > 0:
    rent = user_res / revenue
    print(f"Отличные новости! Ваша компания работает с прибылью {user_res} евро.")
    print(f"Рентабельность выручки составляет {rent}")
    rev_person = user_res / int(input("Сколько сотрудников работает в Вашей компании? "))
    print(f"Прибыль вашей компании в пересчете на одного человека составляет {rev_person} евро.")
else:
    print(f"Похоже, дела идут не очень! Ваша компания работает с убытком {-user_res} евро.")

# task 6

while True:
    a = float(input("Введите результат первого дня в километрах: "))
    b = float(input("Введите необходимый общий результат в километрах: "))
    days = 1
    while a < b:
        a += a * 0.1
        days += 1
    print(f"Вам потребуется {days} дней, чтобы достичь результата в {b} километров.")
    break