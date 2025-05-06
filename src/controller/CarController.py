from service.CarService import CarService
from utils.Wrapper import Wrapper
from utils.CarFactory import CarFactory
from dto.CarView import CarView


class CarController:
    def __init__(self, service: CarService) -> None:
        self.service = service

    def create_or_update_car(self, dto: CarView) -> Wrapper[CarView]:
        result = Wrapper[CarView]()
        if (
            dto.get_category() is not None
            and dto.get_licence_plate() is not None
            and dto.get_type() is not None
            and dto.get_rental_fee() is not None
        ):
            possible_car = CarFactory.map_view_to_data(dto)
            saved_car = self.service.save_or_update_car(possible_car)
            car_view = CarFactory.map_data_to_view(saved_car)
            result.set_wrapped_obj(car_view)
        if dto.get_category() is None:
            result.add_error("Category is missing!")
        if dto.get_licence_plate() is None:
            result.add_error("Licence plate is missing!")
        if dto.get_type() is None:
            result.add_error("Type is missing!")
        if dto.get_rental_fee() is None:
            result.add_error("Rental fee is missing!")
        return result

    def get_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            car = self.service.get_car_by_id(id)
            car_view = CarFactory.map_data_to_view(car)
            wrapper.set_wrapped_obj(car_view)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_cars(self) -> Wrapper[list[CarView]]:
        cars = self.service.get_all_cars()
        result = Wrapper[list[CarView]]()
        views: list[CarView] = list()
        for car in cars:
            view = CarFactory.map_data_to_view(car)
            views.append(view)
        result.set_wrapped_obj(views)

        return result

    def remove_car_by_id(self, id: int) -> Wrapper[CarView]:
        wrapper = Wrapper[CarView]()
        try:
            self.service.remove_car_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))
        return wrapper
