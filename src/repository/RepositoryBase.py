from abc import ABC, abstractmethod
from data.DataBase import DataBase


class RepositoryBase(ABC):

    def __init__(self):
        super().__init__()
        self.datas: dict[int, DataBase] = dict()

    @abstractmethod
    def get_data_by_id(self, id: int) -> DataBase:
        return self.datas.get(id)

    @abstractmethod
    def get_all_datas(self) -> list[DataBase]:
        return self.datas.values()

    @abstractmethod
    def save_or_update(self, data: DataBase) -> None:
        self.datas[data.get_id()] = data

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        self.datas.pop(id)
