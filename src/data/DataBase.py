from abc import ABC, abstractmethod


class DataBase(ABC):
    def __init__(self):
        super().__init__()
        self.id: None | int = None

    @abstractmethod
    def get_id(self) -> int:
        return self.id

    @abstractmethod
    def set_id(self, value: int) -> None:
        self.id = value
