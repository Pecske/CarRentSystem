from data.Car import Car
from datetime import date
from data.DataBase import DataBase


class Rent(DataBase):
    def __init__(self, car: Car, rental_time: date, id: int | None = None):
        super().__init__(id)
        self.car = car
        self.rental_time = rental_time

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def get_car(self) -> Car:
        return self.car

    def set_car(self, value: Car) -> None:
        self.car = value

    def get_rental_time(self) -> date:
        return self.rental_time

    def set_rental_time(self, value: date) -> None:
        self.rental_time = value
