class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


person1 = Position("Andrey", "Sufude", "Captain", 400000, 50000)
person2 = Position("Denis", "Ivanov", "First officer", 200000, 35000)
person3 = Position("Lena", "Ermolaeva", "Flight attendant", 100000, 20000)

print(f"{person1.get_full_name()}, position - {person1.position}, income - {person1.get_total_income()}rub.")
print(f"{person2.get_full_name()}, position - {person2.position}, income - {person2.get_total_income()}rub.")
print(f"{person3.get_full_name()}, position - {person3.position}, income - {person3.get_total_income()}rub.")