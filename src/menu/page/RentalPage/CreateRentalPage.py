from menu.page.PageBase import PageBase
from menu.page.CarPage.CreateCarPage import CreateCarPage
from dto.CarView import CarView
from dto.ViewBase import ViewBase
from menu.utils.MenuOption import MenuOption
from menu.utils.Item import Item
from menu.service.MenuService import MenuService
from dto.CarRentalView import CarRentalView


class CreateRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, "Rental Creation")
        self.service = service

    def _get_rental_name(self) -> None:
        question = "What is the name of the rental? "
        return self.get_item().get_text_result(Item(question))

    def _add_another_car(self) -> bool:
        question = "Would u like to add another car?"
        return self.get_item().get_yes_no_result(question)

    def _select_car(self) -> int:
        question = "Which car would u like to add?: "
        source = self.service.get_all_cars()
        return self.get_item().get_selection_result(Item(question, source))

    def _get_cars(self) -> list[CarView]:
        cars_to_add: list[CarView] = list()
        question = "Would u like to create a new car, or add an existing one?"
        car_creation_page = CreateCarPage(1, self.service)
        source: list[ViewBase] = (
            car_creation_page,
            MenuOption(2, "Add existing car"),
        )
        selected_option = self.get_item().get_selection_result(Item(question, source))
        if selected_option == 1:
            while True:
                created_car = car_creation_page.run()
                cars_to_add.append(created_car)
                if not self._add_another_car():
                    break

        else:
            while True:
                car_id = self._select_car()
                selected_car = self.service.get_car_by_id(car_id)
                cars_to_add.append(selected_car)
                if not self._add_another_car():
                    break

        return cars_to_add

    def run(self) -> None:
        super().run()
        try:
            rental_name = self._get_rental_name()
            cars = self._get_cars()
            self.service.save_or_update_rental(CarRentalView(rental_name, cars))
        except Exception as e:
            print(str(e))
