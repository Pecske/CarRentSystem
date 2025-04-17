from utils.FactoryBase import FactoryBase
from data.Rent import Rent
from dto.RentView import RentView
from utils.CarFactory import CarFactory


class RentFactory(FactoryBase):

    def __init__(self):
        super().__init__()

    def from_data_to_view(data: Rent) -> RentView:
        return RentView(
            data.get_id(),
            CarFactory.from_data_to_view(data.get_car()),
            data.get_rental_time(),
        )

    def from_view_to_data(view: RentView) -> Rent:
        return Rent(
            view.get_id(),
            CarFactory.from_view_to_data(view.get_car_view()),
            view.get_rental_time(),
        )
