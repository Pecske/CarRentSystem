import json
from utils.Serializeable import Serializeable
from dto.ViewBase import ViewBase


class FileHandler:
    def __init__(self) -> None:
        pass

    def _read_file(self, path: str) -> dict[str, str]:
        with open(path, encoding="utf-8") as f:
            read = json.load(f)
        return read

    def _write_file(self, dicts: list[dict[str, str]], destination: str) -> None:
        with open(destination, "w", encoding="utf-8") as f:
            json.dump(dicts, f, ensure_ascii=False, indent=4)

    def read(self, serializeable: type[Serializeable], path: str) -> list[ViewBase]:
        datas = self._read_file(path)
        results: list[ViewBase] = list()
        if len(datas) > 0:
            for data in datas:
                results.append(serializeable.de_serialize(data))
        else:
            raise Exception(f"Invalid {serializeable} json format!")
        return results

    def write(self, serializeables: list[Serializeable], destination: str) -> None:
        result: list[dict[str, str]] = list()
        for serializeable in serializeables:
            result.append(serializeable.serialize())
        self._write_file(result, destination)
