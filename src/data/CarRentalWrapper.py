from data.WrapperBase import WrapperBase
from data.CarRental import CarRental


class CarRentalWrapper(WrapperBase):
    def __init__(self, rental: CarRental):
        super().__init__()
        self.rental = rental

    def add_error(self, error):
        return super().add_error(error)

    def get_errors(self):
        return super().get_errors()

    def get_rental(self) -> CarRental:
        return self.rental

    def set_rental(self, rental: CarRental) -> None:
        self.rental = rental
