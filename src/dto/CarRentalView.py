from dto.CarView import CarView
from utils.Serializeable import Serializeable

ID = "id"
NAME = "name"
CARS = "cars"


class CarRentalView(Serializeable):

    def __init__(
        self, name: str, cars: list[CarView] = None, id: int | None = None
    ) -> None:
        super().__init__(id)
        self.name = name
        if cars is None:
            self.cars = list()
        else:
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

    def serialize(self):
        serialized_cars: list[dict[str, str]] = list()
        if len(self.get_cars()) > 0:
            for car in self.get_cars():
                serialized_cars.append(car.serialize())

        return {NAME: self.get_name(), CARS: serialized_cars, ID: str(self.get_id())}

    def de_serialize(dct: dict[str, str]):
        try:
            id = int(dct.get(ID)) if dct.get(ID) else None
            name = dct.get(NAME) if dct.get(NAME) else None
            cars = dct.get(CARS) if dct.get(CARS) else list()
            de_serialized_cars: list[CarView] = list()
            if len(cars) > 0:
                for car in cars:
                    de_serialized_cars.append(CarView.de_serialize(dct=car))
            return CarRentalView(name, de_serialized_cars, id)
        except Exception:
            raise Exception("Deserialization of car rental failed!")

    def __str__(self):
        result = f"{self.get_id()} {self.get_name()}"
        if len(self.get_cars()) > 0:
            for car in self.get_cars():
                result += "\n" + str(car)

        return result
