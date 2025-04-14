from repository.RepositoryBase import RepositoryBase


class CarRenalRepository(RepositoryBase):
    def __init__(self):
        super().__init__()

    def save_or_update(self, data):
        return super().save_or_update(data)

    def get_data_by_id(self, id):
        return super().get_data_by_id(id)

    def get_all_datas(self):
        return super().get_all_datas()

    def delete_by_id(self, id):
        return super().delete_by_id(id)
