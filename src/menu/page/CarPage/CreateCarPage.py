from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from utils.CarCategory import CarCategory
from menu.utils.MenuOption import MenuOption
from menu.utils.Item import Item
from dto.CarView import CarView
from utils.TextType import TextType


class CreateCarPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, TextType.Car_Create_Menu)
        self.service = service

    def _get_car_category(self) -> CarCategory:
        question = self.get_text_from_cache(TextType.Car_Create_Category)
        source: list[MenuOption] = list()
        for category in CarCategory:
            option = MenuOption(category.value, category.name)
            source.append(option)

        selected_category = self.get_item().get_selection_result(Item(question, source))
        return CarCategory(selected_category)

    def _get_licence_plate(self) -> str:
        question = self.get_text_from_cache(TextType.Car_Create_Licence_Plate)
        return self.get_item().get_text_result(Item(question))

    def _get_type(self) -> str:
        question = self.get_text_from_cache(TextType.Car_Create_Type)
        return self.get_item().get_text_result(Item(question))

    def _get_rental_currency(self) -> str:
        question = self.get_text_from_cache(TextType.Car_Create_Currency)
        return self.get_item().get_text_result(Item(question))

    def _get_rental_fee(self) -> int:
        question = self.get_text_from_cache(TextType.Car_Create_Amount)
        return self.get_item().get_int_text_result(Item(question))

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
