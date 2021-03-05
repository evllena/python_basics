import colorama
from colorama import Fore

colorama.init()


class Colors:
    blue = Fore.BLUE
    red = Fore.RED
    green = Fore.GREEN


class Stationary:
    def __int__(self, title, color):
        self.title = title
        self.color = color

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def __init__(self, title, color):
        super().__int__(title, color)

    def draw(self):
        print(self.color + '\033[1mЗапуск отрисовки\033[0m')


class Pencil(Stationary):
    def __init__(self, title, color):
        super().__int__(title, color)

    def draw(self):
        print(self.color + 'Запуск отрисовки\033[0m')


class Handle(Stationary):
    def __init__(self, title, color):
        super().__int__(title, color)

    def draw(self):
        print(self.color + '\033[4m\033[1mЗапуск отрисовки\033[0m')


pen = Pen("Red pen", Colors.red)
print(f"Trying to draw with a {pen.title}:")
pen.draw()
print()

pencil = Pencil("Green pencil", Colors.green)
print(f"Trying to draw with a {pencil.title}:")
pencil.draw()
print()

handle = Handle("Blue handle", Colors.blue)
print(f"Trying to draw with a {handle.title}:")
handle.draw()