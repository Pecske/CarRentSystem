from menu.PageBase import PageBase
from dto.RentView import RentView
from menu.MenuService import MenuService
from menu.Item import Item


class RemoveRentPage(PageBase):
    def __init__(self, page_id, serivce: MenuService) -> None:
        super().__init__(page_id, "Remove Rent")
        self.service = serivce

    def _get_rent_id(self) -> int:
        question = "Which rent would u like to discard?"
        source = self.service.get_all_rents()
        return self.get_item().get_selection_result(Item(question, source))

    def _remove_rent(self, rent_id: int) -> None:
        self.service.remove_rent_by_id(rent_id)

    def run(self) -> None:
        rent_id = self._get_rent_id()
        self._remove_rent(rent_id)
