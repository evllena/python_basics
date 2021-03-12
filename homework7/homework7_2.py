from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return round(self.tissue_consumption + other.tissue_consumption)


class Coat(Clothes):

    @property
    def tissue_consumption(self):
        return round(self.parameter/6.5 + 0.5)


class Suit(Clothes):

    @property
    def tissue_consumption(self):
        return round(2 * self.parameter + 0.3)


coat1 = Coat(42)
suit1 = Suit(179)

print(f"Consumption of tissue for this coat is {coat1.tissue_consumption} m.")
print(f"Consumption of tissue for this suit is {suit1.tissue_consumption} m.")

print(f"General consumption of tissue for this clothes is {coat1 + suit1} m.")