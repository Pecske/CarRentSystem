from utils.FileService import FileService
from utils.DependencyController import DependencyController
from menu.MenuFactory import MenuFactory
import sys


class MainMenu:

    CAR_RENTAL_PATH = "resources/carrental.json"
    RENTS_PATH = "resources/rents.json"
    LANGUAGE_PATH = "resources/texts.json"

    def __init__(self) -> None:
        self.container = DependencyController.get_instance()
        self._init_data()
        self.factory = MenuFactory()

    def _init_data(self) -> None:
        # file_service = self.container.get_class(FileService)
        file_service: FileService = FileService.get_instance()
        try:
            # file_service.save_car_rental(self.CAR_RENTAL_PATH)
            # file_service.save_rents(self.RENTS_PATH)
            # file_service.save_texts(self.LANGUAGE_PATH)
            file_service.import_data()

        except Exception as e:
            print(str(e))

    def run(self) -> None:
        try:
            main_menu = self.factory.create_main()

            while True:
                main_menu.run()
        except Exception as e:
            print(e)
        finally:
            sys.exit()
