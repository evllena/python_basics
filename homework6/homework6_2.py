class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def count_mass(self):
        return f"{self.length}м * {self.width}м * 25кг * 5см = {(self.length * self.width * 5 * 25) / 1000}т"


lost_highway = Road(1500, 5)
print(lost_highway.count_mass())