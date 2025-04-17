from dto.CarView import CarView


class CarRentalView:
    def __init__(self, id: int, name: str, cars: list[CarView]) -> None:
        self.id = id
        self.name = name
        self.cars = cars

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_cars(self) -> list[CarView]:
        return self.cars

    def set_id(self, value: int) -> None:
        self.id = value

    def set_name(self, value: str) -> None:
        self.name = value

    def set_cars(self, value: list[CarView]) -> None:
        self.cars = value

    def add_car(self, car: CarView) -> None:
        self.cars.append(car)

    def remove_car(self, car: CarView) -> None:
        self.cars.remove(car)
