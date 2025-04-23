from abc import ABC, abstractmethod
from data.DataBase import DataBase


class RepositoryBase(ABC):

    def __init__(self):
        super().__init__()
        self.id_counter = 1
        self.datas: dict[int, DataBase] = dict()

    @abstractmethod
    def get_data_by_id(self, id: int) -> DataBase:
        return self.datas.get(id)

    @abstractmethod
    def get_all_datas(self) -> list[DataBase]:
        return self.datas.values()

    @abstractmethod
    def save_or_update(self, data: DataBase) -> DataBase:
        id = data.get_id()
        if id == None:
            id = self.id_counter
            data.set_id(id)
            self.id_counter += 1

        self.datas[id] = data
        return data

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        self.datas.pop(id)
