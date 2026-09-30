class User:
    def __init__(self, id: str, nombre: str, ape1: str, ape2: str, fechanac: str):
        self._id = id
        self._nombre = nombre
        self._ape1 = ape1
        self._ape2 = ape2
        self._fechanac = fechanac
        # self._id = User._sanitize(id)
        # self._nombre = User._sanitize(nombre)
        # self._ape1 = User._sanitize(ape1)
        # self._ape2 = User._sanitize(ape2)
        # self._fechanac = User._sanitize(fechanac)

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
