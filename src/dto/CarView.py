from utils.CarCategory import CarCategory
from utils.Serializeable import Serializeable

ID = "id"
CATEGORY = "category"
LICENCE_PLATE = "licence_plate"
TYPE = "type"
RENTAL_FEE = "rental_fee"
RENTAL_CURRENCY = "rental_currency"


class CarView(Serializeable):

    def __init__(
        self,
        category: CarCategory,
        licence_plate: str,
        type: str,
        rental_fee: int,
        rental_currency: str,
        id: int | None = None,
    ):
        super().__init__(id)
        self.category = category
        self.licence_plate = licence_plate
        self.type = type
        self.rental_fee = rental_fee
        self.rental_currency = rental_currency

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

    def get_rental_currency(self) -> str:
        return self.rental_currency

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

    def set_rental_currency(self, value: str) -> None:
        self.rental_currency = value

    def print(self):
        return f"[{self.get_id()}] {self.get_category().name} {self.get_licence_plate()} {self.get_type()} {self.get_rental_fee()} {self.get_rental_currency()}"

    def serialize(self):
        return {
            CATEGORY: str(self.get_category()),
            LICENCE_PLATE: self.get_licence_plate(),
            TYPE: self.get_type(),
            RENTAL_FEE: str(self.get_rental_fee()),
            RENTAL_CURRENCY: self.get_rental_currency(),
            ID: str(self.get_id()),
        }

    def de_serialize(dct: dict[str, str]):
        try:
            id = int(dct.get(ID)) if dct.get(ID) else None
            category = CarCategory[dct.get(CATEGORY)] if dct.get(CATEGORY) else None
            licence_plate = dct.get(LICENCE_PLATE) if dct.get(LICENCE_PLATE) else None
            type = dct.get(TYPE) if dct.get(TYPE) else None
            rental_fee = int(dct.get(RENTAL_FEE)) if dct.get(RENTAL_FEE) else None
            rental_currency = (
                dct.get(RENTAL_CURRENCY) if dct.get(RENTAL_CURRENCY) else None
            )
            return CarView(
                category, licence_plate, type, rental_fee, rental_currency, id
            )
        except Exception:
            raise Exception("Deserialization of car failed!")

    def __eq__(self, other):
        if isinstance(other, CarView):
            return (
                other.get_licence_plate() == self.get_licence_plate()
                and other.get_type() == self.get_type()
                and other.get_rental_fee() == self.get_rental_fee()
                and other.get_rental_currency() == self.get_rental_currency()
            )
        return False

    def __hash__(self):
        return (
            hash(self.get_category())
            * hash(self.get_licence_plate())
            * hash(self.get_type())
            * hash(self.get_rental_fee())
            * hash(self.get_rental_currency())
        )

    def __str__(self):
        return f"Category: {self.get_category().name} - Licence Plate: {self.get_licence_plate()} - Type: {self.get_type()} - Rental Fee: {self.get_rental_fee()} {self.get_rental_currency()}"
