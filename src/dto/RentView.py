from dto.ViewBase import ViewBase
from dto.CarView import CarView
from datetime import datetime


class RentView(ViewBase):
    def __init__(self, id: int, car_view: CarView, rental_time: datetime):
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
        return f"{self.get_rental_time()}\t{self.get_car_view()}"
