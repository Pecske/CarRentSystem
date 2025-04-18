from service.CarService import CarService
from utils.Wrapper import Wrapper
from utils.CarFactory import CarFactory
from dto.CarView import CarView


class CarController:
    def __init__(self):
        self.service = CarService()

    def create_or_update_car(self, dto: CarView) -> Wrapper[CarView]:
        result = Wrapper[CarView]()
        if (
            dto.get_category() != None
            and dto.get_licence_plate() != None
            and dto.get_type() != None
            and dto.get_rental_fee() != None
        ):
            possible_car = CarFactory.from_view_to_data(dto)
            saved_car = self.service.save_or_update_car(possible_car)
            car_view = CarFactory.from_data_to_view(saved_car)
            result.set_wrapped_obj(car_view)
        if dto.get_category() == None:
            result.add_error("Category is missing!")
        if dto.get_licence_plate() == None:
            result.add_error("Licence plate is missing!")
        if dto.get_type() == None:
            result.add_error("Type is missing!")
        if dto.get_rental_fee() == None:
            result.add_error("Rental fee is missing!")
        return result

    def get_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            car = self.service.get_car_by_id(id)
            car_view = CarFactory.from_data_to_view(car)
            wrapper.set_wrapped_obj(car_view)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_cars(self) -> Wrapper[list[CarView]]:
        cars = self.service.get_all_cars()
        result = Wrapper[list[CarView]]()
        views: list[CarView] = list()
        for car in cars:
            view = CarFactory.from_data_to_view(car)
            views.append(view)
        result.set_wrapped_obj(views)

        return result

    def remove_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            self.service.remove_car_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))
