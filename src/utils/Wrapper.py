from typing import TypeVar, Generic

T = TypeVar("T")


class Wrapper(Generic[T]):
    def __init__(self, obj: T = None) -> None:
        super().__init__()
        self.wrapped_obj = obj
        self.errors: list[str] = list()

    def add_error(self, error: str) -> None:
        if error != "":
            self.errors.append(error)

    def get_errors(self) -> list[str]:
        return self.errors

    def get_wrapped_obj(self) -> T:
        return self.wrapped_obj

    def set_wrapped_obj(self, value: T) -> None:
        self.wrapped_obj = value
