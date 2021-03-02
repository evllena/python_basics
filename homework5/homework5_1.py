
with open("task1.txt", "w") as f_obj:
    while True:
        user_str = input("Введите данные для записи в файл: ")
        if user_str == "":
            break
        else:
            f_obj.write(user_str + "\n")