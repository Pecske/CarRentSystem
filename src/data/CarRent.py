from data.Car import Car
from data.DataBase import DataBase


class CarRent(DataBase):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.cars: list[Car] = list()
        pass

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)
