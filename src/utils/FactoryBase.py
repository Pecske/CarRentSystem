from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")


class FactoryBase(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def map_data_to_view(data: T) -> U:
        raise NotImplementedError

    @abstractmethod
    def map_view_to_data(view: U) -> T:
        raise NotImplementedError
