from utils.FileService import FileService
from utils.DependencyController import DependencyController
from menu.MenuFactory import MenuFactory


class MainMenu:

    CAR_RENTAL_PATH = "resources/carrental.json"
    RENTAL_PATH = "resources/rents.json"

    def __init__(self) -> None:
        self.container = DependencyController()
        self._init_data()
        self.factory = MenuFactory(self.container)

    def _init_data(self) -> None:
        file_service = self.container.get_class(FileService)
        try:
            file_service.save_car_rental(self.CAR_RENTAL_PATH)
            file_service.save_rents(self.RENTAL_PATH)
        except Exception as e:
            print(str(e))

    def run(self) -> None:
        main_menu = self.factory.create_main()

        while True:
            main_menu.run()
