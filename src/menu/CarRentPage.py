from menu.PageBase import PageBase
from datetime import datetime
from dto.RentView import RentView
from dto.CarView import CarView
from menu.Item import Item
from menu.MenuService import MenuService


class CarRentPage(PageBase):

    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, "Rent a car")
        self.service = service

    def _get_car_rental_id(self) -> int:
        question = "Which car rental would you like to browse from?"
        source = self.service.get_all_rentals()
        return self.get_item().get_selection_result(Item(question, source))

    def _get_car_id(self, rental_id: int) -> int:
        question = "Which car would u like to choose from?"
        source = self.service.get_car_rental_by_id(rental_id)
        return self.get_item().get_selection_result(Item(question, source.get_cars()))

    def _get_car_by_id(self, id: int) -> CarView:
        return self.service.get_car_by_id(id)

    def _get_rental_date(self, car: CarView) -> datetime:
        question = "When would u like to rent the chosen car?:"
        while True:
            chosen_date = self.get_item().get_date_result(question)
            if not self.service.is_car_reserved(RentView(car, chosen_date)):
                return chosen_date
            else:
                print("Car is already reserved for the given date!")

    def _create_rent(self, car: CarView, rental_date: datetime) -> RentView:
        possible_rent = RentView(car_view=car, rental_time=rental_date)
        return self.service.save_or_update_rent(possible_rent)

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def run(self):
        try:
            rental_id = self._get_car_rental_id()
            car_id = self._get_car_id(rental_id)
            car = self._get_car_by_id(car_id)
            rental_date = self._get_rental_date(car)
            saved_rent = self._create_rent(car, rental_date)
        except Exception as e:
            print(str(e))

    def print(self):
        return super().print()
