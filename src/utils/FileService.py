from controller.CarRentalController import CarRentalController
from controller.CarController import CarController
from controller.RentController import RentController
from utils.FileHandler import FileHandler
from utils.TextCache import TextCache
from utils.TextType import TextType


class FileService:
    def __init__(
        self,
        car_rental_controller: CarRentalController,
        car_controller: CarController,
        rent_controller: RentController,
        file_handler: FileHandler,
        text_cache: TextCache,
    ) -> None:
        self.car_rental_controller = car_rental_controller
        self.car_controller = car_controller
        self.rent_controller = rent_controller
        self.handler = file_handler
        self.text_cache = text_cache

    def _join_errors(self, errors: list[str]) -> str:
        errors_joined = ""
        for error in errors:
            errors_joined += f"{error}\n"
        return errors_joined

    def save_car_rental(self, path: str) -> None:
        imported_car_rentals = self.handler.read_car_rentals(path)
        errors: str = ""
        for car_rental in imported_car_rentals:
            saved = self.car_rental_controller.save_or_update_rental(car_rental)
            if len(saved.get_errors()) > 0:
                errors = self._join_errors(saved.get_errors())
        if errors != "":
            raise Exception(errors)

    def save_rents(self, path: str) -> None:
        imported_rents = self.handler.read_rents(path)
        errors: str = ""
        for rent in imported_rents:
            saved = self.rent_controller.save_or_update_rent(rent)
            if len(saved.get_errors()) > 0:
                errors = self._join_errors(saved.get_errors())
        if errors != "":
            raise Exception(errors)

    def save_texts(self, path: str) -> None:
        imported_texts = self.handler.read_text(path)
        for text in imported_texts:
            for type in TextType:
                if type.name.lower() == text.get_name():
                    self.text_cache.add_to_texts(type, text)
