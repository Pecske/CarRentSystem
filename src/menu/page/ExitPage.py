from menu.page.PageBase import PageBase
from utils.TextType import TextType
from utils.FileService import FileService
import sys


class ExitPage(PageBase):
    def __init__(self, page_id: int) -> None:
        super().__init__(page_id, TextType.Exit_Menu)
        self.service = FileService.get_instance()

    def _is_exit(self) -> bool:
        question = self.get_text_from_cache(TextType.Exit_Sure_Exit)
        return self.get_item().get_yes_no_result(question)

    def _is_save(self) -> bool:
        question = self.get_text_from_cache(TextType.Exit_Save)
        return self.get_item().get_yes_no_result(question)

    def run(self) -> None:
        super().run()
        save = self._is_save()
        if self._is_exit():
            if save:
                self.service.export_data()
            sys.exit()
