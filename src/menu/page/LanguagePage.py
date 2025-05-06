from menu.page.PageBase import PageBase
from utils.TextCache import TextCache
from utils.TextType import TextType
from utils.LanguageType import LanguageType
from menu.utils.Item import Item
from menu.utils.MenuOption import MenuOption


class LanguagePage(PageBase):
    def __init__(self, page_id):
        super().__init__(page_id, TextType.Choose_Language_Menu)

    def _choose_language(self) -> int:
        question = self.get_text_from_cache(TextType.Language_Select)
        options: list[MenuOption] = list()
        for lang_type in LanguageType:
            options.append(MenuOption(lang_type.value, lang_type.name))

        return self.get_item().get_selection_result(Item(question, options))

    def run(self):
        super().run()
        chosen_lang = self._choose_language()
        self.get_cache().set_lang(LanguageType(chosen_lang))
