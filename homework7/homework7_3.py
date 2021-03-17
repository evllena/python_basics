class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return f"Сумма клеток равна {self.num + other.num}"

    def __sub__(self, other):
        return f"Разность клеток равна {self.num - other.num}" if self.num - other.num > 0 \
            else "Разность клеток не может быть отрицательной или равна 0!"

    def __mul__(self, other):
        return f"Произведение клеток равно {self.num * other.num}"

    def __floordiv__(self, other):
        return f"Целочисленное деление клеток равно {self.num // other.num}"

    def __truediv__(self, other):
        return f"Нецелочисленное деление клеток с округлением до целого равно {round(self.num / other.num)}"

    def make_order(self, row):
        print(f"\nОрганизация {self.num} ячеек по рядам из {row} звездочек:")
        return '\n'.join(['*' * row for _ in range(self.num // row)]) + '\n' + '*' * (self.num % row)


cell1 = Cell(9)
cell2 = Cell(18)

print(f"Для клеток со значениями {cell1} и {cell2}:\n")
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1 // cell2)
print(f"\nДля клеток со значениями {cell2} и {cell1}:\n")
print(cell2 - cell1)
print(cell2 // cell1)
print(cell2 / cell1)
print('\n' + cell1.make_order(4))
print('\n' + cell2.make_order(8))
