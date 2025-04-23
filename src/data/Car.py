from data.DataBase import DataBase
from data.Money import Money


class Car(DataBase):

    def __init__(
        self, licence_plate: str, type: str, rental_fee: Money, id: int | None = None
    ) -> None:
        super().__init__(id)
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee

    def get_licence_plate(self) -> str:
        return self.licence_plate

    def get_type(self) -> str:
        return self.type

    def get_rental_fee(self) -> Money:
        return self.rental_fee

    def set_licence_plate(self, value: str) -> None:
        self.licence_plate = value

    def set_type(self, value: str) -> None:
        self.type = value

    def set_rental_fee(self, value: Money) -> None:
        self.rental_fee = value

    def __eq__(self, other) -> bool:
        if isinstance(other, Car):
            return (
                other.licence_plate == self.licence_plate
                and other.type == self.type
                and other.rental_fee == self.rental_fee
            )
        return False

    def __hash__(self) -> int:
        return hash(self.licence_plate) * hash(self.type) * hash(self.rental_fee)

    def __str__(self) -> str:
        return f"Licence plate: {self.licence_plate}\nType: ,{self.type}\nRental Fee: {self.rental_fee}"
