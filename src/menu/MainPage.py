from menu.CarRentPage import CarRentPage
from menu.PageBase import PageBase
from menu.ExitPage import ExitPage
from menu.Item import Item
import sys
import os


class MainPage(PageBase):
    def __init__(self, page_id, menu_name):
        super().__init__(page_id, menu_name)
        self.pages = (CarRentPage(1), ExitPage(2))

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
            self._clear_console()
            selected_page = self._select_page()
            for page in self.pages:
                if page.get_id() == selected_page:
                    page.run()
                    break
