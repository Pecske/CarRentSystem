from data.RentWrapper import RentWrapper
from service.CarRentalService import CarRentalService
from service.CarService import CarService
from service.RentService import RentService


class RentController:
    def __init__(self):
        self.car_rental_service = CarRentalService()
        self.car_service = CarService()
        self.rent_service = RentService()

    def save_or_update_rent(self, wrapper: RentWrapper) -> RentWrapper:
        if wrapper.get_rent() == None:
            wrapper.add_error("Missing rent information!")
        else:
            rent = wrapper.get_rent()
            possible_car = rent.get_car()
            if possible_car == None:
                wrapper.add_error("Missing car information!")
            else:
                car_id = possible_car.get_id()
                try:
                    found_car = self.car_service.get_car_by_id(car_id)
                    if self.rent_service.is_car_reserved(
                        found_car, rent.get_rental_time()
                    ):
                        wrapper.add_error("Car is already reserved on the given date!")
                    else:
                        rent.set_car(found_car)
                        saved_rent = self.rent_service.save_or_update_rent(rent)
                        wrapper.set_rent(saved_rent)
                except Exception as e:
                    wrapper.add_error(str(e))

        return wrapper

    def get_rent_by_id(self, id: int) -> RentWrapper:
        wrapper = RentWrapper()
        try:
            found_rent = self.rent_service.get_rent_by_id(id)
            wrapper.set_rent(found_rent)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_rents(self) -> list[RentWrapper]:
        wrappers: list[RentWrapper] = list()
        rents = self.rent_service.get_all_rents()
        for rent in rents:
            wrappers.append(RentWrapper(rent))

        return wrappers

    def remove_rent_by_id(self, id: int) -> RentWrapper:
        wrapper = RentWrapper()
        try:
            self.rent_service.delete_rent_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper
