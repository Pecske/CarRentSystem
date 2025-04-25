from repository.CarRepository import CarRepository
from data.Car import Car


class CarService:

    def __init__(self, repo: CarRepository):
        self.repo = repo

    def save_or_update_car(self, car: Car) -> Car:
        found_car = self.repo.get_car_by_licence_plate(car.get_licence_plate())
        is_new = car.get_id() is None and found_car is None
        if car.get_id() is not None or is_new:
            return self.repo.save_or_update(car)
        else:
            raise Exception("Car with the given licence plate already exists!")

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
