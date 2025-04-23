from data.Car import Car
from data.DataBase import DataBase


class CarRental(DataBase):

    def __init__(
        self, name: str, cars: list[Car] = list(), id: int | None = None
    ) -> None:
        super().__init__(id)
        self.name = name
        self.cars = cars

    def get_id(self) -> int:
        return super().get_id()

    def set_id(self, value) -> None:
        super().set_id(value)

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> None:
        self.name = value

    def get_cars(self) -> list[Car]:
        return self.cars

    def set_cars(self, value: list[Car]) -> None:
        self.cars = value

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        self.cars.remove(car)
