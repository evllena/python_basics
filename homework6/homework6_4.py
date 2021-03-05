class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.isPolice = is_police

    def go(self):
        print(f"{self.name} is on its way!")

    def stop(self):
        print(f"{self.name} stopped.")

    def turn(self, direction):
        if direction < 0:
            print(f"{self.name} turns left.")
        else:
            print(f"{self.name} turns right.")

    def show_speed(self):
        return f"Car speed is {self.speed} km/hr."


class TownCar(Car):
    def show_speed(self):
        return f"{self.name} speed is {self.speed} km/hr." \
            if self.speed <= 60 else f"{self.name} speed is too high! Its {self.speed} km/hr."


class SportCar(Car):
    year = 1962


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} speed is {self.speed} km/hr." \
            if self.speed <= 40 else f"{self.name} speed is too high! Its {self.speed} km/hr."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, "White", "Toyota")
print(f"This car is a {town_car.name} and its color is {town_car.color}.")
town_car.go()
town_car.turn(-1)
print(town_car.show_speed())
town_car.stop()
print()

work_truck = WorkCar(65, "Purple", "Truck")
print(f"This car is a {work_truck.name} and its color is {work_truck.color}.")
work_truck.go()
work_truck.turn(7)
print(work_truck.show_speed())
work_truck.stop()
print()

sport_car = SportCar(140, "Red", "Mustang")
print(f"This car is a {sport_car.name} and its color is {sport_car.color}.")
print(f"{sport_car.name} was made in {sport_car.year}.")
print("This is a police car, be aware!!!") if sport_car.isPolice else print("Don't worry. It is not a police car.")
print()

police = PoliceCar(120, "Black&White", "Police car # 1")
print(f"This car is a {police.name} and its color is {police.color}.")
police.go()
police.turn(1)
print(police.show_speed())
police.stop()
if police.isPolice:
    print("This is a police car, be aware!!!")
