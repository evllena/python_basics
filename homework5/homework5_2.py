from itertools import count

with open("task2.txt", "r") as my_file_obj:
    my_file_list = my_file_obj.readlines()
print(f"В данном файле {len(my_file_list)} строк(и).")

c = count()
for line in my_file_list:
    words = 1
    if line == '\n':
        words = 0
    for symbol in line:
        if symbol == ' ':
            words += 1

    print(f"Количество слов в строке {next(c) + 1} - {words}.")

