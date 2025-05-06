from data.PassengerCar import PassengerCar
from data.Truck import Truck
from data.Car import Car
from data.Money import Money
from utils.FactoryBase import FactoryBase
from utils.CarCategory import CarCategory
from dto.CarView import CarView


class CarFactory(FactoryBase):

    def __init__(self) -> None:
        super().__init__()

    def map_data_to_view(data: Car) -> CarView:
        category: CarCategory | None = None
        if isinstance(data, PassengerCar):
            category = CarCategory.Passenger
        else:
            category = CarCategory.Truck
        rental_money = data.get_rental_fee()
        return CarView(
            category,
            data.get_licence_plate(),
            data.get_type(),
            rental_money.get_amount(),
            rental_money.get_currency(),
            data.get_id(),
        )

    def map_view_to_data(view: CarView) -> Car:
        category = view.get_category()
        rental_money = Money(view.get_rental_fee(), view.get_rental_currency())
        if category == CarCategory.Passenger:
            return PassengerCar(
                view.get_licence_plate(),
                view.get_type(),
                rental_money,
                view.get_id(),
            )
        else:
            return Truck(
                view.get_licence_plate(),
                view.get_type(),
                rental_money,
                view.get_id(),
            )
