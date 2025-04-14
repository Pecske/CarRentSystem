from data.CarWrapper import CarWrapper
from data.PassengerCar import PassengerCar
from data.Truck import Truck
from data.Car import Car
from utils.CarCategory import CarCategory


class CarFactory:

    def __init__(self):
        pass

    def create_car(wrapper: CarWrapper) -> Car:
        category = wrapper.get_category()
        if category == CarCategory.PassengerCar:
            return PassengerCar(
                wrapper.get_id(),
                wrapper.get_licence_plate(),
                wrapper.get_type(),
                wrapper.get_rental_fee(),
            )
        else:
            return Truck(
                wrapper.get_id(),
                wrapper.get_licence_plate(),
                wrapper.get_type(),
                wrapper.get_rental_fee(),
            )

    def create_wrapper(car: Car) -> CarWrapper:
        category: CarCategory | None = None
        if isinstance(car, PassengerCar):
            category = CarCategory.PassengerCar
        else:
            category = CarCategory.Truck
        return CarWrapper(
            category,
            car.get_id(),
            car.get_licence_plate(),
            car.get_type(),
            car.get_rental_fee(),
        )
