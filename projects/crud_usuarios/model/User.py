import csv
import json
from io import StringIO


class User:
    def __init__(
        self,
        id: str = "",
        nombre: str = "",
        ape1: str = "",
        ape2: str = "",
        fechanac: str = "",
    ):
        self._id = id
        self._nombre = nombre
        self._ape1 = ape1
        self._ape2 = ape2
        self._fechanac = fechanac

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def ape1(self):
        return self._ape1

    @property
    def ape2(self):
        return self._ape2

    @property
    def fechanac(self):
        return self._fechanac

    def serialize(self) -> dict[str, str]:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "ape1": self._ape1,
            "ape2": self._ape2,
            "fechanac": self._fechanac,
        }

    def to_json(self) -> str:
        return json.dumps(self.serialize())

    def to_csv(self, write_header: bool = True) -> str:
        buffer = StringIO()
        writer = csv.DictWriter(buffer, fieldnames=self.serialize().keys())
        if write_header:
            writer.writeheader()
        writer.writerow(self.serialize())
        return buffer.getvalue()
