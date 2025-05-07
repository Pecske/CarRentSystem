from utils.Text import Text
from utils.LanguageType import LanguageType
from utils.TextType import TextType
from controller.ControllerBase import ControllerBase
from utils.Wrapper import Wrapper


class TextCache(ControllerBase):

    _instance = None

    def __init__(self):
        super().__init__()
        self.lang = LanguageType.Hun
        self.texts: dict[TextType, Text] = dict()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TextCache()
        return cls._instance

    def get_lang(self) -> str:
        return self.lang

    def set_lang(self, value: LanguageType) -> None:
        self.lang = value

    def save_or_update(self, text: Text) -> Wrapper[Text]:
        self.texts[text.get_name()] = text
        return Wrapper(text)

    def get_text(self, text_type: TextType) -> str:
        return self.texts.get(text_type).get_text_by_lang(self.lang)

    def get_all_data(self) -> Wrapper[list[Text]]:
        return Wrapper(self.texts.values())

    def get_data_by_id(self, id) -> Wrapper[Text]:
        found_data = self.texts.get(TextType(id))
        result = Wrapper(found_data)
        if found_data is None:
            result.add_error("Text not found by id!")
        return result

    def remove_data_by_id(self, id):
        return Wrapper(self.texts.pop(TextType(id)))
