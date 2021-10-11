from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return
        if self.fuel <= 0:
            raise LowFuelError
        self.started = True
        return

    def move(self, distanse):
        if (distanse * self.fuel_consumption) > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= distanse * self.fuel_consumption
            return

