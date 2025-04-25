from typing import TypeVar, Generic

T = TypeVar("T")


class ValidationResult(Generic[T]):

    def __init__(self, valid: bool, error_msg: str = None, result: T = None):
        self.valid = valid
        self.error_msg = error_msg
        self.result = result

    def is_valid(self) -> bool:
        return self.valid

    def set_valid(self, value: bool) -> None:
        self.valid = value

    def get_result(self) -> T:
        return self.result

    def set_result(self, value: T) -> None:
        self.result = value

    def get_error_msg(self) -> str:
        return self.error_msg

    def set_error_msg(self, value: str) -> None:
        self.error_msg = value
