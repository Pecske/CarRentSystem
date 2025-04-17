from data.PassengerCar import PassengerCar
from data.Truck import Truck
from data.Car import Car
from utils.FactoryBase import FactoryBase
from utils.CarCategory import CarCategory
from dto.CarView import CarView


class CarFactory(FactoryBase):

    def __init__(self):
        super().__init__()

    def from_data_to_view(data: Car) -> CarView:
        category: CarCategory | None = None
        if isinstance(data, PassengerCar):
            category = CarCategory.PassengerCar
        else:
            category = CarCategory.Truck
        return CarView(
            category,
            data.get_id(),
            data.get_licence_plate(),
            data.get_type(),
            data.get_rental_fee(),
        )

    def from_view_to_data(view: CarView) -> Car:
        category = view.get_category()
        if category == CarCategory.PassengerCar:
            return PassengerCar(
                view.get_id(),
                view.get_licence_plate(),
                view.get_type(),
                view.get_rental_fee(),
            )
        else:
            return Truck(
                view.get_id(),
                view.get_licence_plate(),
                view.get_type(),
                view.get_rental_fee(),
            )
