from repository.CarRepository import CarRepository
from data.Car import Car
from data.CarWrapper import CarWrapper
from utils.CarFactory import CarFactory


class CarService:

    def __init__(self):
        self.repo = CarRepository()

    def create_or_update_car(self, wrapper: CarWrapper) -> Car:
        car = CarFactory.create_car(wrapper)

        return self.repo.save_or_update(car)

    def get_car_by_id(self, id: int) -> Car:
        found_car = self.repo.get_data_by_id(id)
        if found_car == None:
            raise Exception("There is no car by the given id!")
        else:
            return found_car

    def get_all_cars(self) -> list[Car]:
        return self.repo.get_all_datas()

    def remove_car_by_id(self, id: int) -> None:
        try:
            self.repo.delete_by_id(id)
        except KeyError:
            raise KeyError("There is no car by the given id!")
