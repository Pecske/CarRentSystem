from utils.CarCategory import CarCategory


class CarWrapper:

    
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
        self.error_collection: list[str] = list()

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

    def get_error_collection(self) -> list[str]:
        return self.error_collection

    def add_error(self, error: str) -> None:
        self.error_collection.append(error)
