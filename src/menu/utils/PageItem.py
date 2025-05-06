from dto.ViewBase import ViewBase
from datetime import date
from menu.utils.Item import Item


class PageItem:
    def __init__(self):
        pass

    def _selection_item(self, question: str, options: list[ViewBase]) -> int:
        picked_option: int | None = None
        if len(question) > 0:
            print("\n" + question + "\n")
        valid_ids: list[int] = list()
        if len(options) > 0:
            for option in options:
                valid_ids.append(option.get_id())
                print(option.print())
            # print("\n")
            while True:
                try:
                    picked_option = int(input("Id: "))
                    if picked_option in valid_ids:
                        break
                    else:
                        raise Exception("Valid id must be given!")
                except ValueError:
                    print("Id must be a number!")
                except Exception as e:
                    print(str(e))
            return picked_option
        else:
            raise Exception("There are no items to choose from!")

    def _yes_no_item(self, question: str) -> bool:
        while True:
            answer = input("\n" + question + " (y/n):")
            if answer.lower() == "y":
                return True
            elif answer.lower() == "n":
                return False
            else:
                print("y or n is allowed!")

    def _date_picker_item(self, question: str) -> date:
        while True:
            try:
                picked_date = input(f"\n{question} (yyyy-mm-dd): ")
                year, month, day = map(int, picked_date.split("-"))
                rental_date = date(year=year, month=month, day=day)
                if rental_date > date.today():
                    break
                else:
                    raise Exception("Date must be in the future!")
            except ValueError:
                print("Date must be in the follinwg format: yyyy-mm-dd!")
            except Exception as e:
                print(str(e))
        return rental_date

    def _view_only_item(self, source: list[ViewBase]) -> None:
        for item in source:
            print(item)
        # print("\n")

    def _text_item(self, question: str) -> str:
        while True:
            text = input(question)
            if len(text) > 0:
                return text
            else:
                print("Text can't be empty!")

    def _positive_int_text_item(self, question: str) -> int:
        while True:
            try:
                text = input("\n" + question)
                if len(text) > 0:
                    parsed_result = int(text)
                    if parsed_result > 0:
                        return int(text)
                    else:
                        print("Positive numbers are allowed!")
                else:
                    print("Text can't be empty!")
            except ValueError:
                print("Only numbers are allowed!")

    def get_selection_result(self, item: Item) -> int:
        return self._selection_item(item.get_question(), item.get_source())

    def get_date_result(self, question: str) -> date:
        return self._date_picker_item(question)

    def get_yes_no_result(self, question: str) -> bool:
        return self._yes_no_item(question)

    def get_view_result(self, item: Item) -> bool:
        self._view_only_item(item.get_source())
        while True:
            if self.get_yes_no_result(item.get_question()):
                break

    def get_text_result(self, item: Item) -> str:
        return self._text_item(item.get_question())

    def get_int_text_result(self, item: Item) -> int:
        return self._positive_int_text_item(item.get_question())
