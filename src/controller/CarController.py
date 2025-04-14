from service.CarService import CarService
from data.CarWrapper import CarWrapper
from utils.CarFactory import CarFactory


class CarController:
    def __init__(self):
        self.service = CarService()

    def _add_error_to_wrapper(self, wrapper: CarWrapper, error: str) -> None:
        if error != "":
            wrapper.add_error(error)

    def create_or_update_car(self, wrapper: CarWrapper) -> CarWrapper:
        car = self.service.create_or_update_car(wrapper)
        return CarFactory.create_wrapper(car)

    def get_car_by_id(self, id: int) -> CarWrapper:
        error: str = ""
        try:
            car = self.service.get_car_by_id(id)
        except Exception as e:
            error = str(e)
        finally:
            wrapper: CarWrapper = CarFactory.create_wrapper(car)
            self._add_error_to_wrapper(wrapper, error)
            return wrapper

    def get_all_cars(self) -> list[CarWrapper]:
        cars = self.service.get_all_cars()
        wrappers: list[CarWrapper] = list()
        for car in cars:
            wrappers.append(CarFactory.create_wrapper(car))

        return wrappers

    def remove_car_by_id(self, id: int) -> None:
        error: str = ""
        try:
            self.service.remove_car_by_id(id)
        except Exception as e:
            error = str(e)
        finally:
            wrapper: CarWrapper = CarWrapper()
            self._add_error_to_wrapper(wrapper, error)
