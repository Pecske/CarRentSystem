from data.CarRental import CarRental
from dto.CarRentalView import CarRentalView
from utils.FactoryBase import FactoryBase
from utils.CarFactory import CarFactory


class CarRentalFactory(FactoryBase):
    def __init__(self) -> None:
        super().__init__()

    def map_data_to_view(data: CarRental) -> CarRentalView:
        view = CarRentalView(name=data.get_name(), id=data.get_id())
        for car in data.get_cars():
            view.add_car(CarFactory.map_data_to_view(car))
        return view

    def map_view_to_data(view: CarRentalView) -> CarRental:
        data = CarRental(name=view.get_name(), id=view.get_id())
        for car_view in view.get_cars():
            data.add_car(CarFactory.map_view_to_data(car_view))
        return data
