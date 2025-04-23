from dto.CarView import CarView
from datetime import datetime
from utils.Serializeable import Serializeable

ID = "id"
CAR = "car"
DATE = "date"


class RentView(Serializeable):

    def __init__(self, car_view: CarView, rental_time: datetime, id: int | None = None):
        super().__init__(id)
        self.car_view = car_view
        self.rental_time = rental_time

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def get_car_view(self) -> CarView:
        return self.car_view

    def set_car_view(self, value: CarView) -> None:
        self.car_view = value

    def get_rental_time(self) -> datetime:
        return self.rental_time

    def set_rental_time(self, value: datetime) -> None:
        self.rental_time = value

    def print(self):
        return f"{self.get_id()} {self.get_rental_time()}\t{self.get_car_view()}"

    def serialize(self):
        return {
            CAR: self.get_car_view().serialize(),
            DATE: str(self.get_rental_time()),
            ID: self.get_id(),
        }

    def de_serialize(dct: dict[str, str]):
        try:
            id = int(dct.get(ID)) if dct.get(ID) else None
            car = CarView.de_serialize(dct.get(CAR)) if dct.get(CAR) else None
            date = dct.get(DATE) if dct.get(DATE) else None
            year, month, day = map(int, date.split("-"))
            reserved_date = datetime(year=year, month=month, day=day)
            return RentView(car, reserved_date, id)
        except Exception:
            raise Exception("Deserialization of rent failed!")

    def __str__(self):
        return f"{self.get_id()} - {self.get_rental_time()} - {self.get_car_view()}"
