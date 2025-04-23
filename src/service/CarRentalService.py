from repository.CarRentalRepository import CarRentalRepository
from data.CarRental import CarRental
from data.Car import Car


class CarRentalService:
    def __init__(self, repo: CarRentalRepository):
        self.repo = repo

    def save_or_update_rental(self, rental: CarRental) -> CarRental:
        return self.repo.save_or_update(rental)

    def get_rental_by_id(self, id: int) -> CarRental:
        found_rental = self.repo.get_data_by_id(id)
        if found_rental == None:
            raise Exception("There is no car rental by the given id!")
        else:
            return found_rental

    def get_all_rentals(self) -> list[CarRental]:
        return self.repo.get_all_datas()

    def delete_rental_by_id(self, id: int) -> None:
        try:
            self.repo.delete_by_id(id)
        except KeyError:
            raise KeyError("There is no car by the given id!")

    def add_car_to_rental(self, rental_id: int, car: Car) -> CarRental:
        rental = self.get_rental_by_id(rental_id)
        rental.add_car(car)
        return self.save_or_update_rental(rental)

    def remove_car_from_rental(self, rental_id: int, car: Car) -> CarRental:
        rental = self.get_rental_by_id(rental_id)
        try:
            rental.remove_car(car)
            return self.save_or_update_rental(rental)
        except ValueError:
            raise Exception("No car found in the given rental!")
