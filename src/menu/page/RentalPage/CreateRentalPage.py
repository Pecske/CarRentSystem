from menu.page.PageBase import PageBase
from menu.page.CarPage.CreateCarPage import CreateCarPage
from dto.CarView import CarView
from dto.ViewBase import ViewBase
from menu.utils.MenuOption import MenuOption
from menu.utils.Item import Item
from menu.service.MenuService import MenuService
from dto.CarRentalView import CarRentalView
from utils.TextType import TextType


class CreateRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, TextType.Rental_Create_Menu)
        self.service = service

    def _get_rental_name(self) -> None:
        question = self.get_text_from_cache(TextType.Rental_Create_Name)
        return self.get_item().get_text_result(Item(question))

    def _add_another_car(self) -> bool:
        question = self.get_text_from_cache(TextType.Rental_Create_Another_Car)
        return self.get_item().get_yes_no_result(question)

    def _select_car(self) -> int:
        question = self.get_text_from_cache(TextType.Rental_Create_Select_car)
        source = self.service.get_all_cars()
        return self.get_item().get_selection_result(Item(question, source))

    def _select_cars(self) -> list[int]:
        results: list[int] = list()
        question = self.get_text_from_cache(TextType.Rental_Create_Select_car)
        source = self.service.get_all_cars()
        while True:
            car_list: list[CarView] = list()
            for car in source:
                if car.get_id() not in results:
                    car_list.append(car)
            if len(car_list) > 0:
                item = Item(question, car_list)
                chosen_id = self.get_item().get_selection_result(item)
                if chosen_id not in results:
                    results.append(chosen_id)
            else:
                break
            if not self._add_another_car():
                break
        return results

    def _get_cars(self) -> list[CarView]:
        cars_to_add: list[CarView] = list()
        question = self.get_text_from_cache(TextType.Rental_Create_New_Existing_Car)
        car_creation_page = CreateCarPage(1, self.service)
        source: list[ViewBase] = (
            car_creation_page,
            MenuOption(
                2, self.get_text_from_cache(TextType.Rental_Create_Add_Car_Menu)
            ),
        )
        selected_option = self.get_item().get_selection_result(Item(question, source))
        if selected_option == 1:
            while True:
                created_car = car_creation_page.run()
                cars_to_add.append(created_car)
                if not self._add_another_car():
                    break

        else:
            car_ids = self._select_cars()
            for id in car_ids:
                found_car = self.service.get_car_by_id(id)
                cars_to_add.append(found_car)

        return cars_to_add

    def run(self) -> None:
        super().run()
        try:
            rental_name = self._get_rental_name()
            cars = self._get_cars()
            self.service.save_or_update_rental(CarRentalView(rental_name, cars))
        except Exception as e:
            print(str(e))
