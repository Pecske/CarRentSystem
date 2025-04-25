from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.page.RentalPage.CreateRentalPage import CreateRentalPage
from menu.page.RentalPage.UpdateRentalPage import UpdateRentalPage
from menu.page.RentalPage.DeleteRentalPage import DeleteRentalPage
from menu.page.RentalPage.ListRentalPage import ListRentalPage
from menu.utils.Item import Item


class ManageRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, "Manage Rental")
        self.service = service
        self.pages = (
            # Create Rental
            CreateRentalPage(1, service),
            # Add car to existing rental
            # Remove car from existing rental
            UpdateRentalPage(2, service),
            # Delete rental
            DeleteRentalPage(3, service),
            # List Rental
            ListRentalPage(4, service),
        )

    def _select_page(self) -> int:
        menu_item = Item("", self.pages)
        return self.get_item().get_selection_result(menu_item)

    def run(self) -> None:
        super().run()
        selected_page = self._select_page()
        for page in self.pages:
            if page.get_id() == selected_page:
                page.run()
                break
