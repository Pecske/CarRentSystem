from abc import ABC, abstractmethod


class WrapperBase(ABC):
    def __init__(self):
        super().__init__()
        self.errors: list[str] = list()

    @abstractmethod
    def add_error(self, error: str) -> None:
        if error != "":
            self.errors.append(error)

    @abstractmethod
    def get_errors(self) -> list[str]:
        return self.errors
