from data.WrapperBase import WrapperBase
from data.Rent import Rent


class RentWrapper(WrapperBase):
    def __init__(self, rent: Rent):
        super().__init__()
        self.rent = rent

    def get_errors(self):
        return super().get_errors()

    def add_error(self, error):
        return super().add_error(error)

    def get_rent(self) -> Rent:
        return self.rent

    def set_rent(self, value: Rent) -> None:
        self.rent = value
