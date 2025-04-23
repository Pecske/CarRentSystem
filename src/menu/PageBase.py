from abc import abstractmethod
from menu.PageItem import PageItem
from dto.ViewBase import ViewBase


class PageBase(ViewBase):
    def __init__(self, page_id: int, menu_name: str) -> None:
        super().__init__(page_id)
        self.item = PageItem()
        self.menu_name = menu_name

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def get_id(self) -> int:
        return super().get_id()

    def set_id(self, value) -> None:
        return super().set_id(value)

    def get_name(self) -> str:
        return self.menu_name

    def get_item(self) -> PageItem:
        return self.item

    def print(self) -> None:
        return f"[{self.get_id()}] {self.get_name()}"

    def print_header(self) -> None:
        print(self.get_name())
        dash_line = ""
        for i in range(len(self.get_name())):
            dash_line += "-"
        print(dash_line + "\n")
