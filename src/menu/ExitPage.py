from menu.PageBase import PageBase
import sys


class ExitPage(PageBase):
    def __init__(self, page_id: int):
        super().__init__(page_id, "Exit program")

    def _is_exit(self) -> bool:
        question = "Are you sure you want to quit?(y/n) :"
        return self.item.get_yes_no_result(question)

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def run(self):
        if self._is_exit():
            sys.exit()
