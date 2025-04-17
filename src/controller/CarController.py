from service.CarService import CarService
from utils.Wrapper import Wrapper
from utils.CarFactory import CarFactory
from dto.CarView import CarView


class CarController:
    def __init__(self):
        self.service = CarService()

    def create_or_update_car(
        self, wrapper: Wrapper[CarView]
    ) -> Wrapper[CarView]:
        wrapped_obj = wrapper.get_wrapped_obj()
        if wrapped_obj.get_category() == None:
            wrapper.add_error("Category is missing!")
        if wrapped_obj.get_licence_plate() == None:
            wrapper.add_error("Licence plate is missing!")
        if wrapped_obj.get_type() == None:
            wrapper.add_error("Type is missing!")
        if wrapped_obj.get_rental_fee() == None:
            wrapper.add_error("Rental fee is missing!")
        if (
            wrapped_obj.get_category() != None
            and wrapped_obj.get_licence_plate() != None
            and wrapped_obj.get_type() != None
            and wrapped_obj.get_rental_fee() != None
        ):
            car = self.service.save_or_update_car(wrapped_obj)
            return CarFactory.create_transfer_obj(car)

    def get_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            car = self.service.get_car_by_id(id)
            transfer_obj = CarFactory.create_transfer_obj(car)
            wrapper.set_wrapped_obj(transfer_obj)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_cars(self) -> list[Wrapper[CarView]]:
        cars = self.service.get_all_cars()
        wrappers: list[Wrapper[CarView]] = list()
        for car in cars:
            transfer_obj = CarFactory.create_transfer_obj(car)
            wrappers.append(Wrapper[CarView](transfer_obj))

        return wrappers

    def remove_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            self.service.remove_car_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))
