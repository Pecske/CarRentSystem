from repository.RentRepository import RentRepository
from data.Rent import Rent
from data.Car import Car
from datetime import datetime


class RentService:
    def __init__(self):
        self.repo = RentRepository()

    def save_or_update_rent(self, rent: Rent) -> Rent:
        date = rent.get_rental_time()
        if date <= datetime.now():
            raise Exception("Invalid date!")
        else:
            return self.repo.save_or_update(rent)

    def get_rent_by_id(self, id: int) -> Rent:
        found_rent = self.repo.get_data_by_id(id)
        if found_rent == None:
            raise Exception("There is no rent by the given id!")
        else:
            return found_rent

    def get_all_rents(self) -> list[Rent]:
        return self.repo.get_all_datas()

    def delete_rent_by_id(self, id: int) -> None:
        try:
            self.repo.delete_by_id(id)
        except KeyError:
            raise KeyError("There is no rent by the given id!")
    
    def is_car_reserved(self,car : Car, time : datetime) -> bool:
        rents = self.get_all_rents()
        for rent in rents:
            if rent.get_car() == car and rent.get_rental_time() == time:
                return True
        
        return False