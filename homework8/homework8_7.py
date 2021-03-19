class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.num = "a + b * i"

    def __str__(self):
        return f"x = {self.a} + {self.b} * i"

    def __add__(self, other):
        print(f'Сумма чисел равна:')
        return f"x = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        print(f'Произведение чисел равно:')
        return f"x = {(self.a * other.a) - (self.b * other.b)} + {(self.a * other.b) + (self.b * other.a)} * i"


number1 = ComplexNumber(7, -9)
number2 = ComplexNumber(-2, 15)
print(number1)
print(number2)
print(number1 + number2)
print(number1 * number2)
print(number2 * number1)
