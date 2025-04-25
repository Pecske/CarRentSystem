from dto.ViewBase import ViewBase


class MenuOption(ViewBase):
    def __init__(self, id: int, option_name: str) -> None:
        super().__init__(id)
        self.option_name = option_name

    def get_id(self) -> int:
        return super().get_id()

    def set_id(self, value) -> None:
        return super().set_id(value)

    def get_option_name(self) -> str:
        return self.option_name

    def set_option_name(self, value: str) -> None:
        self.option_name = value

    def print(self) -> str:
        return f"[{self.get_id()}] {self.get_option_name()}"
