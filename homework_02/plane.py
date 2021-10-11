"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if (cargo + self.cargo) >= self.max_cargo:
            # print("Перегруз =", (cargo + self.cargo), "при макс:", self.max_cargo)
            raise CargoOverload
        else:
            self.cargo += cargo
            # print("weight =", cargo, "self.cargo =", self.cargo, "Сложение weight + self.cargo =", cargo + self.cargo)
            return self.cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        # print("Исходный вес:", cargo)
        return cargo


# bmw = Plane(0, 0, 0, 3000)
# bmw.load_cargo(4000)
# bmw.remove_all_cargo()
