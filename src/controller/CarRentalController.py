from utils.Wrapper import Wrapper
from dto.CarView import CarView
from dto.CarRentalView import CarRentalView
from utils.CarRentalFactory import CarRentalFactory
from service.CarService import CarService
from service.CarRentalService import CarRentalService
from data.Car import Car
from data.CarRental import CarRental


class CarRentalController:
    def __init__(self):
        self.car_service = CarService()
        self.car_rental_service = CarRentalService()

    def _get_cars_to_save(self, cars: list[CarView]) -> list[Car]:
        cars_to_save: list[Car] = list()
        if len(cars) > 0:
            for car in cars:
                car_id = car.get_id()
                if car_id != None:
                    try:
                        found_car = self.car_service.get_car_by_id(car_id)
                        cars_to_save.append(found_car)
                    except:
                        created_car = self.car_service.save_or_update_car(car)
                        cars_to_save.append(created_car)
        return cars_to_save

    def save_or_update_rental(
        self, wrapper: Wrapper[CarRentalView]
    ) -> Wrapper[CarRentalView]:
        wrapped_obj = wrapper.get_wrapped_obj()
        if wrapped_obj() != None:
            cars_to_save = self._get_cars_to_save(wrapped_obj.get_cars())
            rental = CarRental(wrapped_obj.get_name(), cars_to_save)
            saved_rental = self.car_rental_service.save_or_update_rental(rental)
            wrapper.set_wrapped_obj(CarRentalFactory.from_data_to_view(saved_rental))
        else:
            wrapper.add_error("Car Rental data must be given!")

        return wrapper

    def get_rental_by_id(self, id: int) -> Wrapper[CarRentalView]:
        wrapper = Wrapper[CarRentalView]()
        try:
            found_rental = self.car_rental_service.get_rental_by_id(id)
            wrapper.set_wrapped_obj(CarRentalFactory.from_data_to_view(found_rental))
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def get_all_rentals(self) -> list[Wrapper[CarRentalView]]:
        rentals = self.car_rental_service.get_all_rentals()
        wrappers: list[Wrapper[CarRentalView]] = list()
        for rental in rentals:
            wrapper = Wrapper[CarRentalView](CarRentalFactory.from_data_to_view(rental))
            wrappers.append(wrapper)

        return wrappers

    def remove_rental_by_id(self, id: int) -> Wrapper[CarRentalView]:
        wrapper = Wrapper[CarRentalView]()
        try:
            self.car_rental_service.delete_rental_by_id(id)
        except Exception as e:
            wrapper.add_error(str(e))

        return wrapper

    def add_car_to_rental(
        self, rental_id: int, wrapper: Wrapper[CarView]
    ) -> Wrapper[CarRentalView]:
        wrapped_obj = wrapper.get_wrapped_obj()
        result = Wrapper[CarRentalView]()
        if wrapped_obj == None:
            result.add_error("Car info must be given!")
        else:
            car_id = wrapped_obj.get_id()
            if car_id != None:
                try:
                    found_car = self.car_service.get_car_by_id(car_id)
                    rental = self.car_rental_service.add_car_to_rental(
                        rental_id, found_car
                    )
                    result.set_wrapped_obj(CarRentalFactory.from_data_to_view(rental))
                except Exception as e:
                    result.add_error(str(e))
            else:
                result.add_error("Car id must be given!")

        return result

    def remove_car_from_rental(
        self, rental_id: int, wrapper: Wrapper[CarView]
    ) -> Wrapper[CarRentalView]:
        wrapped_obj = wrapper.get_wrapped_obj()
        result = Wrapper[CarRentalView]()
        if wrapped_obj == None:
            result.add_error("Car info must be given!")
        else:
            car_id = wrapped_obj.get_id()
            if car_id != None:
                try:
                    found_car = self.car_service.get_car_by_id(car_id)
                    rental = self.car_rental_service.remove_car_from_rental(
                        rental_id, found_car
                    )
                    result.set_wrapped_obj(CarRentalFactory.from_data_to_view(rental))
                except Exception as e:
                    result.add_error(str(e))
            else:
                result.add_error("Car id must be given!")
        return result
