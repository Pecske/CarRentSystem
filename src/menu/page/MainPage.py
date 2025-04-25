from menu.page.RentPage.CreateRentPage import CreateRentPage
from menu.page.PageBase import PageBase
from menu.page.ExitPage import ExitPage
from menu.page.RentPage.RentListPage import RentListPage
from menu.page.RentPage.DeleteRentPage import DeleteRentPage
from menu.page.RentalPage.ManageRentalPage import ManageRentalPage
from menu.utils.Item import Item
from utils.DependencyController import DependencyController
from menu.service.MenuService import MenuService
from utils.FileService import FileService


class MainPage(PageBase):
    CAR_RENTAL_PATH = "resources/carrental.json"
    RENTAL_PATH = "resources/rents.json"

    def __init__(self, container: DependencyController, page_id: int, menu_name: str):
        super().__init__(page_id, menu_name)
        self.container = container
        self.pages = (
            CreateRentPage(1, self.container.get_class(MenuService)),
            RentListPage(2, self.container.get_class(MenuService)),
            DeleteRentPage(3, self.container.get_class(MenuService)),
            ManageRentalPage(4, self.container.get_class(MenuService)),
            ExitPage(5),
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

    def run(self):
        super().run()
        while True:
            selected_page = self._select_page()
            for page in self.pages:
                if page.get_id() == selected_page:
                    page.run()
                    break
