from utils.FactoryBase import FactoryBase
from data.Rent import Rent
from dto.RentView import RentView
from utils.CarFactory import CarFactory


class RentFactory(FactoryBase):

    def __init__(self):
        super().__init__()

    def from_data_to_view(data: Rent) -> RentView:
        return RentView(
            CarFactory.from_data_to_view(data.get_car()),
            data.get_rental_time(),
            data.get_id(),
        )

    def from_view_to_data(view: RentView) -> Rent:
        return Rent(
            CarFactory.from_view_to_data(view.get_car_view()),
            view.get_rental_time(),
            view.get_id(),
        )
