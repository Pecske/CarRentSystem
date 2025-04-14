from utils.CarCategory import CarCategory
from data.WrapperBase import WrapperBase


class CarWrapper(WrapperBase):

    def __init__(
        self,
        category: CarCategory,
        id: int,
        licence_plate: str,
        type: str,
        rental_fee: int,
    ):
        super().__init__()
        self.category = category
        self.id = id
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee

    def get_errors(self):
        return super().get_errors()

    def add_error(self, error: str):
        super().add_error(error)

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
