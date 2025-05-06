from service.CarService import CarService
from service.RentService import RentService
from utils.Wrapper import Wrapper
from dto.RentView import RentView
from data.Rent import Rent
from utils.RentFactory import RentFactory


class RentController:
    def __init__(self, car_service: CarService, rent_service: RentService) -> None:
        self.car_service = car_service
        self.rent_service = rent_service

    def _create_rent(self, dto: RentView) -> RentView:
        result: RentView | None = None
        car_id = dto.get_car_view().get_id()
        rental_time = dto.get_rental_time()
        found_car = self.car_service.get_car_by_id(car_id)
        if not self.rent_service.is_car_reserved(found_car, rental_time):
            new_rent = Rent(car=found_car, rental_time=rental_time, id=dto.get_id())
            saved_rent = self.rent_service.save_or_update_rent(new_rent)
            result = RentFactory.map_data_to_view(saved_rent)
        return result

    def save_or_update_rent(self, dto: RentView) -> Wrapper[RentView]:
        result = Wrapper[RentView]()
        if dto != None:
            possible_car = dto.get_car_view()
            if possible_car != None:
                try:
                    saved_rent = self._create_rent(dto)
                    if saved_rent != None:
                        result.set_wrapped_obj(saved_rent)
                    else:
                        result.add_error("Car is already reserved on the given date!")
                except Exception as e:
                    result.add_error(str(e))
            else:
                result.add_error("Missing car information!")
        else:
            result.add_error("Missing rent information!")
        return result

    def get_rent_by_id(self, id: int) -> Wrapper[RentView]:
        result = Wrapper[RentView]()
        try:
            found_rent = self.rent_service.get_rent_by_id(id)
            result.set_wrapped_obj(RentFactory.map_data_to_view(found_rent))
        except Exception as e:
            result.add_error(str(e))

        return result

    def get_all_rents(self) -> Wrapper[list[RentView]]:
        result = Wrapper[list[RentView]]()
        rents = self.rent_service.get_all_rents()
        views: list[RentView] = list()
        for rent in rents:
            view = RentFactory.map_data_to_view(rent)
            views.append(view)

        result.set_wrapped_obj(views)
        return result

    def remove_rent_by_id(self, id: int) -> Wrapper[RentView]:
        result = Wrapper[RentView]()
        try:
            self.rent_service.delete_rent_by_id(id)
        except Exception as e:
            result.add_error(str(e))

        return result

    def is_car_reserved(self, dto: RentView) -> Wrapper[bool]:
        result: Wrapper[bool] = Wrapper()
        car = dto.get_car_view()
        if car != None:
            try:
                found_car = self.car_service.get_car_by_id(car.get_id())
                is_reserved = self.rent_service.is_car_reserved(
                    found_car, dto.get_rental_time()
                )
                result.set_wrapped_obj(is_reserved)
            except Exception as e:
                result.add_error(str(e))
        else:
            result.add_error("Missing car info")
        return result
