from menu.page.PageBase import PageBase
import sys


class ExitPage(PageBase):
    def __init__(self, page_id: int) -> None:
        super().__init__(page_id, "Exit program")

    def _is_exit(self) -> bool:
        question = "Are you sure you want to quit?"
        return self.item.get_yes_no_result(question)

    def run(self) -> None:
        super().run()
        if self._is_exit():
            sys.exit()
