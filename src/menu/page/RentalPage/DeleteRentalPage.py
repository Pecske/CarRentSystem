from menu.page.PageBase import PageBase
from menu.service.MenuService import MenuService
from menu.utils.Item import Item
from utils.TextType import TextType


class DeleteRentalPage(PageBase):
    def __init__(self, page_id: int, service: MenuService) -> None:
        super().__init__(page_id, TextType.Rental_Delete_Menu)
        self.service = service

    def _get_rental_id(self) -> int:
        question = self.get_text_from_cache(TextType.Rental_Delete_Id)
        source = self.service.get_all_rentals()
        return self.get_item().get_selection_result(Item(question, source))

    def run(self):
        super().run()
        rental_id = self._get_rental_id()
        self.service.delete_rental_by_id(rental_id)
