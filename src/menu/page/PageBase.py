from abc import abstractmethod
from menu.utils.PageItem import PageItem
from dto.ViewBase import ViewBase
from utils.TextType import TextType
from utils.TextCache import TextCache
import sys
import os


class PageBase(ViewBase):
    def __init__(self, page_id: int, menu_name: TextType) -> None:
        super().__init__(page_id)
        self.item = PageItem()
        self.cache: TextCache = TextCache.get_instance()
        self.menu_name = menu_name

    @abstractmethod
    def run(self) -> ViewBase:
        # self.clear_console()
        self._print_header()

    def _print_header(self) -> None:
        name_length = len(self.get_name())
        header = "\n"
        dash_line = ""
        for i in range(name_length):
            dash_line += "-"
        header += dash_line + "\n" + self.get_name() + "\n" + dash_line
        print(header)

    def get_id(self) -> int:
        return super().get_id()

    def set_id(self, value) -> None:
        return super().set_id(value)

    def get_name(self) -> str:
        return self.cache.get_text(self.menu_name)

    def get_item(self) -> PageItem:
        return self.item

    def get_cache(self) -> TextCache:
        return self.cache

    def get_text_from_cache(self, text_type: TextType) -> str:
        return self.get_cache().get_text(text_type)

    def print(self) -> None:
        return f"[{self.get_id()}] {self.get_name()}"

    def clear_console(self) -> None:
        if sys.platform == "win32":
            os.system("cls")
        else:
            print("\033[H\033[3J", end="")
