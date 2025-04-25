from dto.ViewBase import ViewBase


class Item:
    def __init__(
        self,
        question: str,
        source: list[ViewBase] = None,
    ) -> None:
        self.question = question
        self.source = source

    def get_question(self) -> str:
        return self.question

    def set_question(self, value: str) -> None:
        self.question = value

    def get_source(self) -> list[ViewBase]:
        return self.source

    def set_source(self, value: list[ViewBase]) -> None:
        self.source = value
