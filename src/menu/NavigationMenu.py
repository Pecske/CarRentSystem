from menu.page.PageBase import PageBase
from menu.utils.Item import Item
from utils.TextType import TextType


class NavigationMenu(PageBase):
    def __init__(
        self, page_id: int, menu_name: TextType, pages: list[PageBase] = None
    ) -> None:
        super().__init__(page_id, menu_name)
        self.pages = pages if pages is not None else list()

    def add_page(self, page: PageBase) -> None:
        self.pages.append(page)

    def remove_page(self, page: PageBase) -> None:
        self.pages.remove(page)

    def get_pages(self) -> list[PageBase]:
        return self.pages

    def _select_page(self) -> int:
        menu_item = Item("", self.pages)
        return self.get_item().get_selection_result(menu_item)

    def run(self):
        super().run()
        selected_page = self._select_page()
        for page in self.pages:
            if page.get_id() == selected_page:
                page.run()
                break
