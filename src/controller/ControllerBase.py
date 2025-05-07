from abc import ABC, abstractmethod
from dto.ViewBase import ViewBase
from utils.Wrapper import Wrapper


class ControllerBase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def save_or_update(self, view: ViewBase) -> Wrapper[ViewBase]:
        raise NotImplementedError

    @abstractmethod
    def get_data_by_id(self, id: int) -> Wrapper[ViewBase]:
        raise NotImplementedError

    @abstractmethod
    def get_all_data(self) -> Wrapper[list[ViewBase]]:
        raise NotImplementedError

    @abstractmethod
    def remove_data_by_id(self, id: int) -> Wrapper[ViewBase]:
        raise NotImplementedError
