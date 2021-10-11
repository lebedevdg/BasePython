"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class CreationException(Exception):
    pass


class LowFuelError(CreationException):
    def __init__(self):
        super().__init__(f"Низкий уровень топлива")


class NotEnoughFuel(CreationException):
    def __init__(self):
        super().__init__(f"Недостаточно топлива")


class CargoOverload(CreationException):
    def __init__(self):
        super().__init__(f"Перегруз")
