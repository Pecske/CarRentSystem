from utils.CarCategory import CarCategory


class CarView:
    def __init__(
        self,
        category: CarCategory,
        id: int,
        licence_plate: str,
        type: str,
        rental_fee: int,
    ):
        self.category = category
        self.id = id
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee

    def get_category(self) -> CarCategory:
        return self.category

    def get_id(self) -> int | None:
        return self.id

    def get_licence_plate(self) -> str:
        return self.licence_plate

    def get_type(self) -> str:
        return self.type

    def get_rental_fee(self) -> int:
        return self.rental_fee

    def set_category(self, value: CarCategory) -> None:
        self.category = value

    def set_licence_plate(self, value: str) -> None:
        self.licence_plate = value

    def set_type(self, value: str) -> None:
        self.type = value

    def set_rental_fee(self, value: int) -> None:
        self.rental_fee = value

    def __str__(self):
        return f"Id: {self.get_id()} - Category: {self.get_category()} - Licence Plate: {self.get_licence_plate()} - Type: {self.get_type()} - Rental Fee: {self.get_rental_fee()}"
