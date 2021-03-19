class DataError(Exception):
    def __init__(self, text="Ошибка данных"):
        self.text = text

    def _str_(self):
        print(self.text)


class MyNoneType(DataError):
    def __init__(self, text="Ошибка данных"):
        self.text = text


class WrongNumber(DataError):
    def __init__(self, text="Введите 1 или 2!!"):
        self.text = text


class MyValueError(DataError):
    def __init__(self, text="Введите 1 или 2!!"):
        self.text = text


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.base = {}
        self.given_product = {}
        self.count = {"printer": 0, "xerox": 0, "scanner": 0}

    def __str__(self):
        return f"Склад {self.name}"

    def in_base(self, number):
        return True if number in self.base else False

    def get_stat(self):
        print(f"Сейчас на {self.name}:\n\
                Принтеры:{self.count.get('printer')}\n\
                Ксероксы:{self.count.get('xerox')}\n\
                Сканеры:{self.count.get('scanner')}")

    def get_product(self, equipment):
        self.base.update({equipment.serial_number: [equipment]})
        self.count[equipment.eq_type] += 1
        print(f"Получено на склад {self.name} : {equipment}")

    def give_product(self, equipment, other):
        self.delete_product(equipment)
        other.get_product(equipment)

    def delete_product(self, equipment):
        if equipment.serial_number in self.base:
            del self.base[equipment.serial_number]
            self.given_product.update({equipment.serial_number: [equipment]})
            self.count[equipment.eq_type] -= 1
            print(f"Отдано со склада {self.name} : {equipment}")
        else:
            print(f"Товар с данным серийным номером отсутствует на складе {self.name}.")

    def show_product(self):
        print(f"Сейчас на данном складе находятся следующие устройства:")
        for i in self.base:
            print(f"{self.base[i][0]}")

    def add_to_warehouse(self):
        print("1 - добавить принтер, 2 - добавить ксерокс, 3 - добавить сканер:")
        prod_type = check_input(4)
        if prod_type == "1":
            product = Printer(is_valid(input("Введите стоимость товара:\n")),
                              input("Введите модель товара:\n"),
                              is_valid(input("Введите разрешение печати:\n")),
                              is_valid(input("Введите серийный номер товара:\n")))
            self.get_product(product)
        if prod_type == "2":
            product = Xerox(is_valid(input("Введите стоимость товара:\n")),
                            input("Введите модель товара:\n"),
                            is_valid(input("Введите разрешение печати:\n")),
                            is_valid(input("Введите серийный номер товара:\n")))
            self.get_product(product)
        if prod_type == "3":
            product = Scanner(is_valid(input("Введите стоимость товара:\n")),
                              input("Введите модель товара:\n"),
                              is_valid(input("Введите разрешение печати:\n")),
                              is_valid(input("Введите серийный номер товара:\n")))
            self.get_product(product)

    def delete_from(self, num):
        ab = self.base.get(num)
        del self.base[num]
        if ab[0].eq_type == 'scanner':
            self.count['scanner'] -= 1
            print(f"Вы удалили со склада {self.name}: {ab[0]}")
        if ab[0].eq_type == 'printer':
            self.count['printer'] -= 1
            print(f"Вы удалили со склада {self.name}: {ab[0]}")
        if ab[0].eq_type == 'xerox':
            self.count['xerox'] -= 1
            print(f"Вы удалили со склада {self.name}: {ab[0]}")

    def end_program(self):
        print(f"Выполнено!\n1 - показать количество товаров на {self.name} по категориям,\n2 - полный список товаров ")
        inp = check_input(3)
        if inp == "1":
            self.get_stat()
        if inp == "2":
            self.show_product()

    def pass_to(self, num, other):
        try:
            if not self.in_base(num):
                raise MyNoneType("Товар отсутствует на складе")
        except MyNoneType as err1:
            print(err1)
        else:
            ab = self.base.get(num)
            other.get_product(ab[0])
            self.delete_from(num)

    def go_program(self):
        print(f"Выбран склад {self.name}")
        print(f"1 - добавить товар на склад\n2 - удалить\n3 - передать на другой склад"
              f"\n4 - посмотреть количество товаров по категориям"
              f"\n5 - посмотреть список товаров на складе\n6 - перезапуск")

        req = check_input(7)

        if req == "1":
            self.add_to_warehouse()
            self.end_program()
        if req == "2":
            print("Введите серийный номер товара:")
            res = is_valid(input())
            if self.in_base(res):
                self.delete_from(res)
                self.end_program()
            else:
                print(f"Товар с данным номером отсутствует на складе {self.name}")
        if req == "6":
            print("Программа перезапушена!")
        if req == "4":
            self.get_stat()
        if req == "5":
            self.show_product()
        if req == "3":
            print("Введите серийный номер товара:")
            res = is_valid(input())
            if self.name == '1101':
                self.pass_to(res, b)
            else:
                self.pass_to(res, a)


class Equipment:
    def __init__(self, price, model, serial_number):
        self.model = model
        self.price = is_valid(price)
        self.serial_number = is_valid(serial_number)

    def __str__(self):
        return f"Устройство: модель: {self.model}, стоимость: {self.price}, серийный номер: {self.serial_number}"

    def __repr__(self):
        return self.__str__()


class Printer(Equipment):
    def __init__(self, price, model, print_resolution, serial_number, eq_type="printer"):
        super().__init__(price, model, serial_number)
        self.print_resolution = print_resolution
        self.eq_type = eq_type

    def __str__(self):
        return f"{self.eq_type}, модель: {self.model}, стоимость: {self.price}, серийный номер: {self.serial_number}"


class Xerox(Equipment):
    def __init__(self, price, model, print_resolution, serial_number, eq_type="xerox"):
        super().__init__(price, model, serial_number)
        self.print_resolution = print_resolution
        self.eq_type = eq_type

    def __str__(self):
        return f"{self.eq_type}, модель: {self.model}, стоимость: {self.price}, серийный номер: {self.serial_number}"


class Scanner(Equipment):
    def __init__(self, price, model, print_resolution, serial_number, eq_type="scanner"):
        super().__init__(price, model, serial_number)
        self.print_resolution = print_resolution
        self.eq_type = eq_type

    def __str__(self):
        return f"{self.eq_type}, модель: {self.model}, стоимость: {self.price}, серийный номер: {self.serial_number}"


def is_valid(num):
    while True:
        try:
            if not num.isdigit():
                raise DataError("Необходимо ввести числовое значение!")
        except DataError as error1:
            print(error1)
            num = input()
        else:
            return num


def check_input(max_value=3):
    while True:
        inp = input()
        try:
            if not inp.isdigit():
                raise MyValueError("Ошибка! Вы ввели не цифры!")
        except MyValueError as value_err:
            print(value_err)
        else:
            try:
                if int(inp) not in range(1, max_value):
                    raise WrongNumber(f"Ошибка! Необходимо использовать цифры до {max_value-1}!")
            except WrongNumber as err:
                print(err)
            else:
                return inp


a = Warehouse('1101')
b = Warehouse('1102')

scan1 = Printer('12000', 'sdf3', 345, '0001')
scan2 = Scanner('5100', 'sdf', 345, '0002')
scan3 = Xerox('7000', 'sd', 345, '0003')

a.get_product(scan1)
a.get_product(scan3)
a.get_product(scan2)
a.give_product(scan1, b)
print("\n")

while True:
    print(f"Выберите склад:\n1 - {a.name}\n2 - {b.name}")
    answer = check_input(3)
    if answer == "1":
        a.go_program()
    if answer == "2":
        b.go_program()
    print("\n")
