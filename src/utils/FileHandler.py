import json
from dto.CarRentalView import CarRentalView
from dto.RentView import RentView


class FileHandler:
    def __init__(self) -> None:
        pass

    def _read_file(self, path: str):
        with open(path, encoding="utf-8") as f:
            read = json.load(f)
        return read

    def read_car_rentals(self, path: str) -> list[CarRentalView]:
        car_rentals = self._read_file(path)
        result: list[CarRentalView] = list()
        if len(car_rentals) > 0:
            for car_rental in car_rentals:
                result.append(CarRentalView.de_serialize(car_rental))
        else:
            raise Exception("Invalid car rental json format!")
        return result

    def read_rents(self, path: str) -> list[RentView]:
        rents = self._read_file(path)
        result: list[RentView] = list()
        if len(rents) > 0:
            for rent in rents:
                result.append(RentView.de_serialize(rent))
        else:
            raise Exception("Invalid rent json format!")

        return result
