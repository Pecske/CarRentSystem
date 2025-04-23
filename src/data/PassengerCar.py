from data.Car import Car
from data.Money import Money


class PassengerCar(Car):
    def __init__(
        self, licence_plate: str, type: str, rental_fee: Money, id: int | None = None
    ):
        super().__init__(licence_plate, type, rental_fee, id)

    def get_id(self):
        return super().get_id()

    def get_licence_plate(self):
        return super().get_licence_plate()

    def get_type(self):
        return super().get_type()

    def get_rental_fee(self):
        return super().get_rental_fee()

    def set_id(self, value):
        return super().set_id(value)

    def set_licence_plate(self, value):
        return super().set_licence_plate(value)

    def set_type(self, value):
        return super().set_type(value)

    def set_rental_fee(self, value):
        return super().set_rental_fee(value)

    def __hash__(self):
        return 7 * super().__hash__()
