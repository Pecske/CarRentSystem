from menu.page.PageBase import PageBase
from menu.page.CarPage.CreateCarPage import CreateCarPage
from menu.service.MenuService import MenuService
from dto.CarRentalView import CarRentalView
from menu.utils.Item import Item
from menu.utils.MenuOption import MenuOption
from dto.ViewBase import ViewBase
from dto.CarView import CarView
from utils.TextType import TextType


class UpdateRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, TextType.Rental_Update_Menu)
        self.service = service

    def _get_rental_id(self) -> list[CarRentalView]:
        question = self.get_text_from_cache(TextType.Rental_Update_Id)
        source = self.service.get_all_rentals()
        return self.get_item().get_selection_result(Item(question, source))

    def _add_another_car(self) -> bool:
        question = self.get_text_from_cache(TextType.Rental_Update_Add_Another)
        return self.get_item().get_yes_no_result(question)

    def _remove_another_car(self) -> bool:
        question = self.get_text_from_cache(TextType.Rental_Update_Remove_Another)
        return self.get_item().get_yes_no_result(question)

    def _select_car(self) -> int:
        question = self.get_text_from_cache(TextType.Rental_Update_Select_Car)
        source = self.service.get_all_cars()
        return self.get_item().get_selection_result(Item(question, source))

    def _get_cars_to_add(self) -> list[CarView]:
        cars: list[CarView] = list()
        question = self.get_text_from_cache(TextType.Rental_Update_New_Existing_Car)
        car_creation_page = CreateCarPage(1, self.service)
        source: list[ViewBase] = (
            car_creation_page,
            MenuOption(
                2, self.get_text_from_cache(TextType.Rental_Update_Add_Car_Menu)
            ),
        )
        selected_option = self.get_item().get_selection_result(Item(question, source))
        if selected_option == 1:
            while True:
                car = car_creation_page.run()
                cars.append(car)
                if not self._add_another_car():
                    break
        else:
            while True:
                car_id = self._select_car()
                selected_car = self.service.get_car_by_id(car_id)
                cars.append(selected_car)
                if not self._add_another_car():
                    break

        return cars

    def _get_cars_to_remove(self) -> CarRentalView:
        cars_to_remove: list[CarView] = list()
        while True:
            selected_car = self._select_car()
            cars_to_remove.append(selected_car)
            if not self._remove_another_car():
                break
        return cars_to_remove

    def _add_or_remove_car(self) -> CarRentalView:
        rental_id = self._get_rental_id()
        rental = self.service.get_car_rental_by_id(rental_id)
        question = self.get_text_from_cache(TextType.Rental_Update_Add_Remove_Car)
        source: list[ViewBase] = (
            MenuOption(1, self.get_text_from_cache(TextType.Rental_Update_Add_Menu)),
            MenuOption(2, self.get_text_from_cache(TextType.Rental_Update_Remove_Menu)),
        )
        selected_option = self.get_item().get_selection_result(Item(question, source))
        if selected_option == 1:
            cars = self._get_cars_to_add()
            for car in cars:
                rental.add_car(car)
        else:
            cars = self._get_cars_to_remove()
            for car in cars:
                rental.remove_car(car)
        return self.service.save_or_update_rental(rental)

    def run(self) -> CarRentalView:
        super().run()
        try:
            return self._add_or_remove_car()
        except Exception as e:
            print(str(e))
