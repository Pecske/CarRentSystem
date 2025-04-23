from menu.PageBase import PageBase
from menu.MenuService import MenuService
from menu.Item import Item


class RentListPage(PageBase):
    def __init__(self, page_id, service: MenuService) -> None:
        super().__init__(page_id, "List Rents")
        self.service = service

    def _get_rents(self) -> None:
        question = "Go back? (y/n): "
        source = self.service.get_all_rents()
        self.get_item().get_view_result(Item(question, source))

    def run(self) -> None:
        self.print_header()
        self._get_rents()
