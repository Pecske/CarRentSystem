from abc import abstractmethod
from dto.ViewBase import ViewBase


class Serializeable(ViewBase):
    def __init__(self, id: int):
        super().__init__(id)

    @abstractmethod
    def serialize(self) -> dict[str, str]:
        raise NotImplementedError

    @abstractmethod
    def de_serialize(dct: dict[str, str]) -> ViewBase:
        raise NotImplementedError
