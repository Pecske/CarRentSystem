from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.utils.Item import Item


class ListRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, "List Car Rentals")
        self.service = service

    def _get_rentals(self) -> None:
        question = "Go back?"
        source = self.service.get_all_rentals()
        self.get_item().get_view_result(Item(question, source))

    def run(self) -> None:
        super().run()
        self._get_rentals()
