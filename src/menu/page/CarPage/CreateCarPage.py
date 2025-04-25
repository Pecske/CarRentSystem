from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from utils.CarCategory import CarCategory
from menu.utils.ValidationResult import ValidationResult
from menu.utils.MenuOption import MenuOption
from menu.utils.Item import Item
from dto.CarView import CarView


class CreateCarPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, "Car Creation")
        self.service = service

    def _get_car_category(self) -> CarCategory:
        question = "Choose a category: "
        source: list[MenuOption] = list()
        for category in CarCategory:
            option = MenuOption(category.value, category.name)
            source.append(option)

        selected_category = self.get_item().get_selection_result(Item(question, source))
        return CarCategory(selected_category)

    def _get_licence_plate(self) -> str:
        question = "What is the licence plate?: "
        return self.get_item().get_text_result(Item(question))

    def _get_type(self) -> str:
        question = "What is the type?: "
        return self.get_item().get_text_result(Item(question))

    def _get_rental_currency(self) -> str:
        question = "Which currency is the rental fee in? "
        return self.get_item().get_text_result(Item(question))

    def _get_rental_fee(self) -> int:
        question = "How much is the rental fee?: "
        return self.get_item().get_int_text_result(Item(question=question))

    def run(self) -> CarView:
        super().run()
        try:
            car_category = self._get_car_category()
            licence_plate = self._get_licence_plate()
            car_type = self._get_type()
            rental_currency = self._get_rental_currency()
            rental_fee = self._get_rental_fee()
            car = CarView(
                car_category, licence_plate, car_type, rental_fee, rental_currency
            )
            return self.service.save_or_update_car(car)
        except Exception as e:
            print(str(e))
