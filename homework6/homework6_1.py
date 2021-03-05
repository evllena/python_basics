from time import sleep


class TrafficLight:
    _color = "Отсутствует"

    def running(self):
        self._color = "Красный"
        print(f'Цвет светофора - {self._color}')
        sleep(7)
        self._color = "Желтый"
        print(f'Цвет светофора - {self._color}')
        sleep(2)
        self._color = "Зеленый"
        print(f'Цвет светофора - {self._color}')
        sleep(4)


traffic_light = TrafficLight()
while True:
    traffic_light.running()

