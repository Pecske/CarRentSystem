from utils.FileHandler import FileHandler
from utils.ConfigHolder import ConfigHolder
from utils.ConfigFilePath import ConfigFilePath
from utils.DependencyController import DependencyController


class FileService:

    _instance = None

    def __init__(self) -> None:
        self.container = DependencyController.get_instance()
        self.handler = self.container.get_class(FileHandler)
        self.config_holder = self.container.get_class(ConfigHolder)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = FileService()
        return cls._instance

    def _join_errors(self, errors: list[str]) -> str:
        errors_joined = ""
        for error in errors:
            errors_joined += f"{error}\n"
        return errors_joined

    def _import_file(self, config: ConfigFilePath, errors: str) -> None:
        imported_datas = self.handler.read(
            config.get_serializeable(), config.get_path()
        )
        controller = self.container.get_class(config.get_controller())
        for data in imported_datas:
            saved_data = controller.save_or_update(data)
            if len(saved_data.get_errors()) > 0:
                errors += self._join_errors(saved_data.get_errors())

    def import_data(self) -> None:
        file_configs = self.config_holder.get_file_configs()
        errors: str = ""
        for config in file_configs:
            self._import_file(config, errors)
        if len(errors) > 0:
            raise Exception(errors)

    def export_data(self) -> None:
        file_configs = self.config_holder.get_file_configs()
        for config in file_configs:
            if config.is_exportable():
                controller = self.container.get_class(config.get_controller())
                result = controller.get_all_data()
                if len(result.get_errors()) == 0:
                    self.handler.write(result.get_wrapped_obj(), config.get_path())
