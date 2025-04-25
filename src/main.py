from menu.page.MainPage import MainPage
from utils.DependencyController import DependencyController


def main() -> None:
    container = DependencyController()
    main_page = MainPage(container, 0, "Main Page")
    main_page.run()


if __name__ == "__main__":
    main()
