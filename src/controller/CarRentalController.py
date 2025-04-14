from service.CarRentalService import CarRentalService
from service.CarService import CarService
from data.CarRentalWrapper import CarRentalWrapper
from data.CarWrapper import CarWrapper


class CarRentalController:
    def __init__(self):
        self.rental_service = CarRentalService()
        self.car_service = CarService()

    def save_or_update_rental(self, wrapper: CarRentalWrapper) -> CarRentalWrapper:
        if wrapper.get_rental() != None:
            rental = self.rental_service.save_or_update_rental(wrapper.get_rental())
            wrapper.set_rental(rental)
        else:
            wrapper.add_error("No data was given")

        return wrapper

    def get_rental_by_id(self, id: None) -> CarRentalWrapper:
        wrapper = CarRentalWrapper()
        try:
            found_rental = self.rental_service.get_rental_by_id(id)
            wrapper.set_rental(found_rental)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_rentals(self) -> list[CarRentalWrapper]:
        rentals = self.rental_service.get_all_rentals()
        wrappers: list[CarRentalWrapper] = list()
        for rental in rentals:
            wrapper = CarRentalWrapper(rental)
            wrappers.append(wrapper)

        return wrappers

    def remove_rental_by_id(self, id: int) -> None:
        wrapper = CarRentalWrapper()
        try:
            self.rental_service.delete_rental_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def add_car_to_rental(self, rental_id: int, car: CarWrapper) -> CarRentalWrapper:
        car_id = car.get_id()
        wrapper = CarRentalWrapper()
        if car_id != None:
            try:
                found_car = self.car_service.get_car_by_id(car_id)
                rental = self.rental_service.add_car_to_rental(rental_id, found_car)
                wrapper.set_rental(rental)
            except Exception as e:
                wrapper.add_error(str(e))
        else:
            wrapper.add_error("Car id must be given!")

        return wrapper

    def remove_car_from_rental(
        self, rental_id: int, car: CarWrapper
    ) -> CarRentalWrapper:
        car_id = car.get_id()
        wrapper = CarRentalWrapper()
        if car_id != None:
            try:
                found_car = self.car_service.get_car_by_id(car_id)
                rental = self.rental_service.remove_car_from_rental(
                    rental_id, found_car
                )
                wrapper.set_rental(rental)
            except Exception as e:
                wrapper.add_error(str(e))
        else:
            wrapper.add_error("Car id must be given!")
