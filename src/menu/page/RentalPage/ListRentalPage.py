from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.utils.Item import Item
from utils.TextType import TextType


class ListRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, TextType.Rental_List_Menu)
        self.service = service

    def _get_rentals(self) -> None:
        question = self.get_text_from_cache(TextType.Rental_List_Back)
        source = self.service.get_all_rentals()
        self.get_item().get_view_result(Item(question, source))

    def run(self) -> None:
        super().run()
        self._get_rentals()
