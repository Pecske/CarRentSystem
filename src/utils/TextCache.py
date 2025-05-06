from utils.Text import Text
from utils.LanguageType import LanguageType
from utils.TextType import TextType


class TextCache(object):

    _instance = None

    def __init__(self):
        self.lang = LanguageType.Hun
        self.texts: dict[TextType, Text] = dict()

    def get_instance():
        if TextCache._instance is None:
            TextCache._instance = TextCache()
        return TextCache._instance

    def get_lang(self) -> str:
        return self.lang

    def set_lang(self, value: LanguageType) -> None:
        self.lang = value

    def add_to_texts(self, key: TextType, value: Text) -> None:
        self.texts[key] = value
    
    def get_text(self, text_type : TextType) -> str:
        return self.texts.get(text_type).get_text_by_lang(self.lang)
