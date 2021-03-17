class MyValueError(Exception):
    def __init__(self, text):
        self.text = text


def is_number(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


new_list = []
while True:
    item = input("Введите целое число или F для завершения: ")
    if item == 'F':
        print(f"Так выглядит ваш список: ")
        for n in new_list:
            print(n, end=' ')
        break
    try:
        if not is_number(item):
            raise MyValueError('Значение не будет добавлено в список, так как не является целым числом!')
    except MyValueError as my_error:
        print(my_error)
    else:
        new_list.append(item)


