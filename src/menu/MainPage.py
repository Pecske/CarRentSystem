from menu.CarRentPage import CarRentPage
from menu.PageBase import PageBase
from menu.ExitPage import ExitPage
from menu.RentListPage import RentListPage
from menu.RemoveRentPage import RemoveRentPage
from menu.Item import Item
from utils.DependencyController import DependencyController
from menu.MenuService import MenuService
from utils.FileService import FileService
import sys
import os


class MainPage(PageBase):
    CAR_RENTAL_PATH = "resources/carrental.json"
    RENTAL_PATH = "resources/rents.json"

    def __init__(self, container: DependencyController, page_id, menu_name):
        super().__init__(page_id, menu_name)
        self.container = container
        self.pages = (
            CarRentPage(1, self.container.get_class(MenuService)),
            RentListPage(2,self.container.get_class(MenuService)),
            RemoveRentPage(3, self.container.get_class(MenuService)),
            ExitPage(4),
        )
        self._init_data()

    def _init_data(self) -> None:
        file_service = self.container.get_class(FileService)
        try:
            file_service.save_car_rental(self.CAR_RENTAL_PATH)
            file_service.save_rents(self.RENTAL_PATH)
        except Exception as e:
            print(str(e))

    def _select_page(self) -> int:
        menu_item = Item("", self.pages)
        return self.get_item().get_selection_result(menu_item)

    def _clear_console(self) -> None:
        if sys.platform == "win32":
            os.system("cls")
        else:
            print("\033[H\033[3J", end="")

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def run(self):
        while True:
            selected_page = self._select_page()
            for page in self.pages:
                if page.get_id() == selected_page:
                    self._clear_console()
                    page.run()
                    break
