from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.utils.Item import Item
from utils.TextType import TextType


class DeleteRentPage(PageBase):
    def __init__(self, page_id, serivce: MenuService) -> None:
        super().__init__(page_id, TextType.Rent_Delete_Menu)
        self.service = serivce

    def _get_rent_id(self) -> int:
        question = self.get_text_from_cache(TextType.Rent_Delete_Id)
        source = self.service.get_all_rents()
        return self.get_item().get_selection_result(Item(question, source))

    def _remove_rent(self, rent_id: int) -> None:
        self.service.delete_rent_by_id(rent_id)

    def run(self) -> None:
        super().run()
        rent_id = self._get_rent_id()
        self._remove_rent(rent_id)
