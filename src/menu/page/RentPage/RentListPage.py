from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.utils.Item import Item
from utils.TextType import TextType


class RentListPage(PageBase):
    def __init__(self, page_id, service: MenuService) -> None:
        super().__init__(page_id, TextType.Rent_List_Menu)
        self.service = service

    def _get_rents(self) -> None:
        question = self.get_text_from_cache(TextType.Rent_List_Back)
        source = self.service.get_all_rents()
        return self.get_item().get_view_result(Item(question, source))

    def run(self) -> None:
        super().run()
        self._get_rents()
