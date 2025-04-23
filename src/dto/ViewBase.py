from abc import ABC, abstractmethod


class ViewBase(ABC):

    def __init__(self, id: int):
        self.id = id

    @abstractmethod
    def get_id(self) -> int:
        return self.id

    @abstractmethod
    def set_id(self, value: int) -> None:
        self.id = value

    @abstractmethod
    def print(self) -> str:
        raise NotImplementedError
