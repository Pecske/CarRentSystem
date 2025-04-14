from abc import abstractmethod
from data.DataBase import DataBase


class Car(DataBase):

    def __init__(self, licence_plate: str, type: str, rental_fee: int):
        super().__init__()
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee
        pass

    @abstractmethod
    def get_licence_plate(self) -> str:
        return self.licence_plate

    @abstractmethod
    def get_type(self) -> str:
        return self.type

    @abstractmethod
    def get_rental_fee(self) -> int:
        return self.rental_fee

    @abstractmethod
    def set_licence_plate(self, value: str) -> None:
        self.licence_plate = value

    @abstractmethod
    def set_type(self, value: str) -> None:
        self.type = value

    @abstractmethod
    def set_rental_fee(self, value: int) -> None:
        self.rental_fee = value

    def __eq__(self, other) -> bool:
        if isinstance(other, Car):
            return (
                other.licence_plate == self.licence_plate
                and other.type == self.type
                and other.rental_fee == self.rental_fee
            )
        return False

    def __hash__(self):
        return hash(
            7 * hash(self.licence_plate) * hash(self.type) * hash(self.rental_fee)
        )

    def __str__(self) -> str:
        return "Licence plate: {}\nType: ,{}\nRental Fee: ".format(
            self.licence_plate, self.type, self.rental_fee
        )
