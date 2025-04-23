from controller.CarRentalController import CarRentalController
from controller.CarController import CarController
from controller.RentController import RentController
from utils.Wrapper import Wrapper
from typing import TypeVar
from dto.CarRentalView import CarRentalView
from dto.CarView import CarView
from dto.RentView import RentView


class MenuService:

    T = TypeVar("T")

    def __init__(
        self,
        car_rental_controller: CarRentalController,
        car_controller: CarController,
        rent_controller: RentController,
    ) -> None:
        self.car_rental_controller = car_rental_controller
        self.car_controller = car_controller
        self.rent_controller = rent_controller

    def _join_errors(self, errors: list[str]) -> str:
        errors_joined = ""
        for error in errors:
            errors_joined += f"{error}\n"
        return errors_joined

    def _unwrap_object(self, wrapper: Wrapper[T]) -> T:
        errors = wrapper.get_errors()
        if len(errors) == 0:
            return wrapper.get_wrapped_obj()
        else:
            raise Exception(self._join_errors(errors))

    def get_all_rentals(self) -> list[CarRentalView]:
        result = self.car_rental_controller.get_all_rentals()
        return self._unwrap_object(result)

    def get_car_rental_by_id(self, id: int) -> CarRentalView:
        result = self.car_rental_controller.get_rental_by_id(id)
        return self._unwrap_object(result)

    def get_car_by_id(self, id: int) -> CarView:
        result = self.car_controller.get_car_by_id(id)
        return self._unwrap_object(result)

    def is_car_reserved(self, rent: RentView) -> bool:
        result = self.rent_controller.is_car_reserved(rent)
        return self._unwrap_object(result)

    def save_or_update_rent(self, rent: RentView) -> RentView:
        result = self.rent_controller.save_or_update_rent(rent)
        return self._unwrap_object(result)
