from menu.service.MenuService import MenuService
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
from utils.TextCache import TextCache
from typing import TypeVar

T = TypeVar("T")


class DependencyController(object):

    def __init__(self) -> None:
        self.dependencies = dict()
        self.class_dict = {
            MenuService: self._get_menu_service,
            CarController: self._get_car_controller,
            RentController: self._get_rent_controller,
            CarRentalController: self._get_car_rental_controller,
            CarService: self._get_car_service,
            RentService: self._get_rent_service,
            CarRentalService: self._get_car_rental_serivce,
            FileService: self._get_file_service,
            CarRepository: self._get_car_repo,
            RentRepository: self._get_rent_repo,
            CarRentalRepository: self._get_car_rental_repo,
            FileHandler: self._get_file_handler,
            TextCache: self._get_text_cache,
        }

    def get_class(self, dependency: type[T]) -> T:
        if dependency in self.class_dict:
            builder = self.class_dict.get(dependency)
            return builder()

    def _get_menu_service(self) -> MenuService:
        service_type = MenuService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = MenuService(
                self._get_car_rental_controller(),
                self._get_car_controller(),
                self._get_rent_controller(),
            )
        return self.dependencies.get(service_type)

    def _get_car_controller(self) -> CarController:
        controller_type = CarController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = CarController(self._get_car_service())
        return self.dependencies.get(controller_type)

    def _get_rent_controller(self) -> RentController:
        controller_type = RentController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = RentController(
                self._get_car_service(), self._get_rent_service()
            )
        return self.dependencies.get(controller_type)

    def _get_car_rental_controller(self) -> CarRentalController:
        controller_type = CarRentalController
        if controller_type not in self.dependencies:
            self.dependencies[controller_type] = CarRentalController(
                self._get_car_service(), self._get_car_rental_serivce()
            )
        return self.dependencies.get(controller_type)

    def _get_car_service(self) -> CarService:
        service_type = CarService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = CarService(self._get_car_repo())
        return self.dependencies.get(service_type)

    def _get_rent_service(self) -> RentService:
        service_type = RentService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = RentService(self._get_rent_repo())
        return self.dependencies.get(service_type)

    def _get_car_rental_serivce(self) -> CarRentalService:
        service_type = CarRentalService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = CarRentalService(
                self._get_car_rental_repo()
            )
        return self.dependencies.get(service_type)

    def _get_file_service(self) -> FileService:
        service_type = FileService
        if service_type not in self.dependencies:
            self.dependencies[service_type] = FileService(
                self._get_car_rental_controller(),
                self._get_car_controller(),
                self._get_rent_controller(),
                self._get_file_handler(),
                self._get_text_cache(),
            )
        return self.dependencies.get(service_type)

    def _get_text_cache(self) -> TextCache:
        cache_type = TextCache
        if cache_type not in self.dependencies:
            self.dependencies[cache_type] = TextCache.get_instance()
        return self.dependencies.get(cache_type)

    def _get_car_repo(self) -> CarRepository:
        repo_type = CarRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = CarRepository()
        return self.dependencies.get(repo_type)

    def _get_rent_repo(self) -> RentRepository:
        repo_type = RentRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = RentRepository()
        return self.dependencies.get(repo_type)

    def _get_car_rental_repo(self) -> CarRentalRepository:
        repo_type = CarRentalRepository
        if repo_type not in self.dependencies:
            self.dependencies[repo_type] = CarRentalRepository()
        return self.dependencies.get(repo_type)

    def _get_file_handler(self) -> FileHandler:
        handler_type = FileHandler
        if handler_type not in self.dependencies:
            self.dependencies[handler_type] = FileHandler()
        return self.dependencies.get(handler_type)
