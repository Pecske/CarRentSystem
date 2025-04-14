from service.CarService import CarService
from data.CarWrapper import CarWrapper
from utils.CarFactory import CarFactory


class CarController:
    def __init__(self):
        self.service = CarService()

    def create_or_update_car(self, wrapper: CarWrapper) -> CarWrapper:
        if wrapper.get_category() == None:
            wrapper.add_error("Category is missing!")
        if wrapper.get_licence_plate() == None:
            wrapper.add_error("Licence plate is missing!")
        if wrapper.get_type() == None:
            wrapper.add_error("Type is missing!")
        if wrapper.get_rental_fee() == None:
            wrapper.add_error("Rental fee is missing!")
        if (
            wrapper.get_category() != None
            and wrapper.get_licence_plate() != None
            and wrapper.get_type() != None
            and wrapper.get_rental_fee() != None
        ):
            car = self.service.save_or_update_car(wrapper)
            return CarFactory.create_wrapper(car)

    def get_car_by_id(self, id: int) -> CarWrapper:
        wrapper = CarWrapper()
        try:
            car = self.service.get_car_by_id(id)
            wrapper = CarFactory.create_wrapper(car)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_cars(self) -> list[CarWrapper]:
        cars = self.service.get_all_cars()
        wrappers: list[CarWrapper] = list()
        for car in cars:
            wrappers.append(CarFactory.create_wrapper(car))

        return wrappers

    def remove_car_by_id(self, id: int) -> CarWrapper:
        wrapper = CarWrapper()
        try:
            self.service.remove_car_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))
