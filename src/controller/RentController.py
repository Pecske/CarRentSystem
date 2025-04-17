from service.CarService import CarService
from service.RentService import RentService
from utils.Wrapper import Wrapper
from data.Rent import Rent


class RentController:
    def __init__(self):
        self.car_service = CarService()
        self.rent_service = RentService()

    def save_or_update_rent(self, wrapper: Wrapper[Rent]) -> Wrapper[Rent]:
        wrapped_obj = wrapper.get_wrapped_obj()
        result = Wrapper[Rent]()
        if wrapped_obj == None:
            result.add_error("Missing rent information!")
        else:
            possible_car = wrapped_obj.get_car()
            if possible_car == None:
                result.add_error("Missing car information!")
            else:
                car_id = possible_car.get_id()
                try:
                    found_car = self.car_service.get_car_by_id(car_id)
                    if self.rent_service.is_car_reserved(
                        found_car, wrapped_obj.get_rental_time()
                    ):
                        result.add_error("Car is already reserved on the given date!")
                    else:
                        wrapped_obj.set_car(found_car)
                        saved_rent = self.rent_service.save_or_update_rent(wrapped_obj)
                        result.set_wrapped_obj(saved_rent)
                except Exception as e:
                    result.add_error(str(e))

        return result

    def get_rent_by_id(self, id: int) -> Wrapper[Rent]:
        result = Wrapper[Rent]()
        try:
            found_rent = self.rent_service.get_rent_by_id(id)
            result.set_wrapped_obj(found_rent)
        except Exception as e:
            result.add_error(str(e))

        return result

    def get_all_rents(self) -> list[Wrapper[Rent]]:
        results: list[Wrapper[Rent]] = list()
        rents = self.rent_service.get_all_rents()
        for rent in rents:
            wrapper = Wrapper[Rent](rent)
            results.append(wrapper)

        return results

    def remove_rent_by_id(self, id: int) -> Wrapper[Rent]:
        result = Wrapper[Rent]()
        try:
            self.rent_service.delete_rent_by_id(id)
        except Exception as e:
            result.add_error(str(e))

        return result
