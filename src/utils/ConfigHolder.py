from utils.ConfigFilePath import ConfigFilePath
from dto.CarRentalView import CarRentalView
from dto.RentView import RentView
from controller.CarRentalController import CarRentalController
from controller.RentController import RentController
from utils.Text import Text
from utils.TextCache import TextCache


class ConfigHolder:

    CAR_RENTAL_PATH = "resources/carrental.json"
    RENTS_PATH = "resources/rents.json"
    LANGUAGE_PATH = "resources/texts.json"

    def __init__(self):
        self.file_configs: list[ConfigFilePath] = [
            ConfigFilePath(
                self.CAR_RENTAL_PATH, CarRentalView, CarRentalController, True
            ),
            ConfigFilePath(self.RENTS_PATH, RentView, RentController, True),
            ConfigFilePath(self.LANGUAGE_PATH, Text, TextCache, False),
        ]

    def get_file_configs(self) -> list[ConfigFilePath]:
        return self.file_configs

    def add_config(self, config: ConfigFilePath) -> None:
        self.file_configs.append(config)
