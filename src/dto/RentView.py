from dto.CarView import CarView
from datetime import datetime


class RentView:
    def __init__(self, id: int, car_view: CarView, rental_time: datetime):
        self.id = id
        self.car_view = car_view
        self.rental_time = rental_time

    def get_id(self) -> int:
        return self.id

    def set_id(self, value: int) -> None:
        self.id = value

    def get_car_view(self) -> CarView:
        return self.car_view

    def set_car_view(self, value: CarView) -> None:
        self.car_view = value

    def get_rental_time(self) -> datetime:
        return self.rental_time

    def set_rental_time(self, value: datetime) -> None:
        self.rental_time = value
