from utils.LanguageType import LanguageType
from utils.Serializeable import Serializeable
from utils.TextType import TextType

NAME = "name"
LANG = "lang"


class Text(Serializeable):
    def __init__(self, name: str, texts: dict[LanguageType, str] = None):   
        for type in TextType:
            if type.name.lower() == name.lower():   
                id = type.value
                self.name = type
        super().__init__(id)
        self.texts = texts if texts is not None else dict()

    def get_text_by_lang(self, lang: LanguageType) -> str:
        return self.texts.get(lang)

    def add_text(self, lang: LanguageType, text: str) -> None:
        self.texts[lang] = text

    def get_id(self):
        return super().get_id()

    def set_id(self, value):
        return super().set_id(value)

    def get_name(self) -> TextType:
        return self.name

    def set_name(self, value: TextType) -> None:
        self.name = value

    def serialize(self):
        langs: dict[str, str] = dict()
        for k, v in self.texts.items():
            langs[k.name.lower()] = v

        return {NAME: self.get_name().name, LANG: langs}

    def de_serialize(dct: dict[str, str]):
        try:
            name = dct.get(NAME)
            texts: dict[LanguageType, str] = dict()
            langs: dict[str, str] = dct.get(LANG)
            for k, v in langs.items():
                for type in LanguageType:
                    if type.name.lower() == k.lower():
                        texts[type] = v
            return Text(name, texts)

        except Exception as e:
            print(e)
            raise Exception("Deserialization of Text failed!")

    def print(self):
        lang = ""
        for k, v in self.texts.items():
            lang += f"{k}:{v}\n"
        return f"{self.get_name().name}" + lang
