from utils.DependencyController import DependencyController
from menu.NavigationMenu import NavigationMenu
from menu.service.MenuService import MenuService
from menu.page.RentPage.CreateRentPage import CreateRentPage
from menu.page.ExitPage import ExitPage
from menu.page.RentPage.RentListPage import RentListPage
from menu.page.RentPage.DeleteRentPage import DeleteRentPage
from menu.page.RentalPage.CreateRentalPage import CreateRentalPage
from menu.page.RentalPage.UpdateRentalPage import UpdateRentalPage
from menu.page.RentalPage.DeleteRentalPage import DeleteRentalPage
from menu.page.RentalPage.ListRentalPage import ListRentalPage
from menu.page.PreviousPage import PreviousPage


class MenuFactory:
    def __init__(self, container: DependencyController) -> None:
        self.container = container

    def create_main(self) -> NavigationMenu:
        main_menu = NavigationMenu(0, "Main Menu")
        rent_menu = self.create_rent(1, "Manage Rent")
        rental_menu = self.create_rental(2, "Manage Rental")

        rent_page_length = len(rent_menu.get_pages())
        rental_page_length = len(rental_menu.get_pages())

        rent_menu.add_page(PreviousPage(rent_page_length + 1, main_menu))
        rental_menu.add_page(PreviousPage(rental_page_length + 1, main_menu))

        main_menu.add_page(rent_menu)
        main_menu.add_page(rental_menu)
        main_menu.add_page(ExitPage(3))
        return main_menu

    def create_rental(self, page_id: int, menu_name: str) -> NavigationMenu:
        menu_service = self.container.get_class(MenuService)
        pages = [
            CreateRentalPage(1, menu_service),
            UpdateRentalPage(2, menu_service),
            DeleteRentalPage(3, menu_service),
            ListRentalPage(4, menu_service),
        ]
        return NavigationMenu(page_id, menu_name, pages)

    def create_rent(self, page_id: int, menu_name: str) -> NavigationMenu:
        menu_service = self.container.get_class(MenuService)
        pages = [
            CreateRentPage(1, menu_service),
            RentListPage(2, menu_service),
            DeleteRentPage(3, menu_service),
        ]
        return NavigationMenu(page_id, menu_name, pages)
