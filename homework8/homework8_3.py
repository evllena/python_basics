class MyValueError(Exception):
    def __init__(self, text):
        self.text = text


new_list = []
while True:
    item = input("Введите целое число или F для завершения: ")
    if item == 'F':
        print(new_list)
        break
    try:
        if not item.isdigit():
            raise MyValueError('Значение не будет добавлено в список, так как не является целым числом!')
    except MyValueError as my_error:
        print(my_error)
    else:
        new_list.append(item)


