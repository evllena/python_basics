from time import sleep
import colorama
from colorama import Fore
colorama.init()


class TrafficLight:
    _color = "Отсутствует"

    def running(self):
        self._color = "Красный"
        print(Fore.RED + f'Цвет светофора - {self._color}')
        sleep(7)
        self._color = "Желтый"
        print(Fore.YELLOW + f'Цвет светофора - {self._color}')
        sleep(2)
        self._color = "Зеленый"
        print(Fore.GREEN + f'Цвет светофора - {self._color}')
        sleep(4)


traffic_light = TrafficLight()
while True:
    traffic_light.running()
