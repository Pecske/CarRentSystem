from menu.MainPage import MainPage
from utils.DependencyController import DependencyController

def main() -> None:
    container = DependencyController()
    main = MainPage(container,0, "Main Page")
    main.run()
    pass


if __name__ == "__main__":
    main()
