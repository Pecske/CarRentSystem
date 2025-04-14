from data.Car import Car
from data.DataBase import DataBase


class CarRental(DataBase):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.cars: list[Car] = list()

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        super().set_id(value)

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> None:
        self.name = value

    def get_cars(self) -> list[Car]:
        return self.cars

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
    
    def remove_car(self, car: Car) ->None:
        self.cars.remove(car)
