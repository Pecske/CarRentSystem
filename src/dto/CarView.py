from dto.ViewBase import ViewBase
from utils.CarCategory import CarCategory


class CarView(ViewBase):
    def __init__(
        self,
        category: CarCategory,
        id: int,
        licence_plate: str,
        type: str,
        rental_fee: int,
    ):
        super().__init__(id)
        self.category = category
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee

    def get_category(self) -> CarCategory:
        return self.category

    def get_id(self):
        return super().get_id()

    def get_licence_plate(self) -> str:
        return self.licence_plate

    def get_type(self) -> str:
        return self.type

    def get_rental_fee(self) -> int:
        return self.rental_fee

    def set_id(self, value):
        return super().set_id(value)

    def set_category(self, value: CarCategory) -> None:
        self.category = value

    def set_licence_plate(self, value: str) -> None:
        self.licence_plate = value

    def set_type(self, value: str) -> None:
        self.type = value

    def set_rental_fee(self, value: int) -> None:
        self.rental_fee = value

    def print(self):
        return f"[{self.get_id()}] {self.get_rental_fee()}"

    def __str__(self):
        return f"Id: {self.get_id()} - Category: {self.get_category()} - Licence Plate: {self.get_licence_plate()} - Type: {self.get_type()} - Rental Fee: {self.get_rental_fee()}"
