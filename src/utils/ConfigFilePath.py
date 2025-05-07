from utils.Serializeable import Serializeable
from controller.ControllerBase import ControllerBase


class ConfigFilePath:
    def __init__(
        self,
        path: str,
        serializeable: type[Serializeable],
        controller: type[ControllerBase],
        exportable: bool,
    ):
        self.path = path
        self.serializeable = serializeable
        self.controller = controller
        self.exportable = exportable

    def get_path(self) -> str:
        return self.path

    def get_serializeable(self) -> type[Serializeable]:
        return self.serializeable

    def get_controller(self) -> type[ControllerBase]:
        return self.controller

    def is_exportable(self) -> bool:
        return self.exportable
