from utils.FactoryBase import FactoryBase
from data.Rent import Rent
from dto.RentView import RentView
from utils.CarFactory import CarFactory


class RentFactory(FactoryBase):

    def __init__(self) -> None:
        super().__init__()

    def map_data_to_view(data: Rent) -> RentView:
        return RentView(
            CarFactory.map_data_to_view(data.get_car()),
            data.get_rental_time(),
            data.get_id(),
        )

    def map_view_to_data(view: RentView) -> Rent:
        return Rent(
            CarFactory.map_view_to_data(view.get_car_view()),
            view.get_rental_time(),
            view.get_id(),
        )
