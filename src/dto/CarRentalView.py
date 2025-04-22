from dto.ViewBase import ViewBase
from dto.CarView import CarView


class CarRentalView(ViewBase):
    def __init__(self, id: int, name: str, cars: list[CarView]) -> None:
        super().__init__(id)
        self.name = name
        self.cars = cars

    def get_id(self):
        return super().get_id()

    def get_name(self) -> str:
        return self.name

    def get_cars(self) -> list[CarView]:
        return self.cars

    def set_id(self, value):
        return super().set_id(value)

    def set_name(self, value: str) -> None:
        self.name = value

    def set_cars(self, value: list[CarView]) -> None:
        self.cars = value

    def add_car(self, car: CarView) -> None:
        self.cars.append(car)

    def remove_car(self, car: CarView) -> None:
        self.cars.remove(car)

    def print(self):
        return f"[{self.get_id()}] {self.get_name()}"
