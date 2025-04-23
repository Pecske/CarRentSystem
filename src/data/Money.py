class Money:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def get_amount(self) -> int:
        return self.amount

    def set_amount(self, value: int) -> None:
        self.amount = value

    def get_currency(self) -> str:
        return self.currency

    def set_currency(self, value: str) -> None:
        self.currency = value

    def __hash__(self):
        return hash(4 * hash(self.amount) * hash(self.currency))

    def __str__(self):
        return f"Amount: {self.amount} {self.currency}"