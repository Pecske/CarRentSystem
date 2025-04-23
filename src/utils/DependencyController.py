from typing import Any
from menu.MenuService import MenuService
from controller.CarRentalController import CarRentalController
from controller.CarController import CarController
from controller.RentController import RentController
from service.CarRentalService import CarRentalService
from service.CarService import CarService
from service.RentService import RentService
from repository.CarRentalRepository import CarRentalRepository
from repository.CarRepository import CarRepository
from repository.RentRepository import RentRepository
from utils.FileService import FileService
from utils.FileHandler import FileHandler


class DependencyController:
    def __init__(self):
        self.dependencies = dict()

    def get_menu_service(self) -> MenuService:
        service_type = MenuService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = MenuService(
                self.get_car_rental_controller(),
                self.get_car_controller(),
                self.get_rent_controller(),
            )
        return self.dependencies.get(service_type)

    def get_car_controller(self) -> CarController:
        controller_type = CarController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = CarController(self.get_car_service())
        return self.dependencies.get(controller_type)

    def get_rent_controller(self) -> RentController:
        controller_type = RentController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = RentController(
                self.get_car_service(), self.get_rent_service()
            )
        return self.dependencies.get(controller_type)

    def get_car_rental_controller(self) -> CarRentalController:
        controller_type = CarRentalController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = CarRentalController(
                self.get_car_service(), self.get_car_rental_serivce()
            )
        return self.dependencies.get(controller_type)

    def get_car_service(self) -> CarService:
        service_type = CarService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = CarService(self.get_car_repo())
        return self.dependencies.get(service_type)

    def get_rent_service(self) -> RentService:
        service_type = RentService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = RentService(self.get_rent_repo())
        return self.dependencies.get(service_type)

    def get_car_rental_serivce(self) -> CarRentalService:
        service_type = CarRentalService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = CarRentalService(
                self.get_car_rental_repo()
            )
        return self.dependencies.get(service_type)

    def get_file_service(self) -> FileService:
        service_type = FileService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = FileService(
                self.get_car_rental_controller(),
                self.get_car_controller(),
                self.get_rent_controller(),
                self.get_file_handler(),
            )
        return self.dependencies.get(service_type)

    def get_car_repo(self) -> CarRepository:
        repo_type = CarRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = CarRepository()
        return self.dependencies.get(repo_type)

    def get_rent_repo(self) -> RentRepository:
        repo_type = RentRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = RentRepository()
        return self.dependencies.get(repo_type)

    def get_car_rental_repo(self) -> CarRentalRepository:
        repo_type = CarRentalRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = CarRentalRepository()
        return self.dependencies.get(repo_type)

    def get_file_handler(self) -> FileHandler:
        handler_type = FileHandler
        if handler_type not in self.dependencies:
            self.dependencies[handler_type] = FileHandler()
        return self.dependencies.get(handler_type)
